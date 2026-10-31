document.addEventListener("DOMContentLoaded", function () {

    // Login form validation
    const loginForm = document.getElementById("loginForm");

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();

            alert("Login form submitted successfully!");
        });
    }

    // Registration form validation
    const registerForm = document.getElementById("registerForm");

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();

            alert("Registration form submitted successfully!");
        });
    }

});