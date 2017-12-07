/* jshint esversion:6*/
/**
Simple library to manage fog and cloud layer
**/

module.exports = function(api) {
  var cloud_url = `https://api.thingspeak.com/update?api_key=${api}`;
  return {
    runEvery(f, time) {
      setTimeout(() => {
        f();
        runEvery(f, time);
      }, time * 1000);
    },
    pushData(params, cb = () => {}) {
      var url = `${cloud_url}&${params}`;
      request.get(url, (error, response, body) => {
        if (error) return cb(error);
        console.log(`request on "${url}" status ${response.statusCode} body ${body}`);
        cb(null, body);
      });
    }
  };
};
