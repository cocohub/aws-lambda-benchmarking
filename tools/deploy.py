import sys, os

#creates the system command to deploy
def createCommand(xExecutions, xPeople, url):
    return "sls deploy"

#amount of executions and people executing
option = sys.argv[1]
todoString = ""
if option.strip() == "-a":
    todoString = ", DEPLOYING EVERYTHING"

print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))

deployFolder = os.getcwd() + "\\main\\"
#print(deployFolder)

#todo
#if java in dir, mvn package, then sls deploy
for dir in os.listdir(deployFolder):
    os.chdir(deployFolder + dir)
    os.system("sls deploy")

