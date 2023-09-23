// script1.js

// Find elements
const nextButton = document.getElementById("next-button");
const questionContainers = document.querySelectorAll(".question-container");
const questionIdInput = document.getElementById("question-id");

let currentQuestionIndex = 0;

// Function to show the current question and hide others
function showCurrentQuestion() {
    questionContainers.forEach((container, index) => {
        if (index === currentQuestionIndex) {
            container.style.display = "block";
        } else {
            container.style.display = "none";
        }
    });
    questionIdInput.value = questionContainers[currentQuestionIndex]
        .querySelector(".question")
        .dataset.questionId;
    nextButton.disabled = true;
}

// Event listener for the Next button
nextButton.addEventListener("click", function () {
    currentQuestionIndex++;
    if (currentQuestionIndex < questionContainers.length) {
        showCurrentQuestion();
    } else {
        // Submit the form when all questions are answered
        document.querySelector("form").submit();
    }
});

// Event listener to enable the Next button when an option is selected
const options = document.querySelectorAll("input[type='radio']");
options.forEach((option) => {
    option.addEventListener("change", function () {
        nextButton.disabled = false;
    });
});

// Initially, show the first question
showCurrentQuestion();
