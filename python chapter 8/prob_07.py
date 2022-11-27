a = "      Aftab is a good boy       "
print(a)
print(a.strip()) # Do you understand what is strip? yaa bro, love you more than anyone harry bhai

#problem . write a python function to remove a given word from a list and strip it at the same time.

def update_string(string, word):
    b = string.replace(word, "")
    return b.strip()

a = "                 Hii My name is Md Aftab Ali. I am here to know about coding how the computer do any task what is the language using that i can perfom various task on computer so thankyou harry bhai for giving me that opportunity to provide a high powerful python tutorial video                "
c = update_string(a, "Md Aftab ")
print(c)