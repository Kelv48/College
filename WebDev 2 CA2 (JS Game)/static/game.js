let canvas;
let context;

let fpsInterval = 1000 / 40;
let now;
let then = Date.now();

let x = -340;
let y = -240;
let pixelX = 0;
let pixelY = 0;

let player = {
    x: 0,
    y: 0,
    width: 32,
    height: 36,
    frameX: 0,
    frameY: 0,
    xChange: 0,
    yChange: 0,
    hp: 100,
    maxHp: 100,
    atk: 10,
    def: 5,
    exp: 0,
    level: 1,
    inventory: []
};

let enemy = {
    x: 0,
    y: 0,
    width: 32,
    height: 36,
    frameX: 0,
    frameY: 0,
    xChange: 0,
    yChange: 0,
    hp: 100000,
    maxHp: 100,
    atk: 5,
    def: 2,
    level: 1
};


let Music = new Audio("../static/assets/audio/TownTheme.mp3");
let BattleMusic = new Audio("../static/assets/audio/battleThemeA.mp3")

// basic turn based
// get combat working

const collisionsMap = []
for (let i = 0; i < collisions.length; i += 100) {
    collisionsMap.push(collisions.slice(i, 100 + i))
}

let collisionRow = 12;
let collisionCol = 19;

let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;
let moving = false;

let collisionLeft = false;
let collisionRight = false;
let collisionUp = false;
let collisionDown = false;

let playerImage = new Image();
let backgroundImage = new Image();
let battleBackgroundImage = new Image();

let enemyImage = new Image();
let enemies = [];

const battle = {
    initiated: false
}

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    Music.play();


    playerImage.src = "../static/assets/characters/warrior_m.png";
    backgroundImage.src = "../static/assets/caMap.png";
    battleBackgroundImage.src = "../static/assets/battleBackground.png";
    enemyImage.src = "../static/assets/enemies/ghost/ghost-sheet.png";

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);
    load_assets([
        { "var": playerImage, "url": "../static/assets/characters/warrior_m.png" },
        { "var": backgroundImage, "url": "../static/assets/caMap.png" },
        { "var": battleBackgroundImage, "url": "../static/assets/battleBackground.png" },
        { "var": enemyImage, "url": "../static/assets/enemies/ghost/ghost-sheet.png" }
    ], draw);
}

