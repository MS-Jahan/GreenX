#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <dht.h>
dht DHT;//dht
#define DHT11_PIN 10
 float sensor_volt; 
 int ppm; 
  float R0 = -0.10; 
LiquidCrystal_I2C lcd(0x3F, 16, 2);
#define S1 23
#define S0 22
#define S3 25
#define S2 24
#define sensorOut 26
int redFrequency = 0;
int greenFrequency = 0;
int blueFrequency = 0;//color
int upButton = 2;
int downButton = 3;
int selectButton = 4;
int menu = 1;
int sensorValue=0 ;
int percentValue =0;
int soilmoisture = 1;
void setup() {
  pinMode(48,OUTPUT);
   pinMode(S0, OUTPUT);
    pinMode(S1, OUTPUT);
    pinMode(S2, OUTPUT);
    pinMode(S3, OUTPUT);
    pinMode(sensorOut, INPUT);  
    digitalWrite(S0,HIGH);
    digitalWrite(S1,LOW);
  lcd.init(); // initialize the lcd
  lcd.backlight();
  pinMode(upButton, INPUT_PULLUP);
  pinMode(downButton, INPUT_PULLUP);
  pinMode(selectButton, INPUT_PULLUP);
  updateMenu();
  Serial.begin(9600);
}

void loop() {
digitalWrite(trigPin, LOW);
  delayMicroseconds(2);   
  digitalWrite(trigPin, HIGH);     // send waves for 10 us
  delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH); // receive reflected waves
  distance = duration / 58.2;   // convert to distance
  delay(10);
    // If you dont get proper movements of your robot then alter the pin numbers
  if (distance > 19)            
  {
    digitalWrite(fwdright7, HIGH);                    // move forward
    digitalWrite(revright6, LOW);
    digitalWrite(fwdleft5, HIGH);                                
    digitalWrite(revleft4, LOW);                                                       
  }

  if (distance < 18)
  {
    digitalWrite(fwdright7, LOW);  //Stop                
    digitalWrite(revright6, LOW);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, LOW);
    delay(500);
    digitalWrite(fwdright7, LOW);      //movebackword         
    digitalWrite(revright6, HIGH);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, HIGH);
    delay(500);
    digitalWrite(fwdright7, LOW);  //Stop                
    digitalWrite(revright6, LOW);
    digitalWrite(fwdleft5, LOW);                                
    digitalWrite(revleft4, LOW);  
    delay(100);  
    digitalWrite(fwdright7, HIGH);       
    digitalWrite(revright6, LOW);   
    digitalWrite(revleft4, LOW);                                 
    digitalWrite(fwdleft5, LOW);  
    delay(500);
  }
  if (!digitalRead(downButton)){
    menu++;
    updateMenu();
    delay(100);
    while (!digitalRead(downButton));
  }
  if (!digitalRead(upButton)){
    menu--;
    updateMenu();
    delay(100);
    while(!digitalRead(upButton));
  }
  if (!digitalRead(selectButton)){
    executeAction();
    updateMenu();
    delay(100);
    while (!digitalRead(selectButton));
  }
}

void updateMenu() {
  switch (menu) {
    case 0:
      menu = 1;
      break;
    case 1:
      lcd.clear();
      lcd.print(">Data");
      lcd.setCursor(0, 1);
      lcd.print(" Settings");
      break;
    case 2:
      lcd.clear();
      lcd.print(" Data");
      lcd.setCursor(0, 1);
      lcd.print(">Settings");
      break;
    case 3:
      lcd.clear();
      lcd.print(">Awareness");
      lcd.setCursor(0, 1);
      lcd.print(" Advice");
      break;
    case 4:
      lcd.clear();
      lcd.print(" Awareness");
      lcd.setCursor(0, 1);
      lcd.print(">Advice");
      break;
    case 5:
      menu = 4;
      break;
  }
}

void executeAction() {
  switch (menu) {
    case 1:
      action1();
      break;
    case 2:
      action2();
      break;
    case 3:
      action3();
      break;
    case 4:
      action4();
      break;
  }
}

void action1() {
  sensorValue = analogRead(soilmoisture);
  percentValue =  map(sensorValue,1015, 380, 0 ,120);
  if(percentValue<40){
    digitalWrite(48,LOW);
  }
  else{
    digitalWrite(48,HIGH);
  }
    int sensorValue = analogRead(A0); 
sensor_volt = ((float)sensorValue / 1024) * 5.0; 
ppm = (5.0 - sensor_volt); 
  int chk = DHT.read11(DHT11_PIN);
  int temp =DHT.temperature;
  int hum =DHT.humidity;
  float kelvin =DHT.temperature + 273.15;
 int pressure= 3.31603333*kelvin;
 digitalWrite(S2,LOW);
  digitalWrite(S3,LOW); 
  redFrequency = pulseIn(sensorOut, LOW);
    delay(100);
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  greenFrequency = pulseIn(sensorOut, LOW);
  delay(100);
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blueFrequency = pulseIn(sensorOut, LOW);
  delay(100);
  lcd.clear();
  lcd.setCursor(1,0);         // move cursor to   (0, 0)
  lcd.print("T:");
  lcd.print(temp);
  lcd.print("C|");
  lcd.setCursor(0, 1);         // move cursor to   (2, 1)
  lcd.print(" H:");
  lcd.print(hum);
  lcd.print("%|");
 lcd.setCursor(7,0);
  lcd.print("P:");
  lcd.print(pressure);
  lcd.print("hpa");
  lcd.setCursor(7,1);
  lcd.print("CH4:");
  lcd.print(ppm);
  lcd.print("ppm");
  delay(5000);
  lcd.clear();
  lcd.print(percentValue);
  lcd.print("%");
  delay(3000);
  lcd.clear();
   if(percentvalue>40){
  digitalWrite(relay,HIGH);
 }
 else{
  digitalWrite(relay,LOW);
 }
 
}
void action2() {
  lcd.clear();
  lcd.print(">Welcome to Settings!");
  delay(1500);
}
void action3() {
  lcd.clear();
  lcd.print(">Plant trees!");
  delay(1500);
}
void action4() {
  lcd.clear();
  lcd.print(">PLant Apple in low land!");
  delay(1500);
}
if(ppm>5){
  lcd.println("methene is high in environment";
}
