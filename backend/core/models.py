from django.db import models

class VideoResume(models.Model):
    file = models.FileField(upload_to="videos/")
    duration = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"VideoResume {self.id}"

class ProcessingJob(models.Model):
    STATUS_CHOICES = [
        ("queued", "Queued"),
        ("running", "Running"),
        ("done", "Done"),
        ("failed", "Failed"),
    ]

    video = models.ForeignKey(VideoResume, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="queued")
    progress = models.IntegerField(default=0)
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.id} - {self.status}"

class FeatureSet(models.Model):
    video = models.OneToOneField(VideoResume, on_delete=models.CASCADE)
    video_features = models.JSONField(default=dict)
    audio_features = models.JSONField(default=dict)
    text_features = models.JSONField(default=dict)

class TalentScore(models.Model):
    video = models.OneToOneField(VideoResume, on_delete=models.CASCADE)
    total_score = models.FloatField()
    subscores = models.JSONField(default=dict)
    notes = models.JSONField(default=list)
    model_version = models.CharField(max_length=50, default="v1")
