
void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("test\n");
  if(Serial.available()>0)
  {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    String to_send = "test";
    Serial.println('t');
  }
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
}
