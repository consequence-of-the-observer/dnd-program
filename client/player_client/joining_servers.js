var environment

function join_server(host_name) {
    console.log(host_name);

    let data = JSON.parse(localStorage.getItem("server_"+host_name));

    console.log(data.serverAddress);

    environment = data.serverRequestType + data.serverAddress;

    connecting_client();
}

async function connecting_client() {
        fetch(environment,{
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "ngrok-skip-browser-warning": "69420"
            }
            })
        .then(response => {
            if(!response.ok) {
                throw new Error('Network response was no ok');
            }
            return response.json()
        })
        .then(data => {
            console.log(data);
            sessionStorage.setItem("environment", environment);
            window.location.replace("/client/player_client/signup-page/index.html");
        })     
        .catch(error => {
            console.error('There was a problem with the fetch operation: ', error);
        })
}
