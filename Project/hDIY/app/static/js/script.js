//landing page
function passwordToggle() {
    var toggleInput = document.querySelector(".password-field");
    var toggleDisplay = document.querySelector("#password-toggle");

    if (toggleInput.type === "password") {
        toggleInput.type = "text";
    } else {
        toggleInput.type = "password";
    }

    if (toggleDisplay.innerText === "(show)") {
        toggleDisplay.innerText = "(hide)";
    } else {
        toggleDisplay.innerText = "(show)";
    }
}


function registerForm() {
    let signInDiv = document.querySelector("#login-form")
    let registerDiv = document.querySelector("#register-form")
    let navSignBtn = document.querySelector("#nav-sign-btn")

    // console.log(registerDiv)
    // console.log(registerDiv.className === "hidden")
    if (registerDiv.className === "hidden") {
        registerDiv.className = "show"
        signInDiv.className = "hidden"
    } else {
        registerDiv.className = "hidden"
        signInDiv.className = "show"
    }
    if (navSignBtn.innerText === "Sign Up") {
        navSignBtn.innerText = "Sign In"
    } else {
        navSignBtn.innerText = "Sign Up"
    }
}