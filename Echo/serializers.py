__author__ = 'qa'

from rest_framework import serializers

from Echo.models import *

class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intents
        fields = ('pk', 'intent')

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('pk', 'name')