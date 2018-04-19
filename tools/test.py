import sys, os

#creates the system command to execute artillery benchmarks
def createCommand(xExecutions, xPeople, url):
    return "artillery quick --count %s -n %s %s" % (xExecutions, xPeople, url)

#file containing the language and url separated by "|"
fileLinks = "sortlinks.txt"

#amount of executions and people executing
xExecutions = sys.argv[1]
xPeople = sys.argv[2]

#if we have too many executions, cancel script to save executions
if int(xExecutions) * int(xPeople) >= 50:
    print("*** ERROR ***")
    print("You're doing too many requests, keep it lower than 50")
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
        
        print("*** TESTING %s ***" % (language.upper()))
        os.system(createCommand(xExecutions,xPeople,url))