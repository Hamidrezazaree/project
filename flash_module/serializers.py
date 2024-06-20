from rest_framework import serializers

from flash_module.models import FlashCard
from django.contrib.auth.models import User

class CreateProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']



class CreateFlashCardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'


class UpdateFlashCardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['question','answer']

class DeleteFlashCardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['question','answer']


class ListFlashCardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'