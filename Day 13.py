#Q1:
import re
def check_string(string):
    charRE = re.compile(r'[^a-zA-Z0-9.]')
    string = charRE.search(string)
    return not bool(string)
print(check_string("%$%%^&*(#$#%$%"))
print(check_string("dsffcdsafcccsdvsd4545454"))
    
#Q2:

def match_word(s):
    word = '\w\d'
    if re.search (word,s):
        return ("Matched")
    else:
        return ("Not matched")
print(match_word("3273abcdef"))
print(match_word("8989abcdef"))

#Q3:

def word_sen(word):
    sentence = re.compile(r'.*[0-9]$')
    if sentence.match(word):
        return 'matched'
    else:
        return 'not matched'
print(word_sen("jkfghjkfhgkjf"))
print(word_sen("jkfghjkfhgkjf45"))

#Q4:


result = re.finditer(r'([0-9]{1,3})','Exercises' )
print("Length is 1 to 3")
for i in result:
    print(i.group(0))

#Q5:

def upcase(letter):
    text = '[^A-B.]'
    if re.search(text,letter):
        return "mathced"
    else:
        return "Not matched"
print(upcase("GHJJHG"))
print(upcase("KDFD_dfdfd_Dsd"))
