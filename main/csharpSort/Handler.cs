using System; 
using Amazon.Lambda.Core;
using Amazon.Lambda.Serialization.Json;
using Amazon.Lambda.APIGatewayEvents;

[assembly:LambdaSerializer(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]

namespace AwsDotnetCsharp { 
    public class Handler { 
        public APIGatewayProxyResponse Hello(APIGatewayProxyRequest request) { 
            
            int min = 0;
            int max = 10;
            max = Convert.ToInt32(request.QueryStringParameters["arraySize"]);

            int[] unsorted = new int[max]; 

            Random randNum = new Random();
            
            for (int i = 0; i < max; i++) {
                unsorted[i] = randNum.Next(min, max);
            }

            Array.Sort(unsorted);
            
            return new APIGatewayProxyResponse() {
                StatusCode = 200, 
                Body = "success"/*string.Join(", ", unsorted)*/, 
            }; 
        }    
    } 
}