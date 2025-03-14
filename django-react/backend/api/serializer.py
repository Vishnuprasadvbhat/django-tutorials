from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # To make password write only

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

        extra_kwargs = {'author': {'read_only': True }} # to make sure that author is not editable from the frontend

        