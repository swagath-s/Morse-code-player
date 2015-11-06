from winsound import Beep

s = 1.0

def sound(string):
    inv = 1.0/s
    print inv
    for i in string:
        if i == '.':
            Beep(500, int(200*inv))
            print int(200*inv)
        elif i == '-':
            Beep(500, int(600*inv))
            print int(600*inv)
        else:
            Beep(37, int(400*inv))
            print int(400*inv)
        Beep(37, int(200*inv))
        print int(200*inv)

def morsify(string):
    inputStr = string.lower()
    output = ""
    for i in inputStr:
        if i==" ":
            output=output+"   "    
        else:
            for k in morse[i]:                
                if k:
                    output=output+"-"
                else:
                    output=output+"."
            output=output+" "                        #spaces between characters
    print "Transcript:", output
    sound(output)
    return "Transcript: "+output
                

morse = {"a":(0, 1), "b":(1, 0, 0, 0), "c":(1, 0, 1, 0), "d":(1, 0, 0), "e":[0], "f":(0, 0, 1, 0), "g":(1, 1, 0), "h":(0, 0, 0, 0), "i":(0, 0), "j":(0, 1, 1, 1), "k":(1, 0, 1), "l":(0, 1, 0, 0), "m":(1, 1), "n":(1, 0), "o":(1, 1, 1), "p":(0, 1, 1, 0), "q":(1, 1, 0, 1), "r":(0, 1, 0), "s":(0, 0, 0), "t":[1], "u":(0, 0, 1), "v":(0, 0, 01), "w":(0, 1, 1), "x":(1, 0, 0, 1), "y":(1, 0, 1, 1), "z":(1, 1, 0, 0), ".":(0, 1, 0, 1, 0, 1), ",":(1, 1, 0, 0, 1, 1), ":":(1, 1, 1, 0, 0, 0), "?":(0, 0, 1, 1, 0, 0), "'":(0, 1, 1, 1, 0), "-":(1, 0, 0, 0, 0, 1), "/":(1, 0, 0, 1, 0), "(":(1, 0, 1, 1, 0, 1), ")":(1, 0, 1, 1, 0, 1), "\"": (0, 1, 0, 0, 1, 0), "@":(0, 1, 1, 0, 1, 0), "=":(1, 0, 0, 0, 1), "1":(0, 1, 1, 1, 1), "2":(0, 0, 1, 1, 1), "3":(0, 0, 0, 1, 1), "4":(0, 0, 0, 0, 1), "5":(0, 0, 0, 0, 0), "6":(1, 0, 0, 0), "7":(1, 1, 0, 0, 0), "8":(1, 1, 1, 0, 0), "9":(1, 1, 1, 1, 0), "0":(1, 1, 1, 1, 1)}


#morsify(raw_input("Input text to morsify:"))
