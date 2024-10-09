var add_campaign = false;

function addCampaign() {
    add_campaign = true;
    addNewCampaign();
}

function addNewCampaign() {
    if(add_campaign === true) {
        let data = document.getElementById("new_campaign");

        data.innerHTML = `
            <h3>Create New Campaign</h3>
            <b>Campaign Name:</b><input id="campaign_name">
            <br>
            <b>Campaign Code:</b><input id="campaign_code">
            <br>
            <button onClick="campaignData()">Join</button>
        `;
    }
}

function campaignData() {
    
    let data = {
        name: document.getElementById("campaign_name").value,
        code: document.getElementById("campaign_code").value,
        playerId: user.uuid
    };

    console.log(data);
    postCampaign(data);
}

function postCampaign(data) {
    fetch(environment+"/joinCampaign", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          "ngrok-skip-browser-warning": "69420"
      }
      })
        .then((response) => response.json())
        .then((json) => console.log(json));
}