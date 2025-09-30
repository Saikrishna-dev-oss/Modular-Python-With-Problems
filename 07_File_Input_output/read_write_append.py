# f = open("John Doe.txt","a")
# string = """I am a Very Bad Boy 
# I love Playing Video Games"""
# data = f.write(string)
# f.close()

with open("Sai.txt",'r') as f:
    content = f.read()
    print(content)