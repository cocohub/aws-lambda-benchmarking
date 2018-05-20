import sys, os, datetime

#creates the system command to execute artillery benchmarks
def createCommand(xExecutions, xPeople, extras, url):
    #return "artillery quick --count %s -n %s %s %s" % (xExecutions, xPeople, extras, url)
    #return "artillery quick --duration %s --rate %s -n %s" (xExecutions, xPeople, extras, url)
    return "artillery quick -d 60 -r 1 -n 1 " + url
    

#file containing the language and url separated by "|"
fileLinks = "links.txt"

#amount of executions and people executing
xExecutions = sys.argv[1]
xPeople = sys.argv[2]
arraySize = sys.argv[3]
maxExecutions = 1000

if xExecutions == "" or xPeople == "" or arraySize == "":
    print("You need to enter 3 parameters fool; number of executions, number of people executing and size of array")
    sys.exit(0)

#if we have too many executions, cancel script to save executions
if int(xExecutions) * int(xPeople) >= maxExecutions:
    print("*** ERROR ***")
    print("You're doing too many requests, keep it lower than %d" % (maxExecutions))
    sys.exit(0)
else:
    #otherwise, go ahead
    print("*** STARTING TEST ***")
    print("%s REQUESTS * %s PEOPLE\n" % (xExecutions,xPeople))

#open file with urls and for each link, run benchmark
with open(fileLinks) as f:
    for line in f:
        language = line.split("|")[0]
        url = line.split("|")[1].rstrip() + "?arraySize=" + arraySize
        
        print(url)
        
        #time = datetime.datetime.now().strftime("%Y-%m-%d-%I:%M:%S")
        #output = "-o %s%s" % (language,time + ".json")
        #output = "-o %s" % (language + ".json")
        output = ""
        
        print("*** TESTING %s ***" % (language.upper()))
        os.system(createCommand(xExecutions,xPeople, output, url))