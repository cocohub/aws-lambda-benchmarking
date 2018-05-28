import json, random

def hello(event, context):
    number = 1000
    
    if event["queryStringParameters"]['arraySize'] != "":
        number = int(event["queryStringParameters"]['arraySize'])
        
    array = random.sample(xrange(number), number)
    
    array = sorted(array)
    
    #print(array)

    body = {
        "message": array,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": "success"#json.dumps(array)
    }

    return response