import os

ENV_TYPE = os.getenv("ENV_TYPE", "dev")

def get_gcs_bucket_name() -> str:
    return os.getenv("GCS_BUCKET_NAME", "create-chart-demo")

def get_gcs_bucket_url(prefix: str = "web-analytics") -> str:
    bucket = get_gcs_bucket_name()
    return f"https://storage.googleapis.com/{bucket}/{prefix}/static"

class Config:
    ENV_TYPE = ENV_TYPE
    GCS_BUCKET_URL = get_gcs_bucket_url()

    SECRET_KEY = "?YCqd<Z2|7SkRZruG,5H|Mf4nJ!Up?"
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

