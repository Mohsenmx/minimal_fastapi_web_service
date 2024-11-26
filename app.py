from flask import Flask, request, render_template, jsonify
import asyncio

app = Flask(__name__)

db = []


async def async_input():
    if request.method == "POST":
        data = request.get_json()
        db.append(data['item'])    
        
@app.route("/input", methods=["POST"])
async def input():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(async_input())
        tasks.append(task)
    await asyncio.gather(*tasks)
    return jsonify(), 200

@app.route("/summarize", methods=["GET"])
def summarize():
    global db
    result = sum(db)
    db = []
    return jsonify({"sum": result})

if __name__ == '__main__':
    app.run(debug=True, port=8080)

    