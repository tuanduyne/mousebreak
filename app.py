from flask import Flask, render_template, jsonify
import random
import time
import os

app = Flask(__name__)

SO_HANG = 3
SO_COT = 3
THOI_GIAN_CHOI = 30
TOC_DO_CHUOT = 1500

diem = 0
end_time = time.time() + THOI_GIAN_CHOI
vi_tri_chuot = (-1, -1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/state")
def state():
    global vi_tri_chuot

    if time.time() > end_time:
        return jsonify({"game_over": True, "score": diem})

    hang = random.randint(0, SO_HANG - 1)
    cot = random.randint(0, SO_COT - 1)
    vi_tri_chuot = (hang, cot)

    return jsonify({
        "row": hang,
        "col": cot,
        "score": diem,
        "time": int(end_time - time.time())
    })

@app.route("/hit/<int:r>/<int:c>")
def hit(r, c):
    global diem
    if (r, c) == vi_tri_chuot:
        diem += 1
        return jsonify({"hit": True, "score": diem})
    return jsonify({"hit": False})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
