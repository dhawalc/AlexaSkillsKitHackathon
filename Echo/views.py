from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Echo.serializers import *


@api_view(['GET'])
def all_intents(request, **kwargs):
    intents = Intents.objects.all()

    serializers = IntentSerializer(intents, many=True)
    return Response(serializers.data)


@api_view(['POST'])
def input_command(request, **kwargs):
    intents=request.data['intents']
    print intents
    for o in intents:
        print o['intent']
        slots=o['slots']
        for i in slots:
            print i['name']

