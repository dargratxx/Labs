function startCount() {
    let countValue = 1;
    let intervalId = setInterval(() => {
        console.log("Counter: " + countValue);
        if (countValue === 5) {
            clearInterval(intervalId);
        }
        countValue++;
    }, 1000);
}

startCount();