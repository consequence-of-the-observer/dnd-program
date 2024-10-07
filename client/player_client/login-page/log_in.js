function login_button() {
    let data = gatherData();
    console.log(data);

    postConfirmUser(data);
}

function gatherData() {
    let values = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    return values;
}

function postConfirmUser(val) {
    fetch("http://"+environment+"/confirmPlayerUser", {
        method: "POST",
        body: JSON.stringify(val),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          "ngrok-skip-browser-warning": "69420"
      }
      })
        .then((response) => response.json())
        .then((json) => confirmRealAccount(json));
}

function confirmRealAccount(data) {
  console.log(data);
  if(data.real_account === false) {
    console.log("account does not exists");
  }else {
    console.log("account exists");
    window.location.replace("/client/player_client/home-page/index.html");
  }
}