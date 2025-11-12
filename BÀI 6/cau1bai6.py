with open('data.txt', 'r') as f:
    content = f.read()       
reversed_content = content[::-1]
print(reversed_content)
