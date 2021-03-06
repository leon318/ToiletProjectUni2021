/*
 Example using the SparkFun HX711 breakout board with a scale
 By: Nathan Seidle
 SparkFun Electronics
 Date: November 19th, 2014
 License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).
 
 Most scales require that there be no weight on the scale during power on. This sketch shows how to pre-load tare values
 so that you don't have to clear the scale between power cycles. This is good if you have something on the scale 
 all the time and need to reset the Arduino and not need to tare the scale.
 
 This example code uses bogde's excellent library: https://github.com/bogde/HX711
 bogde's library is released under a GNU GENERAL PUBLIC LICENSE
 
 The HX711 does one thing well: read load cells. The breakout board is compatible with any wheat-stone bridge
 based load cell which should allow a user to measure everything from a few grams to tens of tons.
 Arduino pin 2 -> HX711 CLK
 3 -> DOUT
 5V -> VCC
 GND -> GND
 
 The HX711 board can be powered from 2.7V to 5V so the Arduino 5V power should be fine.
 
*/

#include "HX711.h" //This library can be obtained here http://librarymanager/All#Avia_HX711

#define calibration_factor1 -20550.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define zero_factor1 758839 //This large value is obtained using the SparkFun_HX711_Calibration sketch

#define calibration_factor2  
#define zero_factor2 

#define  LOADCELL_DOUT_PIN1  4
#define  LOADCELL_SCK_PIN1  5
#define  LOADCELL_DOUT_PIN2 6
#define  LOADCELL_SCK_PIN12 7


HX711 scale;

void setup() {
  Serial.begin(9600);

  scale.begin(LOADCELL_DOUT_PIN1,LOADCELL_SCK_PIN1);
  scale.begin(LOADCELL_DOUT_PIN2,LOADCELL_SCK_PIN2);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.set_offset(zero_factor); //Zero out the scale using a previously known zero_factor

  scale.set_scale(calibration_factor2); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.set_offset(zero_factor2); //Zero out the scale using a previously known zero_factor

}

void loop() {
  Serial.print(scale.get_units(), 1); //scale.get_units() returns a float
  
  Serial.println();
}
