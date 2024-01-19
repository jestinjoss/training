import os

current_directory = os.getcwd()
print("current working directory is "+current_directory)
file = open("./data/test.txt","r")
content=file.read()
print(content)
file.close()
# adding comment
# adding comment in the branch code