# Use a stable Python base image
FROM python:3.11-slim

LABEL maintainer="VibeCoder Team"
LABEL version="1.2.0"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install UV (as recommended by ADK)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Create non-root user for security
RUN useradd -m vibecoder && chown -R vibecoder:vibecoder /app
USER vibecoder

# Copy project files
COPY --chown=vibecoder:vibecoder . .

# Install Python dependencies
RUN uv pip install --no-cache -r requirements.txt --system

# Default command to run the VibeCoder agent
CMD ["python", "-m", "src.vibe_coder.agent"]
