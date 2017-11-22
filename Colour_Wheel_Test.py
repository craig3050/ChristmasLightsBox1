int redPin = 11;
int greenPin = 6; 
int bluePin = 9;

int colorVal;

int redVal;
int greenVal;
int blueVal;

int encoder0PinA = 4;
int encoder0PinB = 3;
int encoder0Pos = 0;
int encoder0PinALast = HIGH;
int n = LOW;

void setup() 
{ 
 pinMode (encoder0PinA,INPUT_PULLUP);
 pinMode (encoder0PinB,INPUT_PULLUP);
} 

void loop() 
{
  // Rotary encoder
  // INPUT: rotary encoder position
  // OUTPUT: encoder0Pos [0-1535]
  
  n = digitalRead(encoder0PinA);
 
  if ((encoder0PinALast == LOW) && (n == HIGH)) 
  {
    if (digitalRead(encoder0PinB) == LOW) 
    {
      encoder0Pos = encoder0Pos - 8;
    } 
    else 
    {
      encoder0Pos = encoder0Pos + 8;
    }
    
    if (encoder0Pos < 0) 
    {
      encoder0Pos = 1535;
    }
    else if (encoder0Pos > 1535) 
    {
      encoder0Pos = 0;
    }
  } 

  encoder0PinALast = n;

  // Led strip
  // INPUT: encoder0Pos [0-1535]
  // OUTPUT: redVal [0-255], greenVal [0-255], blueVal [0-255]

  // Red to yellow
  if (encoder0Pos <= 255)
  {
    colorVal = encoder0Pos;             
    redVal = 255;
    greenVal = colorVal;
    blueVal = 0;
  }

  // Yellow to green
  else if (encoder0Pos <= 511)
  {
    colorVal = encoder0Pos - 256;
    redVal = 255 - colorVal;
    greenVal = 255;
    blueVal = 0;
  }

  // Green to cyan
  else if (encoder0Pos <= 767)
  {
    colorVal = encoder0Pos - 512;
    redVal = 0;
    greenVal = 255;
    blueVal = colorVal;
  }

  // Cyan to blue
  else if (encoder0Pos <= 1023)
  {
    colorVal = encoder0Pos - 768;
    redVal = 0;
    greenVal = 255 - colorVal;
    blueVal = 255;
  }

  // Blue to magenta
  else if (encoder0Pos <= 1279)
  {
    colorVal = encoder0Pos - 1024;
    redVal = colorVal;
    greenVal = 0;
    blueVal = 255;
  }

  // Magenta to red
  else
  {
    colorVal = encoder0Pos - 1280;
    redVal = 255;
    greenVal = 0;
    blueVal = 255 - colorVal;
  }

  // Set LED strip color
  analogWrite(redPin, redVal);
  analogWrite(greenPin, greenVal); 
  analogWrite(bluePin, blueVal);}<br>