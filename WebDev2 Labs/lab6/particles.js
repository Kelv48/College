let canvas;
let context;
let fpsInterval = 1000 / 30;
let now;
let then = Date.now();

let x = 250;
let y = 150;
let size = 10;
let xChange = randint(1, 10);
let yChange = randint(1, 10);

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    

   draw();
}

function draw() {
    window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "yellow"
    context.fillRect(x, y, size, size);
    x = x + xChange;
    y = y + yChange;
    
    if (x > 512 && y > 0) {
        x = -x - xChange;
        y = y - yChange; 
    
    }
    }
    


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}


