import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def health():
    return jsonify({
        "status": "ok",
        "service": "AI Project Report Generator API"
    })

@app.post("/api/generate")
def generate():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Project title is required"}), 400

    # Demo response. Replace this block with your Gemini/OpenAI API call.
    report = {
        "title": title,
        "abstract": (
            f"This project, {title}, presents a technology-driven solution "
            "designed to address a practical problem through an accessible and "
            "structured system."
        ),
        "introduction": (
            "The project focuses on applying modern technologies to improve "
            "efficiency, automation, usability and reliability."
        ),
        "methodology": (
            "The methodology includes requirement analysis, system design, "
            "implementation, testing and evaluation."
        ),
        "conclusion": (
            "The proposed system demonstrates the practical application of "
            "technology and provides scope for future enhancement."
        )
    }
    return jsonify(report)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
