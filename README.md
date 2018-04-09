<h1>SETUP</h1>

<h2>Install Serverless Framework</h2>
<code>npm install -g serverless</code>

You need to have an AWS account, get it and then set up your credentials (you will need these for the Serverless Framework)
https://serverless.com/framework/docs/providers/aws/guide/credentials/
<br>
https://www.youtube.com/watch?v=KngM5bfpttA

<h2>Create your first service</h2>
https://serverless.com/framework/docs/providers/aws/guide/quick-start/

Or simply use those in the repo, just deploy them to your AWS account and invoke them.
Remember that you need to have the core of those languages installed, otherwise you can't compile them.

To be able to call a function through the API, your serverless.yml additionally needs the last parts betwen stars (*this*):
<code>functions:</code><br>
  &emsp;<code>hello:</code><br>
    &emsp;&emsp;<code>handler: handler.hello</code><br>
    &emsp;<code>*events:</code><br>
        &emsp;&emsp;<code>- http: GET hello*</code>
        
Once you deploy your function, the url to your function will be printed in the console.
Put it in links.txt to use it in the test suite. Use following format:
language|url
Example: python|https://blabla.aws.com/
<hr>

<h1>FRAMEWORK HELP</h1>
Open the command line in the project root folder.

All services are located in folders.
The URLs to execute functions are in links.txt in this format:
language|url

Example: python|https://q8d5irm342.execute-api.us-east-1.amazonaws.com/dev/hello
Reason is, the automated test will print the language and then run URL with Artillery to do benchmarks.
<br>

<h2>Create a service:</h2>
<code>serverless create --template TEMPLATENAME --path NAMEOFDIR</code>
This will create a service in the directory NAMEOFDIR in your current working directory
<hr>

<h2>Deploy the service:</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<code>serverless deploy</code>

This will deploy the service to AWS
<hr>

<h2>Run the function on AWS</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<code>serverless invoke -f FUNCTIONNAME</code> (usually it's hello)
<hr>

<h2>Run the function locally</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<code>serverless invoke local -f FUNCTIONNAME</code> (usually it's hello)
<hr>

<h1>BENCHMARKING</h1>
<h2>Run</h2>
Run test.bat with two integer arguments, the first is amount of executions and second is amount of people.<br>
<code>test.bat 10 10</code> would simulate 10 people executing each lambda function 10 times.
