file = open('trumpiq.txt')

#print("****Trump IQ test****")

#print(file.read()) # Read all the contents

for line in file.readlines():
    print(line)


file.close()
