#define SWITCH 2
#define GREEN 3 
#define RED 4
#define RGB_SOURCE 5

int counter = 0;
int RG[2] = {RED, GREEN};

void setup()
{
  pinMode(SWITCH, INPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(RED, OUTPUT);
  pinMode(RGB_SOURCE, OUTPUT);

  digitalWrite(RGB_SOURCE, HIGH);
  Serial.begin(9600);
  
}

void loop()
{
  
  if(counter >= 2)
    counter = 0;
  
  digitalWrite(RG[counter], LOW);
  
  int switchRead = digitalRead(SWITCH);
  
  if(switchRead == HIGH){ 
    digitalWrite(RG[counter], HIGH);
    counter++;
  }

  delay(150);
  
  Serial.println(switchRead);
  
  
}