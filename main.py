from app_factory import create_app

app = create_app()

def entry_point(request):
    """Entrypoint for Google Cloud Function deployment."""
    # functions-framework --target=entry_point --debug
    return app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
