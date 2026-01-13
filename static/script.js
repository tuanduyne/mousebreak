let gameInterval;

function startGame() {
    fetch("/start")
    .then(res => res.json())
    .then(() => {
        gameInterval = setInterval(updateState, 1000); // mỗi 1 giây
    });
}

function updateState() {
    fetch("/state")
    .then(res => res.json())
    .then(data => {
        if (data.game_over) {
            clearInterval(gameInterval);
            alert("Game over! Điểm của bạn: " + data.score);
        } else {
            // Xóa mole cũ
            document.querySelectorAll(".cell").forEach(cell => cell.classList.remove("mole"));
            // Thêm mole mới với animation
            let cell = document.querySelector(`#cell-${data.row}-${data.col}`);
            cell.classList.add("mole");

            // Cập nhật điểm và thời gian
            document.getElementById("score").innerText = data.score;
            document.getElementById("time").innerText = data.time;
        }
    });
}

function hit(r, c) {
    fetch(`/hit/${r}/${c}`)
    .then(res => res.json())
    .then(data => {
        document.getElementById("score").innerText = data.score;
    });
}
