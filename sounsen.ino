//Inisialisasi pin
int sensorPin = A0; //output dari sensor
int ledPin = 13; //untuk LED
int sensorValue = 00;  //Nilai default sensor
int CompareSensor=300;
 
void setup() {
//inisialisasi i/o
pinMode(ledPin, OUTPUT);
Serial.begin(9600);
}
 
void loop() {
//Pembacaan sensor
sensorValue = analogRead(sensorPin);
//menampilkan nilai pembacaan sensor di serial monitor
Serial.print(" ");
Serial.println(sensorValue, DEC);
 
//untuk indikator dan pembanding
if(sensorValue > CompareSensor){
digitalWrite(ledPin, HIGH);
}
else{
digitalWrite(ledPin, LOW); }
delay(1000);
}
