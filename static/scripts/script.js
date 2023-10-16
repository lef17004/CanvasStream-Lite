function main() {
    const sessionKey = getSessionKey();
    console.log("Session Key: ", sessionKey)
    const configJSON = getSetupJSON(sessionKey);
    addEventListeners();
}

function getSessionKey() {
    const path = "/connect";
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url + path, false);
    xhr.send();

    if (xhr.status === 200) {
        var responseText = xhr.responseText;
        const json = JSON.parse(responseText);
        return json.sessionKey;
    } else {
        // Request failed
        console.error('GET Request failed with status:', xhr.status);
        return "";
    }
}

function getSetupJSON(sessionKey) {
    const path = "/setup/" + sessionKey;
    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure the POST request
    xhr.open('POST', path, false); // Set the third parameter to true for asynchronous

    // Set the content type header
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Data to be sent in the POST request (replace with your own data)
    var postData = JSON.stringify({
        width: window.innerWidth,
        height: window.innerHeight,
        orientation: getOrientation()
    });

    // Send the POST request (blocking)
    xhr.send(postData);

    // Check the response status
    if (xhr.status === 200) {
        // Request was successful
        var responseText = xhr.responseText;
        console.log('POST Response:', responseText);
        return responseText;
    } else {
        // Request failed
        console.error('POST Request failed with status:', xhr.status);
        return responseText
    }
}

function getOrientation() {
    if (window.matchMedia("(orientation: portrait)").matches) {
        return "PORTRAIT"
    } else if (window.matchMedia("(orientation: landscape)").matches) {
        return "LANDSCAPE"
    }

return "UNKOWN"
}

function addEventListeners() {
    // Event Listeners for Mouse Events (Canvas with id "canvas")
    const canvas = document.getElementById('myCanvas');

    // 1. click
    canvas.addEventListener('click', (event) => {
        console.log(event);
    });
    document.addEventListener('keydown', (event) => {
        console.log(event);
    });
    return;
    // 2. dblclick
    canvas.addEventListener('dblclick', (event) => {
        console.log('Mouse Double-Clicked on Canvas');
    });

    // 3. mousedown
    canvas.addEventListener('mousedown', (event) => {
        console.log('Mouse Button Pressed Down on Canvas');
    });

    // 4. mouseup
    canvas.addEventListener('mouseup', (event) => {
        console.log('Mouse Button Released on Canvas');
    });

    // 7. mousemove (for canvas)
    canvas.addEventListener('mousemove', (event) => {
        console.log('Mouse Moved on Canvas');
    });


    // Event Listeners for Touch Events (Canvas with id "canvas")

    // 21. touchstart (for canvas)
    canvas.addEventListener('touchstart', (event) => {
        console.log('Touch Started on Canvas');
    });

    // 22. touchmove (for canvas)
    canvas.addEventListener('touchmove', (event) => {
        console.log('Touch Moved on Canvas');
    });

    // 23. touchend (for canvas)
    canvas.addEventListener('touchend', (event) => {
        console.log('Touch Ended on Canvas');
    });

    // 24. touchcancel (for canvas)
    canvas.addEventListener('touchcancel', (event) => {
        console.log('Touch Canceled on Canvas');
    });


    // Event Listeners for Document (or appropriate elements)

    // 8. keydown (for document)
    document.addEventListener('keydown', (event) => {
        console.log('Key Down: ' + event.key);
    });

    // 9. keyup (for document)
    document.addEventListener('keyup', (event) => {
        console.log('Key Up: ' + event.key);
    });


    // Event Listeners for Window

    // 15. load (for window)
    window.addEventListener('load', () => {
        console.log('Window Loaded');
    });

    // 16. unload (for window)
    window.addEventListener('unload', () => {
        console.log('Window Unloaded');
    });

    // 17. resize (for window)
    window.addEventListener('resize', () => {
        console.log('Window Resized');
    });

}

main();