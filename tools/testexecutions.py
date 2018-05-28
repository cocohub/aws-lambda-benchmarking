import sys, os

#creates the system command to execute artillery benchmarks
def createCommand(executions, url):
    return "artillery quick -c %s -n 1 %s"  % (executions, url)

#amount of executions and people executing
executions = sys.argv[1]
arraySize = sys.argv[2]
testLanguage = sys.argv[3]

#URL EXAMPLE:
#https://blabla.execute-api.us-east-1.amazonaws.com/dev/hello
javaUrl = "URL HERE"
nodeUrl = "URL HERE"
pythonUrl = "URL HERE"
csharpUrl = "URL HERE"
urlEnding = "?arraySize=" + arraySize

urls = {'java':javaUrl, 'nodejs': nodeUrl, 'python': pythonUrl, 'csharp':csharpUrl}

if executions == "" or arraySize == "" or testLanguage == "":
    print("You need to enter 3 parameters; executions, size of array and language to be tested")
    sys.exit(0)

print("*** TESTING %s ***" % (testLanguage.upper()))
os.system(createCommand(executions, urls[testLanguage] + urlEnding))