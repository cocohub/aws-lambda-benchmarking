import sys, os

deployFolder = os.getcwd() + "\\main\\"
#print(deployFolder)

javaDir = "javaSort"
nodejsDir = "nodejsSort"
pythonDir = "pythonSort"
csharpDir = "csharpSort"

#execute command
def cmd(command):
    os.system(command)

#deploy with serverless framework
def sls_deploy():
    cmd("serverless deploy")
    
#build then deploy java
def deployJava():
    cmd("mvn package")
    sls_deploy()
    
#build then deploy c#
def deployCsharp():
    cmd("build.cmd")
    sls_deploy()

#build and deploy all languages    
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
    deployAll() #build and deploy everything
elif option.strip() == "-java":
    todoString = ", DEPLOYING JAVA"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + javaDir) #go to directory
    deployJava() #deploy
elif option.strip() == "-nodejs":
    todoString = ", DEPLOYING NODEJS"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + nodejsDir) #go to directory
    sls_deploy() #deploy
elif option.strip() == "-python":
    todoString = ", DEPLOYING PYTHON"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + pythonDir) #go to directory
    sls_deploy() #deploy
elif option.strip() == "-csharp":
    todoString = ", DEPLOYING C#"
    print("*** STARTING DEPLOYMENT%s ***\n" % (todoString))
    os.chdir(deployFolder + csharpDir) #go to directory
    deployCsharp() #deploy

