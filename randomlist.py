import random, sys

number = int(sys.argv[1])
my_randoms = random.sample(xrange(number), number)

print("Length of array is: %d" % (len(my_randoms)))

with open("arrays.txt", "a") as myfile:
    myfile.write("{:,}".format(number) + ": " + str(my_randoms) + "\n")