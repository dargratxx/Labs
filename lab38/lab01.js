function parseData(jsonInput) {
    try {
        let parsedObj = JSON.parse(jsonInput);
        console.log(parsedObj);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseData('{"name": "Alice"}');
parseData("invalid json");