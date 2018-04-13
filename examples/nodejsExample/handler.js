'use strict';

module.exports.hello = (event, context, callback) => {
    
    console.log(event);
    
    
  const response = {
      statusCode: 200,
      headers: {
        "x-custom-header" : "My Header Value"
      },
      body: JSON.stringify({ "message": "Hello Mehrsh! Would you like some penis?" })
    };

  callback(null, response);

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // callback(null, { message: 'Go Serverless v1.0! Your function executed successfully!', event });
};
