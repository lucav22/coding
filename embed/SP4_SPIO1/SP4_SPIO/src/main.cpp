#include <Arduino.h>


//right button turns on LED (F6, pressed is turned on 1)
//left button turns off LED (D4, pressed is turned on 1)
//LED is on C7
//Setup 3 DDR registers


uint8_t * ptrDDRC = (uint8_t *) 0x27;
uint8_t * ptrDDRD = (uint8_t *) 0x2A;
uint8_t * ptrDDRF = (uint8_t *) 0x30;
//Setup PORTC (out) and PIND,F (IN)
uint8_t * ptrPORTC = (uint8_t *) 0x28;
uint8_t * ptrPIND = (uint8_t *) 0x29;
uint8_t * ptrPINF = (uint8_t *) 0x2F;

void setup() {
// Setup LED as an ouput, DDR --> 1, C7 DDR

*ptrDDRC |= (1 << 7); // shift it 7 spots making it more obvious
*ptrDDRD &= ~(1 << 4); //makes position 4 a zero after the shift
*ptrDDRF &= ~(1 << 6); 




}


void loop() {
  // put your main code here, to run repeatedly:
  //Read Pin F6 and D4

  if((*ptrPINF & (1<<6)) != 0)
    {
      //F6 is pressed!
      //Turn on C7
      *ptrPORTC |= (1 << 7);


    }
  else
    {
    if((*ptrPIND & (1<<4)) != 0)
    {
      //D4 is pressed!
      //Turn on C7
      *ptrPORTC &=  ~(1 << 7);
    }
  }
delay(1);
}