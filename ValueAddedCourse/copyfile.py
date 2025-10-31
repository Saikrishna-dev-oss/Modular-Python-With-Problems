
f1 = open("workFlow3.jpg",'rb')
f2 = open("newImage.png",'wb')

bytes = f1.read()

f2.write(bytes)

