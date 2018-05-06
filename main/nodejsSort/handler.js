'use strict';

module.exports.hello = (event, context, callback) => {
    Array.prototype.quick_sort = function () {
    if (this.length < 2) { return this; }
 
    var pivot = this[Math.round(this.length / 2)];
 
    return this.filter(x => x <  pivot)
               .quick_sort()
               .concat(this.filter(x => x == pivot))
               .concat(this.filter(x => x >  pivot).quick_sort());
    };
    
    function int_arr(a, b) {
        return a - b;
    }
    
    var arraySize = 1000;
    arraySize = event["queryStringParameters"]['arraySize']
    
    var array = Array.from({length: arraySize}, () => Math.floor(Math.random() * arraySize));
    array = array.sort(int_arr);
    //console.log(array);
    
    //console.log(event);
    
    
  const response = {
      statusCode: 200,
      headers: {
        "x-custom-header" : "My Header Value"
      },
      body: JSON.stringify({ "message": array })
    };

  callback(null, response);

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // callback(null, { message: 'Go Serverless v1.0! Your function executed successfully!', event });
};
