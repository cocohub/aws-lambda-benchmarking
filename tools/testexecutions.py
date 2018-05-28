import sys, os

#creates the system command to execute artillery benchmarks
def createCommand(executions, url):
    return "artillery quick -c %s -n 1 %s"  % (executions, url)

#amount of executions and people executing
executions = sys.argv[1]
arraySize = sys.argv[2]
testLanguage = sys.argv[3]

javaUrl = "https://pss8dqdqjc.execute-api.us-east-1.amazonaws.com/dev/hello"
nodeUrl = "https://lpfsgzaeg6.execute-api.us-east-1.amazonaws.com/dev/hello"
pythonUrl = "https://leczhu11tf.execute-api.us-east-1.amazonaws.com/dev/hello"
csharpUrl = "https://5ls7c6fb3j.execute-api.us-east-1.amazonaws.com/dev/hello"
urlEnding = "?arraySize=" + arraySize

urls = {'java':javaUrl, 'nodejs': nodeUrl, 'python': pythonUrl, 'csharp':csharpUrl}

if executions == "" or arraySize == "" or testLanguage == "":
    print("You need to enter 3 parameters; executions, size of array and language to be tested")
    sys.exit(0)

print("*** TESTING %s ***" % (testLanguage.upper()))
os.system(createCommand(executions, urls[testLanguage] + urlEnding))