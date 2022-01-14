var grid = document.getElementById('grid');
var play = Array(7).fill(0).map(() => Array(6).fill(0));
var head = document.getElementById('head');

var player = 1;

function check() {
    var count = 0, curr = 0;

    // checking vertically
    for (let i = 0; i < 7; i++) {
        for (let j = 0 ; j < 6; j++) {
            if (curr === play[i][j] && curr !== 0) {
                count++;
            } else {
                curr = play[i][j];
                count = 1;
            }

            if (count === 4) {
                return true;
            }

            // checking diagonally (main diagonal)
            if (i < 4 && j < 3) {
                if (play[i][j] !== 0 && 
                play[i][j] === play[i + 1][j + 1] &&
                play[i][j] === play[i + 2][j + 2] &&
                play[i][j] === play[i + 3][j + 3]) {
                    return true;
                }
            }

            // checking diagonally (secondary diagonal)
            if (i > 2 && j < 3) {
                if (play[i][j] !== 0 &&
                play[i][j] === play[i - 1][j + 1] &&
                play[i][j] === play[i - 2][j + 2] &&
                play[i][j] === play[i - 3][j + 3]) {
                    return true;
                }
            }
        }
    }

    count = 0;
    curr = 0;

    // checking horizontally
    for (let j = 0; j < 6; j++) {
        for (let i = 0; i < 7; i++) {
            if (curr === play[i][j] && curr !== 0) {
                count++;
            } else {
                curr = play[i][j];
                count = 1;
            }
            
            if (count === 4) {
                return true;
            }
        }
    }
}

function fill(n) {
    for (let i = 5; i >= 0; --i) {
        if (play[n - 1][i] == 0) {
            play[n - 1][i] = player;
            grid.children[0].children[i + 1].children[n - 1].style.backgroundColor = player == 1 ? 'red' : 'yellow';

            if (i == 0) {
                grid.children[0].children[i].children[n - 1].innerHTML = '';
            }
            break;
        }
    }
    
    if (check()) {
        head.innerHTML = "Player " + player + " wins!";
        for (let i = 0; i < 7; ++i) {
            grid.children[0].children[0].children[i].innerHTML = '';
        }
        return;
    }

    player = player == 1 ? 2 : 1;
    head.innerHTML = player == 1 ? "Player 1" : "Player 2";
}