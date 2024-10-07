var environment

function get_environment() {
    environment = sessionStorage.getItem("environment");
    console.log(environment);
}

try {
    get_environment();
}catch(err) {
    window.location.replace("player_client/client/index.html");
}