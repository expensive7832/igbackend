from rest_framework import serializers
from .models import User
class userSerializer(serializers.ModelSerializer):
   class Meta:
    model = User 
    fields = ["first_name", "email", "password"]
