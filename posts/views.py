from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *
# Create your views here.

class CollegeListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CollegeListSerializer
    queryset = College.objects.all()
