from rest_framework import serializers
from .models import *

class CollegeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = ("static_id","name")