function draw() {
    let overWorld = window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);
    if (enemies.length < 1) {
        let e = {
            x: 0,
            y: 0,
            width: 32,
            height: 36,
            frameX: 0,
            frameY: 0,
            xChange: randint(1, 4),
            yChange: 0
        };
        enemies.push(e);
    }

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(backgroundImage, x, y);


    context.drawImage(playerImage,
        (player.width * player.frameX), (player.height * player.frameY), player.width, player.height,
        (canvas.width / 2 - playerImage.width / 2) + 20, (canvas.height / 2 - playerImage.height / 2) + 20, player.height, player.height);

    for (let e of enemies) {
        if (player_collides(e)) {
            enemies.pop(e)
            console.log("Battle start")
            Music.pause()
            BattleMusic.play()
            battle.initiated = true;
            window.cancelAnimationFrame(overWorld)
            const div = document.querySelector('.transition'); // select the div element
            const duration = 2000; // duration of the animation in milliseconds
            const interval = 10; // time interval between opacity changes in milliseconds
            let start = null; // variable to store the start time of the animation

            function changeOpacityIncrease(timestamp) {
                if (!start) start = timestamp; // set the start time if it is not set already
                const elapsed = timestamp - start; // calculate the time elapsed since the start of the animation
                const progress = elapsed / duration; // calculate the progress of the animation
                const opacity = Math.min(1, progress * 2); // calculate the opacity value between 0 and 1
                div.style.opacity = opacity; // set the opacity of the div
                if (progress < 0.5 || opacity === 1) { // continue the animation until halfway or the opacity reaches 1
                    requestAnimationFrame(changeOpacityIncrease); // request the next frame of the animation
                }
            }
            requestAnimationFrame(changeOpacityIncrease); // start the animation
            animateBattle()

        }
    }

    if (battle.initiated) return

    for (let e of enemies) {
        if (e.x + e.size < 0) {
            e.x = canvas.width;
            e.y = randint(0, canvas.height);
        } else {
            e.x = e.x + e.xChange;
            e.y = e.y + e.yChange;
        }
        if (e.y + e.height > canvas.height) {
            e.y = canvas.height - e.height;
            e.yChange = -e.yChange * 1.001;
        } else if (e.y < 0) {
            e.y = 0;
            e.yChange = -e.yChange * 1.001;
        } else if (e.x < 0) {
            e.x = 0;
            e.xChange = -e.xChange * 1.001;
        } else if (e.x + e.width > canvas.width) {
            e.x = canvas.width - e.width;
            e.xChange = -e.xChange * 1.001;
        }
    }

    for (let e of enemies) {
        context.drawImage(enemyImage,
            e.width * e.frameX, e.height * e.frameY, e.width, player.height,
            e.x, (canvas.height / 2 - playerImage.height / 2) + 20, e.width, e.height);
    }

    // If the player collides to the left this blocks movement to the left as well as up and down to prevent problems with the array
    if (collisionLeft) {
        if (moveLeft) {
            player.frameY = 3;
            moving = false;
        }
        if (moveRight) {
            x = x - 6;
            player.frameY = 1;
            collisionLeft = false;
        }
        if (moveUp) {
            player.frameY = 0;
        }
        if (moveDown) {
            player.frameY = 2
        }
    }
    // If the player collides to the right this blocks movement to the right as well as up and down to prevent problems with the array
    if (collisionRight) {
        if (moveRight) {
            player.frameY = 1;
            moving = false;
        }
        if (moveLeft) {
            x = x + 6;
            player.frameY = 3;
            collisionRight = false;
        }
        if (moveDown) {
            player.frameY = 2;
        }
        if (moveUp) {
            player.frameY = 1
        }
    }
    // If the player collides to the top this blocks movement up as well as left and right to prevent problems with the array
    if (collisionUp) {
        if (moveUp) {
            player.frameY = 0;
            moving = false;
        }
        if (moveLeft) {
            player.frameY = 3;
        }
        if (moveRight) {
            player.frameY = 1;
        }
        if (moveDown) {
            y = y - 6;
            player.frameY = 2;
            collisionRow = collisionRow
            collisionUp = false;
        }
    }
    // If the player collides to the bottom this blocks movement down as well as left and right to prevent problems with the array
    if (collisionDown) {
        if (moveDown) {
            player.frameY = 2;
            moving = false;
        }
        if (moveLeft) {
            player.frameY = 3;
        }
        if (moveRight) {
            player.frameY = 1;
        }
        if (moveUp) {
            y = y + 6;
            player.frameY = 0;
            collisionRow = collisionRow;
            collisionDown = false;
        }
    }

    if (collisionLeft == false && collisionRight == false &&
        collisionDown == false && collisionUp == false) {
        if (moveLeft) {
            pixelX += 6;
            x = x + 6;
            player.frameY = 3;
            if (pixelX == 30) {
                pixelX = 0;
                collisionCol = collisionCol - 1;
            }
            detectCollision()
        }
        if (moveRight) {
            pixelX += 6;
            x = x - 6;
            player.frameY = 1;
            if (pixelX == 30) {
                pixelX = 0;
                collisionCol = collisionCol + 1;
            }
            detectCollision()
        }
        if (moveUp) {
            pixelY += 6;
            y = y + 6;
            player.frameY = 0;
            if (pixelY == 30) {
                pixelY = 0;
                collisionRow = collisionRow - 1;
            }
            detectCollision()
        }
        if (moveDown) {
            y = y - 6;
            pixelY += 6;
            player.frameY = 2;
            if (pixelY == 30) {
                pixelY = 0;
                collisionRow = collisionRow + 1;
            }
            detectCollision()
        }
    }

    if ((moveLeft || moveRight || moveUp || moveDown) &&
        !(moveRight && moveLeft) || (moveUp && moveDown)) {
        player.frameX = (player.frameX + 1) % 3;
    }
}


