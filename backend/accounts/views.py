from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User

# Create your views here.
class UserRegister(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = AllowAny
    queryset = User.objects.all()


