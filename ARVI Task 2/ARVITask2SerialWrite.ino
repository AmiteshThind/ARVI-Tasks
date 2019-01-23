int data;

void setup() { 
  Serial.begin(9600); 
  pinMode(7, OUTPUT); 
  digitalWrite (7, LOW);
  
}
 
void loop() {
while (Serial.available()){ // checks if data is being transmitted to device
  data = Serial.read(); // assings data the value that is transmitted by the python code
}

if (data == '1')
digitalWrite (7, HIGH);//turns led on

else if (data == '0')
digitalWrite (7, LOW);//turns led off

}
