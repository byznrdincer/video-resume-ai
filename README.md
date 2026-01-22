🎯 AI-Powered Video Resume Analyzer

Multi-modal AI system that analyzes video resumes using computer vision, audio processing, and NLP to generate talent scores and recruiter-friendly explanations.

📌 Overview

This project is a full product–level AI system that analyzes a student’s 1–2 minute video resume and automatically:

Extracts visual, audio, and textual features

Computes a Talent Score (0–100)

Generates subscores and human-readable explanations

Provides a recruiter-friendly dashboard

This is not a tutorial project.
It is a multi-modal ML pipeline built with production-grade backend architecture.

🎯 Key Outputs (v1 Full)

Talent Score (0–100)

Subscores

Confidence

Communication

Skill Relevance

Engagement

Explanation

Rule-based notes

(Optional) SHAP/LIME feature contributions

Recruiter Dashboard

Video list

Filters

Score detail page

🧠 System Architecture
Frontend (Django Templates + Vanilla JS)
        |
        v
Backend API (Django + DRF)
        |
        v
Celery Workers (Redis broker)
        |
        v
ML Pipeline
  - Video Processing
  - Audio Processing
  - Speech-to-Text
  - NLP
  - Feature Fusion
  - Scoring
        |
        v
PostgreSQL (metadata + results)
Storage (Local / S3)


React is optional.
The initial frontend uses Django templates + vanilla JS for faster iteration and stability.

🧩 Tech Stack
Backend

Python 3.10+

Django 4.x

Django REST Framework

PostgreSQL

Redis

Celery

FFmpeg

django-storages (optional S3/MinIO)

Computer Vision

OpenCV

MediaPipe

NumPy

SciPy

Audio Processing

librosa

soundfile

PyDub

FFmpeg

Speech-to-Text

OpenAI Whisper API

(Optional) Whisper local

NLP

spaCy

Sentence Transformers

scikit-learn

ML & Fusion

XGBoost / LightGBM

joblib

Explainability

SHAP

LIME

Frontend

Django templates

HTML + CSS (Bootstrap or Tailwind CDN)

Vanilla JS

Chart.js

Fetch API

🔌 API Endpoints
Method	Endpoint	Description
POST	/api/videos/	Upload a video resume
GET	/api/jobs/{job_id}/	Get processing status + progress
GET	/api/results/{video_id}/	Fetch scores + explanations
GET	/api/recruiter/videos/	List videos (optional filters)
📦 Data Models

Core models:

User

VideoResume

ProcessingJob

FeatureSet

TalentScore

RecruiterView (optional)

Design choice:
Feature vectors are stored as JSON initially for flexibility.
Normalization can be added later.

🎥 Video Processing

Libraries

OpenCV

MediaPipe

Extracted Features (v1)

Face detection success rate

Face landmark stability

Eye contact ratio

Smile ratio

Head movement variance

Frame quality metrics (blur, brightness)

Emotion Model

Rule-based / lightweight estimator (v1)

CNN (FER2013 / AffectNet) – Phase 2

🎧 Audio Processing

Libraries

librosa

soundfile

PyDub

Extracted Features

Pitch (mean, variance)

Energy stats

Pause ratio / silence ratio

Speaking rate

Volume stability

Deep Audio ML (Phase 2)

wav2vec2

🗣 Speech-to-Text

Recommended (v1):

Whisper API

Optional:

Whisper local (GPU recommended)

Outputs

Transcript

Timestamped segments

Confidence score (if available)

📝 NLP Pipeline

Libraries

spaCy

Sentence Transformers

Extracted Features

Skill keyword count

Buzzword density

Grammar proxy

Coherence proxy

Semantic relevance score

Models

all-MiniLM-L6-v2

mpnet-base

🔗 Feature Fusion & Scoring
v1 Strategy

Rule-based baseline scoring

ML model (XGBoost / LightGBM) – Phase 2

Fusion Inputs

video: eye_contact, smile_ratio, head_movement, face_detect_rate
audio: pitch_var, energy_mean, pause_ratio, speech_rate
text : skill_count, grammar_proxy, coherence_score, semantic_score


Outputs

Talent Score (0–100)

Subscores:

Confidence

Communication

Skill Relevance

Engagement

🔍 Explainability

v1

Rule-based notes

v2

SHAP

LIME

⚙ Async Pipeline (Celery)

Task Flow

ingest_video_task

extract_audio_task

stt_task

video_features_task

audio_features_task

nlp_features_task

fusion_and_score_task

explanation_task

Progress

Each task updates ProcessingJob.progress

🗂 Folder Structure
video_resume_ai/
  backend/
    config/
    api/
    core/
    ml/
    tasks/
    templates/
    static/
    celery_app.py
  data/
    videos/
    audio/
    temp/
  models/
    pretrained/
    scoring/
  docker/
    Dockerfile
    nginx.conf
  docker-compose.yml
  requirements.txt
  README.md

🚀 Deployment
Local / Dev

Docker

Docker Compose

PostgreSQL

Redis

Django (Gunicorn)

Celery Worker

Production

Nginx + Gunicorn

Celery worker (separate)

S3 storage (optional)

Monitoring + logging

🧪 Datasets (Phase 2)

FER2013 / AffectNet

RAVDESS / CREMA-D

Resume datasets

Skill keyword corpus

🧠 Training Strategy

v1: rule-based + heuristic scoring

v2: internal labeling + dataset creation

v3: ML fusion model training

⚠ What’s Hard

Multi-modal feature extraction stability

Celery pipeline orchestration

Training data collection

Explainability

Production deployment

Worker scaling

⏳ Build Time

MVP (end-to-end): 3–4 weeks

Full version: 6–10 weeks

Polished product: 10+ weeks

🎯 Final Note

This project demonstrates:

Multi-modal AI engineering

Production-grade backend architecture

Explainable ML scoring

Real-world ML pipeline design

This is not a toy project.
This is a real AI product.

📌 Status

🚧 Under active development
Phase 1: Core backend + async pipeline
