FROM python:3.12-slim

WORKDIR /app/OpenManus

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/* \
    && (command -v uv >/dev/null 2>&1 || pip install --no-cache-dir uv)

# Copy project files
COPY . .

# Install Python dependencies
RUN uv pip install --system -r requirements.txt
RUN pip install --no-cache-dir playwright && playwright install --with-deps

# Expose the port Uvicorn will run on
EXPOSE 5001

# Run Uvicorn with server.py
CMD ["uvicorn", "server:asgi_app", "--host", "0.0.0.0", "--port", "5001"]

