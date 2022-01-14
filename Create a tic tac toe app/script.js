var grid = document.getElementById('grid');
var table = Array(3).fill().map(() => Array(3).fill(0));
var turn = document.getElementById('player');

var player = 1;
var end = false;

function check() {
    // checking horizontally and vertically
    for (let i = 0; i < 3; ++i) {
        if (table[i][0] !== 0 && table[i][0] === table[i][1] && table[i][0] === table[i][2]) {
            return table[i][0];
        }
        if (table[0][i] !== 0 && table[0][i] === table[1][i] && table[0][i] === table[2][i]) {
            return table[0][i];
        }
    }

    // checking diagonals
    if (table[0][0] !== 0 && table[0][0] == table[1][1] && table[0][0] == table[2][2]) {
        return table[0][0];
    }
    if (table[2][0] !== 0 && table[2][0] == table[1][1] && table[2][0] == table[0][2]) {
        return table[2][0];
    }

    // checking is move available
    for (let i = 0; i < 3; ++i) {
        for (let j = 0; j < 3; ++j) {
            if (table[i][j] === 0) {
                return false;
            }
        }
    }

    return 'Tie';
}

function play(i, j) {
    if (table[i][j] !== 0 || end) {
        return;
    }

    grid.children[0].children[i].children[j].innerHTML = player === 1 ? 'X' : 'O';
    grid.children[0].children[i].children[j].style.color = player === 1 ? 'red' : 'blue';
    table[i][j] = player;

    var result = check();
    if (result) {
        end = true;
        turn.style.color = 'black';
        document.getElementById('reload').innerHTML = '<button onclick="window.location.reload();">Reset</button>';

        if (result === 'Tie') {
            document.getElementById('result').innerHTML = 'Game Draw';
            return;
        }

        turn.innerHTML = result === 1 ? '<span style="color: red">X</span> wins' : '<span style="color: blue">O</span> wins';
        return;
    }

    player = player == 1 ? 2 : 1;
    turn.innerHTML = player === 1 ? 'X' : 'O';
    turn.style.color = player === 1 ? 'red' : 'blue';
}