 #include<SoftwareSerial.h>

SoftwareSerial client(9,10);

void setup()
{
  Serial.begin(115200);
  client.begin(115200);
  delay(500);

  if(client.available())
  {
    Serial.print("Connected");
  }
  else
  {
    Serial.print("NotConnected");
  }

  //initSIM();
  connectGPRS();
}

void loop()
{
  client.println("AT+HTTPINIT");
  delay(1000);
  ShowSerialData();

  client.println("AT+HTTPPARA=\"CID\",1");
  delay(1000);
  ShowSerialData();

  client.println("AT+HTTPPARA=\"URL\",\"http://xw8zf.localto.net/polls/\"");//Public server IP address
  client.println("AT+HTTPPARA=\"URL\",\"http://xw8zf.localto.net/polls/\"");//Public server address
  delay(1000);
  ShowSerialData();

  client.println("AT+HTTPPARA=\"CONTENT\",\"application/json\"");
  delay(1000);
  ShowSerialData();

  String reading= "1";

  client.println("AT+HTTPDATA=" + String(reading.length()) + ",100000");
  delay(5000);
  ShowSerialData();

  client.println(reading);
  delay(5000);
  ShowSerialData();

  client.println("AT+HTTPACTION=1");
  delay(5000);
  ShowSerialData();

  client.println("AT+HTTPTERM");
  delay(1000);
  ShowSerialData();

}


void connectGPRS()
{ 
  client.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");
  delay(1000);
  ShowSerialData();

  client.println("AT+SAPBR=3,1,\"APN\",\"airtelgprs.com\"");//APN
  delay(1000);
  ShowSerialData();

  client.println("AT+SAPBR=3,1,\"USER\",\"\"");//APN
  delay(1000);
  ShowSerialData();

  client.println("AT+SAPBR=3,1,\"PWD\",\"\"");//APN
  delay(1000);
  ShowSerialData();

  client.println("AT+SAPBR=1,1");
  delay(1000);
  ShowSerialData();

  client.println("AT+SAPBR=2,1");
  delay(1000);
  ShowSerialData();

}

void ShowSerialData()
{
  while(client.available()!=0)
  {
  Serial.write(client.read());
  }
}