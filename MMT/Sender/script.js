document.getElementById("forwardButton").addEventListener("click", function() {
    sendCommand("forward");
});

document.getElementById("backwardButton").addEventListener("click", function() {
    sendCommand("backward");
});

document.getElementById("stopButton").addEventListener("click", function() {
    sendCommand("stop");
});

function sendCommand(command) {
    fetch(`/command?cmd=${command}`, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify({ command: command })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}
