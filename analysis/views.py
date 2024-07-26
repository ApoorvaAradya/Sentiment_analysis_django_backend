from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .sentiment import analyze_sentiment
from .serializers import SentimentRequestSerializer, SentimentResponseSerializer

@api_view(['POST'])
def sentiment_view(request):
    serializer = SentimentRequestSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        sentiment = analyze_sentiment(text)
        response_serializer = SentimentResponseSerializer(sentiment)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
