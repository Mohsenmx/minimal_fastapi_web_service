from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

db = []


@app.route("/", methods=["GET"])
def index():
    all_routes = []
    for item in app.url_map.iter_rules():
        all_routes.append(item.rule)

    return all_routes


@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        data = request.get_json()
        db.append(data['item'])
        return jsonify({"message": "json received"})
    
    return render_template("input.html")

@app.route("/summarize", methods=["GET"])
def summarize():
    global db
    result = sum(db)
    db = []
    return jsonify({"sum": result})

if __name__ == '__main__':
    app.run(debug=True, port=8080)