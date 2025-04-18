# Use Python 3.9 as base image, create non-root user, set up environment and working directory
FROM python:3.9
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app

# Copy requirements and install dependencies without cache
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy app code and run FastAPI server with Uvicorn on port 7860
COPY --chown=user . /app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]
