from flask import Flask, request, render_template, jsonify
import asyncio

app = Flask(__name__)

db = []


# @app.route("/", methods=["GET"])
# def index():
#     all_routes = []
#     for item in app.url_map.iter_rules():
#         all_routes.append(item.rule)

#     return all_routes


@app.route("/input", methods=["POST"])
async def input():
    if request.method == "POST":
        data = request.get_json()
        db.append(data['item'])
        # print(request.content_type)
        return jsonify(), 200
    
    # return render_template("input.html")

async def input_task():
    tasks = []
    for i in range(50):
        task = asyncio.create_task(input())
        tasks.append(task)
    for t in tasks:
        await t

@app.route("/summarize", methods=["GET"])
def summarize():
    global db
    result = sum(db)
    db = []
    return jsonify({"sum": result})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    asyncio.run(input_task())