#include <dht.h> // Library for tempreature sensor 

dht DHT;

#define DHTSensor_PIN 7

void setup(){
  Serial.begin(9600);
}



void loop()
{
  DHT.read11(DHTSensor_PIN);// establishs tempreature sensor 
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);// retrieves value from sensor and prints it out in console
  delay(1500);
}
