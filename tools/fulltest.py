import os, time, sys

arraySize = 0
arrayMax = 5000000
incrementSize = 500000
testLanguage = sys.argv[1]

if testLanguage == "":
    print("\n*** Gotta enter a language ***")
    sys.exit(0)
    
while arraySize <= arrayMax:
    print("\n*** TESTING %s WITH ARRAY SIZE %s ***" % (testLanguage.upper(), str(arraySize).upper()))
    #os.system("test 60 1 " + str(arraySize) + " " + testLanguage)
    os.system("testEx 1 " + str(arraySize) + " " + testLanguage)
    arraySize += incrementSize