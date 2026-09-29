async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user-message";
    userMessage.textContent = message;

    chatBox.appendChild(userMessage);

    input.value = "";

    // Show typing indicator
    const typingMessage = document.createElement("div");
    typingMessage.className = "message bot-message";
    typingMessage.textContent = "Typing...";

    chatBox.appendChild(typingMessage);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        // Send message to Flask
        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Remove typing indicator
        typingMessage.remove();

        // Display bot response
        const botMessage = document.createElement("div");

        botMessage.className = "message bot-message";
        botMessage.textContent = data.response;

        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        typingMessage.remove();

        const errorMessage = document.createElement("div");

        errorMessage.className = "message bot-message";
        errorMessage.textContent =
            "Sorry, something went wrong. Please try again.";

        chatBox.appendChild(errorMessage);
    }
}


// Press Enter to send message
document.getElementById("user-input").addEventListener(
    "keypress",
    function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    }
);