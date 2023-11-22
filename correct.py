'''
Character recognition software is widely used to digitise printed texts.
 Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter),
 are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to
 handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
'''
def correct(text):
    corrected_text = ""
    for char in text:
        if char == "5":
            corrected_text += "S"
        elif char == "0":
            corrected_text += "O"
        elif char == "1":
            corrected_text += "I"
        else:
            corrected_text += char
    return corrected_text



def correct(string):
    return string.translate(str.maketrans("501", "SOI"))



def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')