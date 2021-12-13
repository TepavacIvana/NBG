from rest_framework.response import Response

from korisnik.models import UserRegistration, UserLogin
from rest_framework import generics

from korisnik.models import UserRegistration, UserLogin
from korisnik.serializers import UserRegistrationSerializer, UserLoginSerializer


# view for listing all users or creating a new user
# function-based view

# @api_view(['GET', 'POST'])
# def user_list(request, format=None):
#
#     if request.method == "GET":
#         users = UserRegistration.objects.all()
#         serializer = UserRegistrationSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class-based view

# class UserList(APIView):
#
#     def get(self, request, format=None):
#         users = UserRegistration.objects.all()
#         serializer = UserRegistrationSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# mixin classes

# class UserList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = UserRegistration.objects.all()
#     serializer_class = UserRegistrationSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# generic class-based view

class UserList(generics.ListCreateAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
    name = 'Dobro dosli!'
    print('Dobro dosli!')


class UserDetail(generics.RetrieveAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
    lookup_field = 'id'


class Loger(generics.CreateAPIView):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer

