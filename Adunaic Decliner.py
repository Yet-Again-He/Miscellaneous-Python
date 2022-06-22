'''
Adunaic Inflection Maker

If I was to make a simplified English to Adunaic converter, it will go through 3 stages:
1.  Match each english word to a corrosponding adunaic word using a word list most likely imported via a CVC file.
2.  Change each word to the correct tense.
3.  Make sure all pronouns/pospositions/other prefixes/suffixes are not only attached, but undergo any necessary assimilation.
'''

import string


AdOp = ["mî ", "rô "]    

#a_fort_dict = {"a":"â", "i":"ê", "u":"ô"}  Just there for easy access to a-fortified vowels


def process_word():
    word_tbd = input("Please input verb to be inflected: ")
    word_tbd.strip()
    dec_word_1 = list(word_tbd)
    return dec_word_1

dec_word = process_word()

def inflection():
    infl_case_1 = input("Please input the number of the desired verb tense.\n1. aorist\n2. continuative present\n3. past\n4. continuative past"
"\n5. future\n6. continuative future\nYour Choice: ")
    return infl_case_1


def number():
    num_state_1 = input("is it plural? y/n: ")
    return num_state_1


def BVD(dec_word):

    infl_case = inflection()
    num_state = number()
    

    new_tense = ""

    if infl_case == "1":
        dec_word.append("a")
    elif infl_case == "2":
        if dec_word[1] == "a":
            dec_word[1] = "â"
        elif dec_word[1] == "i":
            dec_word[1] = "ê"
        elif dec_word[1] == "u":
            dec_word[1] = "ô"
        else:
            pass
        dec_word.append("i")
    elif infl_case == "3":
        mid_cons = dec_word[2]
        dec_word.insert(2, mid_cons)
        dec_word.append("a")
    elif infl_case == "4":
        if dec_word[1] == "a":
            dec_word[1] = "â"
        elif dec_word[1] == "i":
            dec_word[1] = "ê"
        elif dec_word[1] == "u":
            dec_word[1] = "ô"
        else:
            pass
        dec_word.append("i")
        dec_word.insert(0, AdOp[0])
    elif infl_case == "5":
        dec_word.append("a")
        dec_word.insert(0, AdOp[1])
    elif infl_case == "6":
        if dec_word[1] == "a":
            dec_word[1] = "â"
        elif dec_word[1] == "i":
            dec_word[1] = "ê"
        elif dec_word[1] == "u":
            dec_word[1] = "ô"
        else:
            pass
        dec_word.append("i")
        dec_word.insert(0, AdOp[1])
    else:
        print("Please enter a number between 1 and 6!")
        BVD(dec_word)

    if num_state == "y":
        dec_word.append("m")
    else:
        pass

    return(new_tense.join(dec_word))


def TVD(dec_word):

    infl_case = inflection()
    num_state = number()
    

    new_tense = ""

    if infl_case == "1":
        dec_word.pop(3)
        dec_word.append("a")
    elif infl_case == "2":
        dec_word[3] = "u"
        dec_word.append("i")
    elif infl_case == "3":
        mid_cons = dec_word[2]
        dec_word.insert(2, mid_cons)
        dec_word.append("a")
    elif infl_case == "4":
        dec_word[3] = "u"
        dec_word.append("i")
        dec_word.insert(0, AdOp[0])
    elif infl_case == "5":
        dec_word.pop(3)
        dec_word.append("a")
        dec_word.insert(0, AdOp[1])
    elif infl_case == "6":
        dec_word[3] = "u"
        dec_word.append("i")
        dec_word.insert(0, AdOp[1])
    else:
        print("Please enter a number between 1 and 6!")
        TVD(dec_word)

    if num_state == "y":
        dec_word.append("m")
    else:
        pass

    return(new_tense.join(dec_word))


if len(dec_word) == 5:
    print(TVD(dec_word))
else:
    print(BVD(dec_word))



#if __name__ == "main":