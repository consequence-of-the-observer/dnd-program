var campaign_data = [];

async function getCampaignList() {
    fetch(environment+"/gameMasterCampaignList", {
        method: "POST",
        body: JSON.stringify({
            id: user.uuid
        }),
        headers: {
            "Content-type": "application/json",
            "ngrok-skip-browser-warning": "69420"
        }
    })
        .then((response) => response.json())
        .then((json) => generateCampaignDivs(json));
}

getCampaignList();

function generateCampaignDivs(data) {
    console.log(data);
    campaign_data = data;

    let content = document.getElementById("campaign_list");
    let content_data = [];

    for(let i = 0; i < data.length; i++) {
        let sec_data = `
            <div onClick="campaign_save(`+i+`)">
                <h3>`+data[i].name+`</h3>
            </div>
        `;

        content_data.push(sec_data);
    }

    content.innerHTML = "<h2>Campaign List</h2>";

    for(let i = 0; i < content_data.length; i++) {
        content.innerHTML += content_data[i];
    }
}

function campaign_save(i) {
    sessionStorage.setItem("campaign", JSON.stringify(campaign_data[i]));
    window.location.replace("/client/gameMaster_client/home-page/campaign_page/index.html");
}