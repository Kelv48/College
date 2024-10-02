let canvas;
let context;
let fpsInterval = 1000 / 30;
let now;
let then = Date.now();

let particles = [];

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

    for (let i=0; i < 30; i+= 1) {
    let p = {   
            x : 250,
            y : 150,
            size : 10,
            xChange : randint(-10, 10),
            yChange : randint(-10, 10) 
            }
    }
}

function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}