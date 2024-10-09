var campaign;

function get_campaign() {
    campaign = JSON.parse(sessionStorage.getItem("campaign"));
    console.log(campaign);
}

try {
    get_campaign();
}catch(err) {
    window.location.replace("/client/gameMaster_client/index.html");
}