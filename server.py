import asyncio
from flask import Flask, request, jsonify
from asgiref.wsgi import WsgiToAsgi
from app.agent.manus import Manus
from app.logger import logger

app = Flask(__name__)
agent = Manus()

@app.route("/run", methods=["POST"])
async def run():
    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    prompt = data["prompt"].strip()
    if not prompt:
        return jsonify({"error": "Empty prompt provided."}), 400

    logger.warning("Processing request in background...")

    # Run `agent.run(prompt)` in the background
    asyncio.create_task(agent.run(prompt))

    # Return response immediately
    return jsonify({"message": "Request received. Processing in background."}), 202

# Convert Flask (WSGI) app to ASGI for Uvicorn
asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=5001)

