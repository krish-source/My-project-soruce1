file = open('source data.txt')

print(file.read()) # Read all the contents

print(file.read(100))  # Read by first 200 charecter


file.close()
