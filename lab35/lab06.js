let inputValue;

do {
    inputValue = parseInt(prompt("Enter a number greater than 10: "), 10);
} while (inputValue <= 10);

console.log("Valid input received:", inputValue);