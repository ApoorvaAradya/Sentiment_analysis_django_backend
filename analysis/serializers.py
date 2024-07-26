from rest_framework import serializers

class SentimentRequestSerializer(serializers.Serializer):
    text = serializers.CharField()

class SentimentResponseSerializer(serializers.Serializer):
    neg = serializers.FloatField()
    neu = serializers.FloatField()
    pos = serializers.FloatField()
    compound = serializers.FloatField()
