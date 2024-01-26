async function sendText() {
    const inputText = document.getElementById('inputText').value;
    const response = await fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: inputText})
    });
    const data = await response.json();
    const resultElement = document.getElementById('result');
    resultElement.innerText = data.result;

    const keysElement = document.getElementById('keys');
    keysElement.innerHTML = '';
    for (const key in data.keys) {
        const keyElement = document.createElement('span');
        keyElement.innerText = key;
        keyElement.classList.add('key');
        keyElement.addEventListener('mouseover', () => highlightText(data.keys[key]));
        keyElement.addEventListener('mouseout', () => removeHighlights());
        keysElement.appendChild(keyElement);
    }
}

function highlightText(indices) {
    const resultElement = document.getElementById('result');
    let resultText = resultElement.innerText;
    for (const [start, end] of indices) {
        resultText = resultText.slice(0, start) + '<span class="highlight">' + resultText.slice(start, end) + '</span>' + resultText.slice(end);
    }
    resultElement.innerHTML = resultText;
}

function removeHighlights() {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = resultElement.innerText;  // removes all HTML tags
}
