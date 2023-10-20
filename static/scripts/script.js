let events = [];
let sessionKey = "";
let time = 0;


function main() {
    const setupResponse = setup();
    sessionKey = setupResponse.sessionkey;
    addEventListeners(setupResponse.listeners);
    console.log(setupResponse);
    eventLoop();
    //window.requestAnimationFrame(eventLoop);
}

function advance() {
    const path = "/event/" + sessionKey;
    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure the POST request
    xhr.open('POST', path, false); // Set the third parameter to true for asynchronous

    // Set the content type header
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    // Data to be sent in the POST request (replace with your own data)
    var postData = JSON.stringify({
        events: events,
        time: time
    });

    // Send the POST request (blocking)
    xhr.send(postData);
    time++;

    events = [];

    // Check the response status
    if (xhr.status === 200) {
        // Request was successful
        var responseText = xhr.responseText;
        draw(JSON.parse(responseText));
        return responseText;
    } else {
        // Request failed
        console.error('POST Request failed with status:', xhr.status);
        return responseText
    }
}



function eventLoop() {
    console.log(advance());
    window.requestAnimationFrame(eventLoop);
    //setTimeout(eventLoop, 1000);
}

function getOrientation() {
    if (window.matchMedia("(orientation: portrait)").matches) {
        return "PORTRAIT"
    } else if (window.matchMedia("(orientation: landscape)").matches) {
        return "LANDSCAPE"
    }

    return "UNKNOWN"
}

function addEventListeners(listeners) {
    // Event Listeners for Mouse Events (Canvas with id "canvas")
    const canvas = document.getElementById('myCanvas');

    if (listeners.includes("click")) {
        canvas.addEventListener('click', (event) => {
            const canvas = document.getElementById("myCanvas");
            events.push({
                type: event.type,
                x:  event.clientX - canvas.getBoundingClientRect().left,
                y: event.clientY - canvas.getBoundingClientRect().top,
                ctrlKey: event.ctrlKey,
                altKey: event.altKey,
                metaKey: event.metaKey
            });
        });
    }
    // 1. click
    
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

/**
 * Creates a connection to the CanvasStream server.
 */
function setup() {
    const path = "/setup/";
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
        return JSON.parse(responseText);
    } else {
        // Request failed
        console.error('POST Request failed with status:', xhr.status);
        return responseText;
    }
}

function getContext() {
    const ctx = document.getElementById("myCanvas").getContext("2d");
    ctx.imageCache = {};

    // ctx.drawImg = function(imagePath, dx, dy, dWidth = null, dHeight = null) {

    //     if (!(imagePath in imageCache)) {
    //         const newImage = new Image();
    //         newImage.src = "/assets/" + imagePath;
    //         this.imageCache[imagePath] = newImage;
    //     }
        
    //     let args = [this.imageCache[imagePath], dx, dy];
    //     if (dWidth != null && dHeight != null) {
    //         args.push(dWidth);
    //         args.push(dHeight);
    //     }
    
    //     // Call the original drawImage method
    //     ctx.drawImage.apply(ctx, args);
    // };
}

function draw(drawCommands) {
    const ctx = document.getElementById("myCanvas").getContext("2d");
    for (const message of drawCommands) {
        console.log(message);
        const type = message.type;
        const name = message.name;
        const parameters = message.parameters;

        if (type == "func") {
            ctx[name].apply(ctx, parameters);
        } else if (type == "var") {
            ctx[name] = parameters[0];
        } else if (type == "command") {

        }
    }
}

main();