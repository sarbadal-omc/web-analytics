from flask import Blueprint, Flask, url_for
from routes import home_bp, api_bp


def create_app() -> None:
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    app.extensions = getattr(app, 'extensions', {})

    app.register_blueprint(home_bp, url_prefix='')
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.context_processor
    def override_url_for():
        def _url_for(endpoint, **values):
            # Normal behavior for non-static files
            if endpoint != "static":
                return url_for(endpoint, **values)
    
            # For static, switch depending on ENV
            filename = values.get("filename", "")
            if app.config["ENV_TYPE"] == "prod":
                gcs_bucket_url = app.config.get("GCS_BUCKET_URL")
                return f"{gcs_bucket_url}/{filename}"
            else:
                return url_for(endpoint, **values)
    
        return dict(url_for=_url_for)

    return app
