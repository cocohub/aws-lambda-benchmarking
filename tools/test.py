import sys, os, datetime

#creates the system command to execute artillery benchmarks
def createCommand(xExecutions, xPeople, extras, url):
    return "artillery quick --count %s -n %s %s %s" % (xExecutions, xPeople, extras, url)

#file containing the language and url separated by "|"
fileLinks = "links.txt"

#amount of executions and people executing
xExecutions = sys.argv[1]
xPeople = sys.argv[2]
maxExecutions = 1000

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
        url = line.split("|")[1]
        time = datetime.datetime.now().strftime("%Y-%m-%d-%I:%M:%S")
        #output = "-o %s%s" % (language,time + ".json")
        output = "-o %s" % (language + ".json")
        
        print("*** TESTING %s ***" % (language.upper()))
        os.system(createCommand(xExecutions,xPeople, output, url))