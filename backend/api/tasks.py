from celery import shared_task
from core.models import ProcessingJob

@shared_task
def start_processing_pipeline(job_id):
    job = ProcessingJob.objects.get(id=job_id)
    job.status = "running"
    job.progress = 5
    job.save()

    # Stub — gerçek pipeline burada gelecek
    job.progress = 100
    job.status = "done"
    job.save()
