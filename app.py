from flask import Flask, request, jsonify
from mcp_agent import handle_mcp_action

app = Flask(__name__)

@app.route("/mcp/action", methods=["POST"])
def handle_action():
    data = request.json
    action = data.get("action")
    params = data.get("params", {})
    try:
        result = handle_mcp_action(action, params)
        return jsonify({ "result": result })
    except Exception as e:
        return jsonify({ "error": str(e) }), 500

if __name__ == "__main__":
    app.run(port=4000)
