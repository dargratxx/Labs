function divideNumbers(num1, num2) {
    try {
        if (num2 === 0) {
            throw new Error("Division by zero");
        }
        return num1 / num2;
    } catch (error) {
        console.error("Cannot divide by zero");
    }
}

divideNumbers(10, 2);
divideNumbers(10, 0);