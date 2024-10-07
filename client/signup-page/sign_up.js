function signup_button() {
    let data = gatherData();
    console.log(data);

    postUser(data);
}

function gatherData() {
    let values = {
        fname: document.getElementById("fname").value,
        lname: document.getElementById("lname").value,
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        email: document.getElementById("email").value
    };

    return values;
}

function postUser(val) {
    fetch("http://"+environment+"/registerUser", {
        method: "POST",
        body: JSON.stringify(val),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then((response) => response.json())
        .then((json) => console.log(json));
}