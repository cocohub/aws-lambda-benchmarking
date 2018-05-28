<h1>SETUP</h1>

<h2>Install Serverless Framework</h2>
<code>npm install -g serverless</code>

You need to have an AWS account, get it and then set up your credentials (you will need these for the Serverless Framework)
https://serverless.com/framework/docs/providers/aws/guide/credentials/
<br>
https://www.youtube.com/watch?v=KngM5bfpttA

Also for this test to work you need to install <a href="https://artillery.io/">Artillery.io</a>

<h2>Create your first service</h2>
https://serverless.com/framework/docs/providers/aws/guide/quick-start/

Or simply use the examples in the repo (check the examples folder), just deploy them to your AWS account and invoke them.
Remember that you need to have the core of those languages installed, otherwise you can't compile them.

All examples are ready to be called through the API Gateway. Just copy the folder and deploy.
        
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

Example: python|https://blablabla.execute-api.us-east-1.amazonaws.com/dev/hello
Reason is, the automated test will print the language and then run URL with Artillery to do benchmarks.
<br>

<h2>Create a service:</h2>
<code>serverless create --template TEMPLATENAME --path NAMEOFDIR</code>
This will create a service in the directory NAMEOFDIR in your current working directory
<hr>

<h2>Deploy the service:</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<br>
<code>serverless deploy</code>

This will deploy the service to AWS
<hr>

<h2>Run the function on AWS</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<br>
<code>serverless invoke -f FUNCTIONNAME</code> (usually it's hello)
<hr>

<h2>Run the function locally</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<br>
<code>serverless invoke local -f FUNCTIONNAME</code> (usually it's hello)
<hr>

<h1>BENCHMARKING</h1>
<h2>Preparation</h2>
As written before, include your function invocation urls in links.txt.
If you wish to change starting array size, increment size or array max, do so in tools/fulltest.py.

<h2>Run</h2>
Run starttest.bat
