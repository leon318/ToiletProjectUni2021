#include "HX711.h"

#define floor_calibration_factor -20550 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define toilet_calibration_factor -23223.00

#define LOADCELL1_DOUT_PIN  6
#define LOADCELL1_SCK_PIN  7
#define LOADCELL2_DOUT_PIN  4
#define LOADCELL2_SCK_PIN  5

HX711 floorscale;
HX711 toiletscale;
float f = 10;
float counter = 0;
int x = 0;
float timestamp = counter*1/f;
void setup() {
  // Open serial port
  Serial.begin(9600);
  // Initialize scales
  floorscale.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
  toiletscale.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
  // Set scale to calibration
//  floorscale.set_scale(floor_calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  toiletscale.set_scale(toilet_calibration_factor);
//  floorscale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  toiletscale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
  Serial.println();
}
void loop() {
while ((counter*1/f*1000) < 15000){
    counter = x++;
    Serial.print(counter*1/f*1000);
//    Serial.print(",");
//    Serial.print((floorscale.get_units() * -1), 3); //scale.get_units() returns a float
    Serial.print(",");
    Serial.print((toiletscale.get_units()), 3);
    //Serial.print(" , ");
    //Serial.print((scale.get_value(1)), 5);
    Serial.println();
  }
}
