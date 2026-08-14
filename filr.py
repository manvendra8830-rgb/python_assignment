
# fiel exccecution program ...

file = open("myfile.txt",'w')

file.write("Hello i am manvendra singh \n")
file.write("this is file of content \n")
file.write("I become a devops engneer ")

file.close()

content = open("myfile.txt",'r')
content = content.read()
print(content)
