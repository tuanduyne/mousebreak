from flask import Flask, render_template, jsonify
import random
import time
import os

app = Flask(__name__)

ROWS = 3
COLS = 3
GAME_TIME = 30  # giây

score = 0
mole_pos = (-1, -1)
end_time = 0
last_mole_time = 0

@app.route("/")
def index():
    return render_template("index.html")  # link tới index.html trong folder templates

@app.route("/start")
def start():
    global score, end_time, last_mole_time
    score = 0
    end_time = time.time() + GAME_TIME
    last_mole_time = 0
    return jsonify({"status": "started"})

@app.route("/state")
def state():
    global mole_pos, last_mole_time

    if time.time() > end_time:
        return jsonify({"game_over": True, "score": score})

    # Mole nhảy mỗi 1 giây
    if time.time() - last_mole_time >= 1:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        mole_pos = (r, c)
        last_mole_time = time.time()

    return jsonify({
        "game_over": False,
        "row": mole_pos[0],
        "col": mole_pos[1],
        "score": score,
        "time": int(end_time - time.time())
    })

@app.route("/hit/<int:r>/<int:c>")
def hit(r, c):
    global score
    if (r, c) == mole_pos:
        score += 1
        return jsonify({"hit": True, "score": score})
    return jsonify({"hit": False, "score": score})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
