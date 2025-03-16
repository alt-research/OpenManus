import asyncio
from flask import Flask, request, jsonify
from app.agent.manus import Manus
from app.logger import logger

app = Flask(__name__)
agent = Manus()

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    prompt = data["prompt"].strip()
    if not prompt:
        return jsonify({"error": "Empty prompt provided"}), 400

    logger.warning("Processing request...")

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(agent.run(prompt))
        return jsonify({"message": "Request processing completed."})
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
