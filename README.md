<i>Disclaimer: this was written to be run in a Windows environment. If you're running this on another OS, just translate the .BAT scripts to whatever scripting language available to you. The tools are written in Python.</i>

<h1>SETUP</h1>

<h2>Install Serverless Framework</h2>
<code>npm install -g serverless</code>

You need to have an AWS account, get it and then set up your credentials (you will need these for the Serverless Framework)
https://serverless.com/framework/docs/providers/aws/guide/credentials/
<br>
https://www.youtube.com/watch?v=KngM5bfpttA

Also for this test to work you need to install <a target="blank" href="https://artillery.io/">Artillery.io</a><br>
<code>npm install -g artillery</code>

The tools are written in <a target="blank" href="https://www.python.org/downloads/">Python</a>, make sure you have that too.

<hr>

<h1>BENCHMARKING</h1>
<h2>Preparation</h2>
After creating your AWS account and setting up the Serverless Framework, make sure you have an environment variable called "FUNC_MEMORY".
You can set this from 128 up to 3008. It has to be in 64MB increments.
Once you have the environment variable set up, run deploy.bat to deploy the original functions in the "main" folder.
Make sure to include your function invocation urls in links.txt, these will be printed out when you deploy.
The URLs and more information about your functions can be found on https://platform.serverless.com/
<br>
If you wish to change starting array size, increment size or array max, do so in tools/fulltest.py.

<h2>Run</h2>
Run starttest.bat
<hr>

<h2>Results</h2>
Head over to <a target="blank" href="https://console.aws.amazon.com/cloudwatch/">CloudWatch</a>.
All invocations will be logged. You can either watch the logs or see the results in graphs by creating a dashboard.
<hr>

<h1>FRAMEWORK HELP</h1>
<h2>Create a service:</h2>
<code>serverless create --template TEMPLATENAME --path NAMEOFDIR</code>
<br>
Use one of the templates for AWS or choose one of ours in the "example" folder. 
This will create a service in the directory NAMEOFDIR in your current working directory
Remember that you need to have the core of those languages installed, otherwise you can't compile them.

All examples are ready to be called through the API Gateway. Just copy the folder and deploy.

https://serverless.com/framework/docs/providers/aws/guide/quick-start/
<hr>

<h2>Deploy the service:</h2>
<code>cd SERVICENAME</code> (you must be in the service folder)
<br>
<code>serverless deploy</code>

This will deploy the service to AWS

Once you deploy your service, the url to your function will be printed in the console.<br>
You can also find your function URLs and other information <a target="blank" href="https://platform.serverless.com/">here</a>.
Put the URL in tools/testexecutions.py to use it in the test suite.<br>
For example, put the follwoing url for Python in the pythonUrl variable:<br>
https://blablabla.execute-api.us-east-1.amazonaws.com/dev/hello
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
