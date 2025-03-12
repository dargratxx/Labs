let globalMsg = "Hello from global";

function printGlobal() {
    let globalMsg = "Hello from function scope";
    console.log(globalMsg);
}

printGlobal();
console.log(globalMsg);
console.log(innerMsg);