from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

from knox.models import AuthToken

from .models import Profile
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({ 
            'user': UserSerializer(user).data,
            # 'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({ 
            'user': UserSerializer(user).data,
            'token': token
        })

# class UserAPI(generics.RetrieveAPIView):
class UserAPI(viewsets.ViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def following(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    @action(detail=False, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    def username(self, request):
        username = request.data['username']
        request.user.username = username
        request.user.save()
        return Response({'username': username})

    @action(detail=False, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    def password(self, request):
        password = request.data['password']
        request.user.set_password(password)
        request.user.save()
        return Response({'password': password})

    @action(detail=True, methods=['post'])
    def follow(self, request, pk):
        qs = User.objects.filter(username=pk)
        other_user = qs.first()

        if (not qs.exists()):
            return Response({}, 404)
        
        request.user.profile.following.add(other_user.profile)
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk):
        qs = User.objects.filter(username=pk)
        other_user = qs.first()
        
        if (not qs.exists()):
            return Response({}, 404)
            
        request.user.profile.following.remove(other_user.profile)
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    # def get_object(self):
    #     return self.request.user

# class ProfileAPI(viewsets.ViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ProfileSerializer

#     @action(detail=True, methods=['post'])
#     def follow(self, request, pk):
#         qs = Profile.objects.filter(user__id=pk)
#         other_profile = qs.first()
#         qs = Profile.objects.filter(user=request.user)
#         my_profile = qs.first()
#         my_profile.following.add(other_profile)
#         serializer = UserSerializer()
#         return Response()

#     @action(detail=True, methods=['post'])
#     def follow(self, request, pk):
#         pass