import sys, os

deployFolder = os.getcwd() + "\\main\\"
#print(deployFolder)

javaDir = "javaSort"
nodejsDir = "nodejsSort"
pythonDir = "pythonSort"
csharpDir = "csharpSort"

#creates the system command to deploy
def cmd(command):
    os.system(command)

def sls_deploy():
    cmd("sls deploy")
    
def deployJava():
    cmd("mvn package")
    sls_deploy()
    
def deployCsharp():
    cmd("build.cmd")
    sls_deploy()
    
def deployAll():
    for dir in os.listdir(deployFolder):
        os.chdir(deployFolder + dir)
        if "java" in dir:
            deployJava()
        elif "csharp" in dir:
            deployCsharp()
        else:
            sls_deploy()

option = ""

try:
    option = sys.argv[1]
except IndexError:
    option = "" #if we have no option, we'll deploy everything

if option.strip() == "-a" or option.strip() == "":
    todoString = ", DEPLOYING EVERYTHING"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    deployAll()
elif option.strip() == "-java":
    todoString = ", DEPLOYING JAVA"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + javaDir)
    deployJava()
elif option.strip() == "-nodejs":
    todoString = ", DEPLOYING NODEJS"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + nodejsDir)
    sls_deploy()
elif option.strip() == "-python":
    todoString = ", DEPLOYING PYTHON"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + pythonDir)
    sls_deploy()
elif option.strip() == "-csharp":
    todoString = ", DEPLOYING C#"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + csharpDir)
    deployCsharp()