function animateBattle() {
    let inBattle = window.requestAnimationFrame(animateBattle)
    context.drawImage(battleBackgroundImage, 0, 0, 512, 320);
    let div = document.querySelector('.transition'); // select the div element
    let duration = 2000; // duration of the animation in milliseconds
    let start = null; // variable to store the start time of the animation

    function changeOpacity(timestamp) {
        if (!start) start = timestamp; // set the start time if it is not set already
        let elapsed = timestamp - start; // calculate the time elapsed since the start of the animation
        let progress = elapsed / duration; // calculate the progress of the animation
        let opacity = Math.max(0, 1 - progress * 2); // calculate the opacity value between 1 and 0
        div.style.opacity = opacity; // set the opacity of the div
        if (progress < 0.5 || opacity === 0) { // continue the animation until halfway or the opacity reaches 0
            requestAnimationFrame(changeOpacity); // request the next frame of the animation
        }
    }

    requestAnimationFrame(changeOpacity); // start the animation


    let div2 = document.querySelector('.health-bars'); // select the div element
    let div3 = document.querySelector('.battleAttackBar'); // select the div element
    let duration2 = 2000; // duration of the animation in milliseconds

    function changeOpacityH(timestamp) {
        if (!start) start = timestamp; // set the start time if it is not set already
        let elapsed = timestamp - start; // calculate the time elapsed since the start of the animation
        let progress = elapsed / duration2; // calculate the progress of the animation
        let opacity = Math.min(1, progress * 2); // calculate the opacity value between 0 and 1
        div2.style.opacity = opacity; // set the opacity of the div
        div3.style.opacity = opacity; // set the opacity of the div
        if (progress < 0.5 || opacity === 1) { // continue the animation until halfway or the opacity reaches 1
            requestAnimationFrame(changeOpacityH); // request the next frame of the animation
        }
    }
    requestAnimationFrame(changeOpacityH); // start the animation


    context.drawImage(playerImage,
        player.width, player.height * 1, player.width, player.height,
        140, 190, player.width * 2, player.height * 2);

    context.drawImage(enemyImage,
        enemy.width * enemy.frameX, enemy.height * enemy.frameY, enemy.width, enemy.height,
        380, 60, enemy.width * 1.5, enemy.height * 1.5);



    // Get references to the attack buttons
    let button1 = document.querySelector("#Fireball");
    let button2 = document.querySelector("#Sword");

    // Define a function to handle player attacks
    function playerAttack() {
        // Inflict damage on the AI
        let playerDamage = enemy.hp - player.atk
        enemy.hp = enemy.hp - 1;

        document.querySelector('#dialogBox').style.display = 'block'
        document.querySelector('#dialogBox').innerHTML = 'The player attacks and does ' + playerDamage + ' damage to the enemy';

        // Check if the AI is still alive
        if (enemy.hp <= 0) {
            // AI is dead, end the game
            document.querySelector('#dialogBox').innerHTML = 'The enemy has been slain';
            window.cancelAnimationFrame(inBattle)
            setTimeout(function () {
                let div2 = document.querySelector('.health-bars'); // select the div element
                let div3 = document.querySelector('.battleAttackBar'); // select the div element
                function changeOpacity(timestamp) {
                    if (!start) start = timestamp; // set the start time if it is not set already
                    let elapsed = timestamp - start; // calculate the time elapsed since the start of the animation
                    let progress = elapsed / duration; // calculate the progress of the animation
                    let opacity = Math.max(0, 1 - progress * 2); // calculate the opacity value between 1 and 0
                    div2.style.opacity = opacity; // set the opacity of the div
                    div3.style.opacity = opacity; // set the opacity of the div
                    if (progress < 0.5 || opacity === 0) { // continue the animation until halfway or the opacity reaches 0
                        requestAnimationFrame(changeOpacity); // request the next frame of the animation
                    }
                }
                requestAnimationFrame(changeOpacity); // start the animation
                battle.initiated = false;
                BattleMusic.pause()
                Music.play()
                draw()
            }, 2000)
            return;

        }

        // AI is still alive, it's their turn to attack
        enemyAttack()
    }

    // Define a function to handle AI attacks
    function enemyAttack() {
        // Inflict damage on the player
        let enemyDamage = player.hp - enemy.atk;
        player.hp = player.hp - 1;

        // Update the player health display
        document.querySelector('#dialogBox').style.display = 'block'
        document.querySelector('#dialogBox').innerHTML = 'The enemy attacks and does ' + enemyDamage + ' damage to the player';
        // Check if the player is still alive
        if (player.hp <= 0) {
            // Player is dead, end the game
            document.querySelector('#dialogBox').innerHTML = 'The player has been slain';
            window.cancelAnimationFrame(inBattle)
            setTimeout(function () {
                let div2 = document.querySelector('.health-bars'); // select the div element
                let div3 = document.querySelector('.battleAttackBar'); // select the div element
                function changeOpacity(timestamp) {
                    if (!start) start = timestamp; // set the start time if it is not set already
                    let elapsed = timestamp - start; // calculate the time elapsed since the start of the animation
                    let progress = elapsed / duration; // calculate the progress of the animation
                    let opacity = Math.max(0, 1 - progress * 2); // calculate the opacity value between 1 and 0
                    div2.style.opacity = opacity; // set the opacity of the div
                    div3.style.opacity = opacity; // set the opacity of the div
                    if (progress < 0.5 || opacity === 0) { // continue the animation until halfway or the opacity reaches 0
                        requestAnimationFrame(changeOpacity); // request the next frame of the animation
                    }
                }
                requestAnimationFrame(changeOpacity); // start the animation
                battle.initiated = false;
                BattleMusic.pause()
                Music.play()
                draw()
            }, 2000)
            return;
        }

        // Player is still alive, prompt them to attack again
        document.querySelector('#dialogBox').innerHTML = 'The enemy attacks its your turn now';
        document.querySelector('#dialogBox').style.display = 'none'
    }

    // Attach event listeners to the attack buttons
    button1.addEventListener("click", playerAttack);
    button2.addEventListener("click", playerAttack);

}

