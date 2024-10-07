function signup_button() {
    let data = gatherData();
    console.log(data);

    postUser(data);

    window.location.replace("/client/player_client/login-page/index.html");
}

function gatherData() {
    let values = {
        fname: document.getElementById("fname").value,
        lname: document.getElementById("lname").value,
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        email: document.getElementById("email").value,
        userType: 'player'
    };

    return values;
}

function optionsStart() {
  fetch(environment+"registerPlayerUser", {
    method: "OPTIONS"
  })
}

function postUser(val) {
  optionsStart();
    fetch(environment+"/registerPlayerUser", {
        method: "POST",
        body: JSON.stringify(val),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          "ngrok-skip-browser-warning": "69420"
      }
      })
        .then((response) => response.json())
        .then((json) => console.log(json));
}