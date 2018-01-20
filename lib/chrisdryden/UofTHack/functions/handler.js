

const lib = require("lib")({token: "hqia_boMoZ8Rxx-yg7jRTjc8hAbl7PQNPuPBdYLNn8JuMnK3xQrFSQI1mSrc2Cg_"})


/**
* @param {string} sender The phone number that sent the text to be handled
* @param {string} receiver The StdLib phone number that received the SMS
* @param {string} message The contents of the SMS
* @param {string} createdDatetime Datetime when the SMS was sent


* @returns {any}
*/



module.exports = (sender, receiver, message, createdDatetime, context, callback) => {

	// callback
lib.messagebird.tel['@0.0.17'].sms({
  originator: receiver, // (required)
  recipient: sender, // (required)
  body: message // (required)
}, (err, result) => { 
	callback(null, 'hello world');

/* your code */ });


  
};
