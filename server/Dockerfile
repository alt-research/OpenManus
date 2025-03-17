FROM python:3.12-slim

WORKDIR /app/OpenManus

# Install system dependencies and clean up in a single step
RUN apt-get update && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv && uv pip install --system --upgrade pip

# Copy only requirements first to leverage Docker caching
COPY requirements.txt ./
RUN uv pip install --system -r requirements.txt \
    && pip install --no-cache-dir playwright \
    && playwright install --with-deps \
    && apt-get purge -y git curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /root/.cache/pip

# Copy the rest of the project files
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 5001

# Run Uvicorn with ASGI app
CMD ["uvicorn", "server:asgi_app", "--host", "0.0.0.0", "--port", "5001"]

