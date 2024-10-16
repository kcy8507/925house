function setup() {
  let canvas = createCanvas(500, 500);
  canvas.parent("myCanvas");
  colorMode(HSB);

  // Set angle mode so that atan2() returns angles in degrees
  angleMode(DEGREES);

  describe("Two eyes that follow the cursor.");
}

function draw() {
  background("fffffff");

  // Draw left eye

  let leftX = 150;
  let leftY = 200;

  // Calculate angle between left eye and mouse
  let leftAngle = atan2(mouseY - leftY, mouseX - leftX);

  push();
  translate(leftX, leftY);
  fill(255);
  ellipse(0, 0, 100, 100);
  rotate(leftAngle);
  fill(0);
  ellipse(30, 0, 40, 40);
  pop();

  // Draw right eye

  let rightX = 300;
  let rightY = 200;

  // Calculate angle between right eye and angle
  let rightAngle = atan2(mouseY - rightY, mouseX - rightX);

  push();
  translate(rightX, rightY);
  fill(255);
  ellipse(0, 0, 100, 100);
  rotate(rightAngle);
  fill(0);
  ellipse(30, 0, 40, 40);
  pop();
}
