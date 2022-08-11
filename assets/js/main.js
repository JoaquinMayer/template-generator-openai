var form = document.getElementById("form");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    let phrase = document.getElementById("phrase").value;
    fetch('/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: phrase,
        })
    })
        .then(response => response.json())
        .then(data => {
            const element = document.createElement('div')
            if (data.error) {
                element.innerHTML = data.message
            } else {
                element.innerHTML = JSON.stringify(data.data)
            }
            document.body.appendChild(element)
        })
  });