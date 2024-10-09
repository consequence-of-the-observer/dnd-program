var user;

function get_user() {
    user = JSON.parse(sessionStorage.getItem("user"));
    console.log(user);
}

try {
    get_user();
}catch(err) {
    window.location.replace("/client/gameMaster_client/index.html");
}