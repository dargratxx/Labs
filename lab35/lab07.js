let values = [3, 7, 12, 5, 9];

for (let index = 0; index < values.length; index++) {
    if (values[index] === 12) {
        console.log("Number 12 found, stopping the loop.");
        break;
    }
    console.log(values[index]);
}