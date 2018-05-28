import os, time, sys

arraySize = 0
incrementSize = 5000
arrayMax = 1000000
testLanguage = sys.argv[1]

if testLanguage == "":
    print("\n*** Gotta enter a language ***")
    sys.exit(0)
    
    
#it will test the language from 0 to arrayMax
while arraySize <= arrayMax:
    print("\n*** TESTING %s WITH ARRAY SIZE %s ***" % (testLanguage.upper(), str(arraySize).upper()))
    os.system("test 1 " + str(arraySize) + " " + testLanguage)
    arraySize += incrementSize