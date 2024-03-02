FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN apt-get update \
    && apt-get install -y curl \
    && pip install --no-cache-dir -r /app/requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 80

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl --fail http://localhost:80/health || exit 1
