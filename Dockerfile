FROM python:3.12-slim

WORKDIR /app

# Copy the full project including pickle model
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install -r requirements.txt


# Making sure Python can find 'app' as a package, not used when running locally
ENV PYTHONPATH=/app

# Optional: Expose port (if using FastAPI uvicorn server)
EXPOSE 8000

# Run the app (adjust as needed)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]