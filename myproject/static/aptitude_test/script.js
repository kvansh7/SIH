// script.js

// Find the "Start Test" button by its id
const startButton = document.getElementById("start-button");

// Add a click event listener to the button
startButton.addEventListener("click", function() {
    // Redirect to the quiz page URL
    window.location.href = "/quiz/";
});
