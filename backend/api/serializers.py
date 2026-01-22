from rest_framework import serializers
from core.models import VideoResume

class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoResume
        fields = ["id", "file"]
