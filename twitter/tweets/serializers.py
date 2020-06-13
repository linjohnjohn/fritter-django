from django.conf import settings
from rest_framework import serializers

from .models import Freet, FreetLike

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH


class FreetSerializer(serializers.ModelSerializer):
    source_freet = serializers.PrimaryKeyRelatedField(read_only=True)
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Freet
        fields = ['content', 'id', 'likes', 'is_refreet', 'owner', 'source_freet']
