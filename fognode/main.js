/* jshint esversion:6 */
var SerialPort = require('serialport');
var request = require('request');

const THINGSPEAK_APIKEY = '4TYULDLKJHADSAHKJHS';

const UPDATE_TIME = 60; // seconds
const MOISTURE = 'field1';
// WINDOWS:
// show ports with ".\node_modules\.bin\serialport-list.cmd"
// port on windows COM4
// LINUX:
// port on linux '/dev/ttyACM0'
const MICROBIT_PORT = '/dev/ttyACM0';

var fog = require('./fog_lib.js')(THINGSPEAK_APIKEY);

// Connection with the microbit
var port = new SerialPort(MICROBIT_PORT, {
  baudRate: 115200,
  parser: SerialPort.parsers.readline('\n')
}, function(err) {
  if (err)
    return console.log('Error: ', err.message);
  console.log('connected');
});

var sum = 0;
var n = 0;
// Run whne new data is receveid from microbit
port.on('data', function(data) {
  var data_split = data.split(':');
  if (data_splitlength == 2) {
    var name = data_split[0];
    var value = parseInt(data_split[1]);
    console.log(`${name}: ${value}`);
    sum += value;
    n++;
  }
});

// use here fogFun or fogFun2
fog.startFog(fogFun2, UPDATE_TIME);

// Fist filter function
function fogFun() {
  fog.pushData(`${MOISTURE}=${sum/n}`);
  sum = 0;
  n = 0;
}

// Second filter function
var previous = 0;
const THRESHOLD = 30;

function fogFun2() {
  var avg = sum / n;
  if (Math.abs(previous - avg) > THRESHOLD)
    fog.pushData(`$URL${MOISTURE}=${avg}`);
  else
    console.log('I will not waste the cloud time!');
  previous = avg;
  sum = 0;
  n = 0;
}
