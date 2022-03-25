function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySector(".form__message");

    messageElement.textContext = message;
    messageElement.classlist.remove("form__message--success", "form__message--error");
    messageElement.classlist.add('form__message--${type}');

}

function setInputError(inputElement,message){
    inputElement.classList.add("form__message--error");
    inputElement.parentElement.querySelector(".form__input--error-message").textContent = message;
}

function clearInputError(inputElement){
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent =""
}

document.addEventListener("DOMContentloaded",() => {
    const loginForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        CreateAccountForm.classList.remove("form--hidden");       
    });

    document.querySelector("#linklogin").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("form--hidden");
        CreateAccountForm.classList.add("form--hidden");       
    });

    loginForm.addEventListener("submit", e => {
        e.preventDefault();

        // Perform your AJAX/Fetch login

        setFormMessage(loginForm, "error", "Invalid username/password combination");

    });

    document.querySelectorAll(".form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", e=> {
            if (e.target.id == "signupUsername" && e.target.value.length > 0 && e.target.value.length < 10){
                setInputError(inputElement,"Username must be at least 10 characters in length");
            }

        });

        inputElement.addEventListener("input", e => {
           clearInputError(inputElement); 
        });
    });
}); 
