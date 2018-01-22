

const lib = require("lib")({token: "hqia_boMoZ8Rxx-yg7jRTjc8hAbl7PQNPuPBdYLNn8JuMnK3xQrFSQI1mSrc2Cg_"})
const axios = require("axios")

/**
* @param {string} sender The phone number that sent the text to be handled
* @param {string} receiver The StdLib phone number that received the SMS
* @param {string} message The contents of the SMS
* @param {string} createdDatetime Datetime when the SMS was sent


* @returns {any}
*/



module.exports = (sender, receiver, message, createdDatetime, context, callback) => {

	// callback
	axios.post( 'ec2-18-218-80-92.us-east-2.compute.amazonaws.com:8080', {
		title = "yolo"
	}).then(results => {
		callback(null, 'hello world');
	}).catch(err => {
		console.log(err);
	});

  
};
                                 