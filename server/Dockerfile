FROM python:3.12-slim

WORKDIR /app/OpenManus

RUN apt-get update && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/* \
    && (command -v uv >/dev/null 2>&1 || pip install --no-cache-dir uv)

COPY . .

RUN uv pip install --system -r requirements.txt
RUN pip install --no-cache-dir playwright && playwright install --with-deps


# Expose the port Flask runs on
EXPOSE 5001

# Command to run the application
CMD ["python", "server.py"]

