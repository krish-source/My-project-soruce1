with open('trumpiq.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('trumpiq.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

