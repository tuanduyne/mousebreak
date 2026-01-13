const grid = document.getElementById("grid");
const scoreEl = document.getElementById("score");
const timeEl = document.getElementById("time");

for (let i = 0; i < 9; i++) {
  const cell = document.createElement("div");
  cell.className = "cell";
  cell.onclick = () => hit(Math.floor(i / 3), i % 3);
  grid.appendChild(cell);
}

function renderMouse(r, c) {
  document.querySelectorAll(".cell").forEach(e => e.textContent = "");
  grid.children[r * 3 + c].textContent = "🐭";
}

function hit(r, c) {
  fetch(`/hit/${r}/${c}`)
    .then(res => res.json())
    .then(data => {
      if (data.hit) scoreEl.textContent = "Điểm: " + data.score;
    });
}

function update() {
  fetch("/state")
    .then(res => res.json())
    .then(data => {
      if (data.game_over) {
        alert("Hết giờ! Điểm: " + data.score);
        return;
      }
      scoreEl.textContent = "Điểm: " + data.score;
      timeEl.textContent = "Thời gian: " + data.time + "s";
      renderMouse(data.row, data.col);
    });
}

setInterval(update, 1500);
