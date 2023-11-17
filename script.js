// CHARACTER COUNTER

document.getElementById('reddit-post').addEventListener('input', function () {
    var currentLength = this.value.length;
    var maxLength = 5000;
    var counterElement = document.getElementsByClassName('counter-char')[0];
    counterElement.textContent = currentLength + '/' + maxLength;
});

// CLEAR BUTTON
document.addEventListener("DOMContentLoaded", function () {
    var clearButton = document.getElementById("clear-btn");

    clearButton.addEventListener("click", function () {
        var textarea = document.getElementById("reddit-post");

        textarea.value = '';

        var counter = document.querySelector(".counter-char");
        counter.textContent = '0/5000';
    });
});
