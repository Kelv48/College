

function chooseFirstAttacker() {
    if (Math.random() < 0.5) {
      return player;
    } else {
      return enemy;
    }
  }
  
  // Define function for player to attack enemy
  function playerAttack() {
    let damage = player.attack - enemy.defense;
    enemy.health -= damage;
    console.log(`${player.name} attacked ${enemy.name} for ${damage} damage!`);
  }
  
  // Define function for enemy to attack player
  function enemyAttack() {
    let damage = enemy.attack - player.defense;
    player.health -= damage;
    console.log(`${enemy.name} attacked ${player.name} for ${damage} damage!`);
  }
  
  // Define function to check if either player or enemy is defeated
  function checkForDefeat() {
    if (player.health <= 0) {
      console.log(`${player.name} has been defeated!`);
      return true;
    } else if (enemy.health <= 0) {
      console.log(`${enemy.name} has been defeated!`);
      return true;
    } else {
      return false;
    }
  }
  
  // Define function for a single turn in the combat
  function combatTurn() {
    let attacker = chooseFirstAttacker();
    if (attacker === player) {
      playerAttack();
      if (!checkForDefeat()) {
        enemyAttack();
        checkForDefeat();
      }
    } else {
      enemyAttack();
      if (!checkForDefeat()) {
        playerAttack();
        checkForDefeat();
      }
    }
  }
  
  // Begin the combat loop
  while (!checkForDefeat()) {
    combatTurn();
  }