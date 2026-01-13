with open('source.txt', 'r') as source_file:
    content = source_file.read()
with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)
with open('destination.txt', 'r') as destination_file:
    content = destination_file.read()
content = content.replace('cat', 'dog')
with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)
print("Содержимое скопировано и слово 'cat' заменено на 'dog'.")