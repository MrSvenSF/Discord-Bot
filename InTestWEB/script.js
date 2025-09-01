document.addEventListener("DOMContentLoaded", function() {
    const sendButton = document.getElementById("send-button");
    const userInput = document.getElementById("user-input");
    const messagesContainer = document.getElementById("messages");

    sendButton.addEventListener("click", function() {
        const userMessage = userInput.value;
        if (userMessage.trim() !== "") {
            const messageElement = document.createElement("div");
            messageElement.classList.add("user-message");
            messageElement.textContent = userMessage;
            messagesContainer.appendChild(messageElement);
            userInput.value = "";
        }
    });
});
