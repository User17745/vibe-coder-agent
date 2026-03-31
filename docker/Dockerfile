# Use a stable Python base image
FROM python:3.11-slim

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

# Copy project files
COPY . .

# Install Python dependencies
# Note: google-adk should be in requirements.txt
RUN uv pip install -r requirements.txt --system

# Default command to run the VibeCoder agent
CMD ["python", "-m", "src.vibe_coder.agent"]
