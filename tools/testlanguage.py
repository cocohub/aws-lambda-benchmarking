import sys, os

#creates the system command to execute artillery benchmarks
def createCommand(duration, frequency, url):
    return "artillery quick -d %s -r %s -n 1 %s"  % (duration, frequency, url)

#amount of executions and people executing
duration = sys.argv[1]
frequency = sys.argv[2]
arraySize = sys.argv[3]
testLanguage = sys.argv[4]

javaUrl = "https://pss8dqdqjc.execute-api.us-east-1.amazonaws.com/dev/hello"
nodeUrl = "https://lpfsgzaeg6.execute-api.us-east-1.amazonaws.com/dev/hello"
pythonUrl = "https://leczhu11tf.execute-api.us-east-1.amazonaws.com/dev/hello"
csharpUrl = "https://5ls7c6fb3j.execute-api.us-east-1.amazonaws.com/dev/hello"
urlEnding = "?arraySize=" + arraySize

urls = {'java':javaUrl, 'nodejs': nodeUrl, 'python': pythonUrl, 'csharp':csharpUrl}

if duration == "" or frequency == "" or arraySize == "" or testLanguage == "":
    print("You need to enter 4 parameters fool; duration, tests per second, size of array and language to be tested")
    sys.exit(0)

print("*** TESTING %s ***" % (testLanguage.upper()))
os.system(createCommand(duration,frequency, urls[testLanguage] + urlEnding))