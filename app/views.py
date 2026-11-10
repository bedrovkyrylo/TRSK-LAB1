from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


def utc_now_iso() -> str:
    """Поточний час UTC у форматі ISO 8601."""
    return datetime.now(timezone.utc).isoformat()


@app.route("/healthz/live", methods=["GET"])
def liveness_check():
    """Liveness: процес застосунку працює."""
    return jsonify({
        "status": "alive",
        "timestamp": utc_now_iso(),
    }), 200


@app.route("/healthz/ready", methods=["GET"])
def readiness_check():
    """Readiness: застосунок готовий приймати трафік."""
    # На етапі Лабораторної №1 підключення до БД відсутнє
    return jsonify({
        "status": "ready",
        "database": "not_connected_yet",
        "timestamp": utc_now_iso(),
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
