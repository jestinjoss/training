def count_lines(content):
    print("No of lines: #")

def count_words(content):
    print("No of words: #")
    
def print_alternate_lines(content):
    print("Alternate lines go here")


file = open("./data/test.txt","r")
content=file.read()
print("PRINTING NUMBER OF LINES")
print("========================")
count_lines(content)
print("========================")

print("PRINTING NUMBER OF WORDS")
print("========================")
count_words(content)
print("========================")

print("PRINTING ALTERNATE LINES")
print("========================")
print_alternate_lines(content)
print("========================")

file.close()
# adding comment
# adding comment in the branc code

    
    