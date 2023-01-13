from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import child,manual,auto



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user
    
class MDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = manual
        fields =("child_id","Date","Manual_height","Manual_weight")
    def create(self, validated_data):
        data = manual(
            child_id=validated_data["child_id"],
            Date=validated_data["Date"],
            Manual_height=validated_data["Manual_height"],
            Manual_weight=validated_data["Manual_weight"],
        )
        return data
    
class ADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = auto
        fields =("child_id","Date","Auto_height","Auto_weight")
    def create(self, validated_data):
        adata = auto(
            child_id=validated_data["child_id"],
            Date=validated_data["Date"],
            Auto_height=validated_data["Auto_height"],
            Auto_weight=validated_data["Auto_weight"],
        )
        return adata
    
class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields =("id","User_id","First_name","Last_name","Gender","date_of_birth","Organization","Father_name","Father_mobile","Mother_name","State","District","Taluk","Village")
    def create(self, validated_data):
        children = child(
            User_id=validated_data["User_id"],
            First_name=validated_data["First_name"],
            Last_name=validated_data["Last_name"],
            Gender=validated_data["Gender"],
            date_of_birth=validated_data["date_of_birth"],
            Organization=validated_data["Organization"],
            Father_name=validated_data["Father_name"],
            Father_mobile=validated_data["Father_mobile"],
            Mother_name=validated_data["Mother_name"],
            State=validated_data["State"],
            District=validated_data["District"],
            Taluk=validated_data["Taluk"],
            Village=validated_data["Village"],

        )
        return children