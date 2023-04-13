var TYPE = null
async function get_token() {
    const options = { method: 'GET', };
    let teste = await fetch('http://127.0.0.1:8000/get-token/', options)
    const token = await teste.json();
    return token["token"]
}

var testando = (async () => {
    const data = await get_token();
    let token = await data;
    const connTeste = new WebSocket("ws://localhost:8765")
    connTeste.onopen = (event) => connTeste.send(JSON.stringify({ "token": token }));
    connTeste.onmessage = function (event) {
        if (JSON.parse(event.data)["message"] != "" && JSON.parse(event.data)["message"] != null) {
            // console.log(event.data, TYPE)

            let messages = document.getElementById(`messages-${TYPE}`)
            messages.insertAdjacentHTML('beforeend', `<div>
                                            <p>${JSON.parse(event.data)["message"]}</p>
                                        </div>`)
        }
    }
})();




window.onload = function () {
    fetch("recover/", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then((response) => response.json())
        .then(function (data) {
            data.forEach(function (item) {

                let messages = document.getElementById(`messages-${item.chat_id}`)

                messages.insertAdjacentHTML('beforeend', `<div>
                        <p>${item.message}</p>
                        </div>`)
            })
        })
}

function addMsg(message, id) {
    fetch("send/", {
        method: 'POST',
        body: JSON.stringify({
            "message": message,
            "chat_id": id,
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

function send_dinos() {
    let formDinos = document.getElementById('chat-dinos')
    formDinos.addEventListener('submit', (e) => {
        e.preventDefault()
        let message = e.target.message.value
        formDinos.reset()
        TYPE = 'dinos'
        addMsg(message, 'dinos')
    })
}

function send_aves() {
    let formAves = document.getElementById('chat-aves-raras')
    formAves.addEventListener('submit', (e) => {
        e.preventDefault()
        let message = e.target.message.value
        formAves.reset()
        TYPE = 'aves-raras'
        addMsg(message, 'aves-raras')
    })
}