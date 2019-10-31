from rest_framework import generics
from user.serializers import UserSerializer
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

