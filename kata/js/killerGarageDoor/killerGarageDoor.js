function door(events) {
  let doorState = new DoorState();
  for (const event of events) {
    doorState.handleEvent(event);
  };
  return doorState.allPositions;
}

class DoorState {
  constructor() {
    this.position = 0;
    this.direction = 0;
    this.isMoving = false;
    this.isPaused = false;
    this.allPositions = '';
  }

  handleEvent(event) {
    if(event == '.') this.continueAction();
    if(event == 'P') this.reactToPush();
    if(event == 'O') this.reactToObstacle();
    this.allPositions += this.position;
  }

  continueAction() {
    if(this.isMoving == true && !this.isPaused) {
      this.changePosition();
    }
  }

  reactToPush() {
    if(!this.isMoving && !this.isPaused){
      this.isMoving = true;
      this.changeDirection();
      this.changePosition();
    }
    else if(this.isMoving && this.isPaused) {
      this.isPaused = false;
      this.changePosition();
    }
    else if(this.isMoving && !this.isPaused) {
      this.isPaused = true;
    }
  }

  reactToObstacle() {
    if(this.isMoving == true) {
      this.changeDirection();
      this.changePosition();
    }
  }

  changeDirection(){
    if(this.direction == 0) this.direction = 1;
    else this.direction = -this.direction;
  }

  changePosition() {
    if(this.isMoving && !this.isPaused){
      this.position += this.direction;
      if(this.position < 0) {
        this.position = 0;
        this.isMoving = false;
      } 
      if(this.position > 5) {
        this.position = 5;
        this.isMoving = false;
      } 
    }
  }
}

module.exports = door;