from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import VideoResume, ProcessingJob
from .serializers import VideoUploadSerializer
from .tasks import start_processing_pipeline

class VideoUploadView(APIView):
    def post(self, request):
        serializer = VideoUploadSerializer(data=request.data)
        if serializer.is_valid():
            video = serializer.save()
            job = ProcessingJob.objects.create(video=video)

            start_processing_pipeline.delay(job.id)

            return Response(
                {"video_id": video.id, "job_id": job.id, "status": "queued"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
