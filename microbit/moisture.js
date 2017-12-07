/* jshint esversion:6*/

led.setBrightness(64);
let reading = 0;
basic.forever(() => {
  pins.analogWritePin(AnalogPin.P1, 1023);
  reading = pins.analogReadPin(AnalogPin.P0);
  pins.analogWritePin(AnalogPin.P1, 0);

  led.plotBarGraph(reading, 1023);
  serial.writeValue("moisture", reading);

  if (input.buttonIsPressed(Button.A)) {
    basic.showNumber(reading);
  }

  basic.pause(1000);
});
