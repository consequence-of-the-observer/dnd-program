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
    fetch("http://"+environment+"/confirmUser", {
        method: "POST",
        body: JSON.stringify(val),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then((response) => response.json())
        .then((json) => console.log(json));
}