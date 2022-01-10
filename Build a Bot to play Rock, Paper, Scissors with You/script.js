function play() {
    var player = parseInt(document.getElementById("player").value);
    var computer = Math.floor(Math.random() * 3);

    document.getElementById("computer").value = computer;

    if (player == computer) {
        document.getElementById("result").innerHTML = "It's a tie!";
    } else if ((player == 0 && computer == 1) || 
    (player == 1 && computer == 2) || 
    (player == 2 && computer == 0)) {
        document.getElementById("result").innerHTML = "You lose!";
    } else if ((player == 0 && computer == 2) || 
    (player == 1 && computer == 0) || 
    (player == 2 && computer == 1)) {
        document.getElementById("result").innerHTML = "You win!";
    }
}

function clearResult() {
    document.getElementById("result").innerHTML = "&nbsp;";
}