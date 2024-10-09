function setupCampaignPage() {
    let title = document.getElementById("campaign_title");
    title.innerHTML = "<h1>"+campaign.name+"</h1>"

    let gm = document.getElementById("campaign_gameMaster");
    gm.innerHTML = "<h2><b>Game Master:</b> <br>"+user.username+"</h2>"

    let players = document.getElementById("campaign_players");
    players.innerHTML = "<h2><b>Players:</b></h2>";

    getPlayers()
}

async function getPlayers() {
    fetch(environment+"/retrievePlayerList", {
        method: "POST",
        body: JSON.stringify({
            id: campaign.id
        }),
        headers: {
            "Content-type": "application/json",
            "ngrok-skip-browser-warning": "69420"
        }
    })
        .then((response) => response.json())
        .then((json) => console.log(json));
}

setupCampaignPage();