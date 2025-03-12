function delayedOutput(text, waitTime) {
    setTimeout(() => console.log(text), waitTime);
}

delayedOutput("Hello, after 3 seconds!", 3000);