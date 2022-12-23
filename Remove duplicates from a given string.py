#Given a string S, the task is to remove all the duplicates in the given string. Below are the different methods to remove duplicates in a string.
def unique(s):
 
    st = ""
    length = len(s)

    for i in range(length):
        c = s[i]
        if c not in st:
            st += c
 
    return st
