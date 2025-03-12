let numberList = [1, 2, 3, 4, 5, 6];
let totalEven = 0;

for (let i = 0; i < numberList.length; i++) {
    console.log(numberList[i]);
    if (numberList[i] % 2 === 0) {
        totalEven += numberList[i];
    }
}

console.log(totalEven);