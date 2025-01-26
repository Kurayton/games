let ballX, ballY;
let ballSpeedX = 4;
let ballSpeedY = 3;
let ballRadius = 15;

function setup() {
  createCanvas(500, 500);
  ballX = width / 2;
  ballY = height / 2;
}

function draw() {
  background(255);

  // Draw the ball
  fill(255, 0, 0);
  noStroke();
  ellipse(ballX, ballY, ballRadius * 2, ballRadius * 2);

  // Update ball position
  ballX += ballSpeedX;
  ballY += ballSpeedY;

  // Check for collisions with walls
  if (ballX - ballRadius <= 0 || ballX + ballRadius >= width) {
    ballSpeedX = -ballSpeedX;
  }
  if (ballY - ballRadius <= 0 || ballY + ballRadius >= height) {
    ballSpeedY = -ballSpeedY;
  }
}
