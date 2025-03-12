function fetchInfo() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Data received"), 2000);
    });
}

fetchInfo().then(result => console.log(result)).finally(() => console.log("Request completed"));