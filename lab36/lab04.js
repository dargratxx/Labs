function makeCounter() {
    let tally = 0;
    return function() {
        tally++;
        return tally;
    };
}

const firstCounter = makeCounter();
const secondCounter = makeCounter();

firstCounter();
firstCounter();
secondCounter();