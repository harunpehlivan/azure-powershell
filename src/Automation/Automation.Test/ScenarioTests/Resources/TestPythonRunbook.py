import sys

print("Starting process")
sum = sum(int(sys.argv[i]) for i in range(1,len(sys.argv)))

print ("Process completed")
print(sum)