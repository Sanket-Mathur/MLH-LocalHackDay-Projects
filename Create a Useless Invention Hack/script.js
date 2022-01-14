var text = document.getElementById('text');

var choice = [
    'No.',
    'Why did you touch me?',
    'Stop touching me.',
    'I\'m not touching you.',
    'What the hell?',
    'You little kiddo. Stop it.',
    'You wanna fight, huh?',
    'You\'re not my mother.',
    'You\'re not my father.',
    'Get the hell off of me.',
    'Go play somewhere else.',
    'I\'m not your friend.',
    'GO AWAY!!',
    'What do you want?',
    'Go away or I\'m calling the cops.'
];
var count = 0;
var end = false;

function touch() {
    if (end) {
        return;
    }

    count++;
    if (count >= 10) {
        text.innerHTML = 'Fine. I\'ll take to you MLH\'s LocalHackDay.';

        var time = 5;
        setInterval(() => {
            text.innerHTML = 'Fine. I\'ll take to you MLH\'s LocalHackDay. In ' + (time);
            time--;
        }, 1000);

        setTimeout(() => {
            window.location.replace('https://localhackday.mlh.io/build');
        }, 5000);

        end = true;
        return;
    }

    text.innerHTML = choice[Math.floor(Math.random() * choice.length)];
}