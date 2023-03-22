from dj_rest_auth.views import LogoutView
from rest_framework import generics, permissions, mixins
from rest_framework.authtoken.admin import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from post.serializers import PostListSerializer
from . import serializers


class CustomViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


class UserRegisterView(generics.CreateAPIView):
    qs = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class UserViewSet(CustomViewSet):
    queryset = User.objects.all()
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.UserDetailSerializer
        return serializers.UserListSerializer

    @action(['GET'], detail=True)
    def favorites(self, requests, pk):
        user = self.get_object()
        posts = user.favorites.all()
        serializer = PostListSerializer(instance=posts, many=True)
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = (permissions.IsAuthenticated, )

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )