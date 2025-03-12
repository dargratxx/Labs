let values = [1, 2, 3, 4, 5, 6, 7];

for (let index = 0; index < values.length; index++) {
    if (values[index] === 5) {
        continue;
    }
    console.log(values[index]);
}