function detectCollision() {
    if (moveLeft) {
        let check = collisionsMap[collisionRow][collisionCol - 1]
        if (check == 1025) {
            collisionLeft = true;
            console.log("collision left")
        }
        else {
            collisionLeft = false;
        }
    }
    if (moveRight) {
        let check = collisionsMap[collisionRow][collisionCol + 1]
        if (check == 1025) {
            collisionRight = true;
            console.log("collision right")
        }
        else {
            collisionRight = false;
        }
    }
    if (moveUp) {
        let check = collisionsMap[collisionRow - 1][collisionCol]
        if (check == 1025) {
            collisionUp = true;
            console.log("collision up")
        }
        else {
            collisionUp = false;
        }
    }
    if (moveDown) {
        let check = collisionsMap[collisionRow][collisionCol]
        if (check == 1025) {
            collisionDown = true;
            console.log("collision down")
        }
        else {
            collisionDown = false;
        }
    }

}

function player_collides(e) {
    if (player.x + player.width < e.x ||
        e.x + e.width < player.x ||
        player.y > e.y + e.height ||
        e.y > player.y + player.height) {
        return false;
    } else {
        return true;
    }
}


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}

function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft" || key === "a") {
        moveLeft = true;
    } else if (key === "ArrowUp" || key === "w") {
        moveUp = true;
    } else if (key === "ArrowRight" || key === "d") {
        moveRight = true;
    } else if (key === "ArrowDown" || key === "s") {
        moveDown = true;
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "ArrowLeft" || key === "a") {
        moveLeft = false;
    } else if (key === "ArrowUp" || key === "w") {
        moveUp = false;
    } else if (key === "ArrowRight" || key === "d") {
        moveRight = false;
    } else if (key === "ArrowDown" || key === "s") {
        moveDown = false;
    }
}

function load_assets(assets, callback) {
    let num_assets = assets.length;
    let loaded = function () {
        console.log("loaded");
        num_assets = num_assets - 1;
        if (num_assets === 0) {
            callback();
        }
    };
    for (let asset of assets) {
        let element = asset.var;
        if (element instanceof HTMLImageElement) {
            console.log("img")
            element.addEventListener("load", loaded, false);
        }
        else if (element instanceof HTMLAudioElement) {
            console.log("audio");
            element.addEventListener("canplaythrough", loaded, false);
        }
        element.src = asset.url
    }
}
