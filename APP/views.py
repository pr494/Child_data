from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer,ChildrenSerializer,MDataSerializer,ADataSerializer
from .models import manual,auto,child
from rest_framework import status,views
from rest_framework import viewsets

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    return Response({
        'status':status.HTTP_200_OK,
        'success':True,
        'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        'message': 'Success'
        
    })

@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'status':status.HTTP_200_OK,
            'success':True,
            'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'message': 'Success'
    })
    return Response({'error':'not authenticated'})

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            'status':status.HTTP_200_OK,
            'success':True,
            "data":{
            'id':user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": token
            },
            'message': 'Success'
            
        })
        
@api_view(['POST'])
def ADD_CHILD(request):
        serializer = ChildrenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_child(request, id=None):
        if id:
            Child = child.objects.get(id=id)
            serializer = ChildrenSerializer(Child)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = child.objects.all()
        serializer = ChildrenSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
@api_view(['POST'])
def ADD_mDATA(request):
        serializer = MDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ADD_aDATA(request):
        serializer = ADataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_data(request, id=None):
        if id:
            Data = auto.objects.get(id=id)
            serializer = ADataSerializer(Data)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = auto.objects.all()
        serializer = ADataSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    