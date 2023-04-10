text = "cold"
result = ""

for index,char in enumerate(text):
    result = result + (char * index)

print(result)