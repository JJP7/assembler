# Converting hack assembly langauge to machine code as part of the nand2tetris course

destdict = {"null": "000", "M": "001", "D": "010", "MD": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111"}
compdict = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100", "A": "0110000", "M": "1110000", "!D": "0001101", "!A": "0110001", "!M": "1110001", "-D": "0001111", "-A": "0110011", "-M": "1110011", "D+1": "0011111", "A+1": "0110111",
            "M+1": "1110111", "D-1": "0001110", "A-1": "0110010", "M-1": "1110010", "D+A": "0000010", "D+M": "1000010", "D-A": "0010011", "D-M": "1010011", "A-D": "0000111", "M-D": "1000111", "D&A": "0000000", "D&M": "1000000", "D|A": "0010101", "D|M": "1010101"}
jumpdict = {"null": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
symboldict = {"R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5", "R6": "6", "R7": "7", "R8": "8", "R9": "9", "R10": "10", "R11": "11", "R12": "12", "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4"}
instructiondict = {}


class HackAssembler:

    pass

class Tests:    # should we do this?

    pass



def string_test(toTest):   # do something like for test in unit test check test

    passtest = False

    if type(toTest) == str:   #should I use is isinstance instead?

        passtest = True

    return passtest


# All I'm doing is just a copy paste here nothing fancy...

def get_machine_code():
    pass

def parse_instruction(instrcuction):
    pass

def get_instruction():      # gets the instruction

    instruction = ""


    return instruction



# Fuck comments, the code should speak for itself!


def convert2binary16(decimal):

    # should we like do a unit test to see if decimal is a string?

    if string_test(decimal) == True:

        bin = f"{int(decimal):b}"

        toAdd = 16 - len(bin)

        zeroes = ""

        for _ in range(0, toAdd):
            zeroes += "0"

        binary16 = zeroes + bin

        return binary16

    else:
        print("decimal is not a string!")


# def get_next_instruction(next_instruction):
#
#     next_instruction = next_instruction
#
#     return next_instruction


def translate():
    pass

# should have followed the proposed API I suppose

def numberfile():

    # okay, we're gonna store it in a dictionary, I think.

    f = open(r"C:\Users\JUVER\Downloads\nand2tetris\nand2tetris\projects\06\pong\Pong.asm", "r")

    # mapping the line number to the instruction number

    linenum = 0
    instruction_num = -1


    for line in f:

        loadlabel = False
        addLabel = False
        temp = ""
        isInstruction = False

        #check if it is whitespace, comments or empty lines else it is an instruction
        # should be like parse_line() or something
        for c in line.strip():

            #I'll just deal with them the simple way lol, can't be bothered


            # I need to handle in-line comments

            if c == "/":    # this is in binary mode though
                break

            elif c == " ":
                break

            elif c == "":
                break

            elif c == "(":    # this actually isn't complete but meh.

                loadlabel = True

            elif c == ")":
                loadlabel = False
                addLabel = True

            elif loadlabel == True:
                temp += c

            else:
                isInstruction = True


        if isInstruction == True:
            instruction_num += 1

        if addLabel == True:

            symboldict[temp] = str(instruction_num + 1)  # address of the next instruction, do we count comments in?
                                                         # let's no store this in binary


        linenum += 1

    f.close()

    print("symboltable", symboldict)

def checkifnumber(temp):

    isNumber = False
    isDigit = False

    for c in temp:

        isDigit = False

        # what the hell, that took long, lol
        for x in range(0, 10):  # so, nine was not included in the checking i see...
            if c == str(x):
                isDigit = True
                break

        # checking the status after we checked the digit
        if isDigit == False:
            isNumber = False
            break

        else:  # check the next digit
            continue

    # check if it is a number finally

    if isDigit == True:
        isNumber = True

    return isNumber
    
def isComment(line):
    
    # this assumes that the commemt is in the beginning though(stripped line)...
    if (line[0] == "/") and (line[1] == "/"):
        return True
        
    else
        return False
        
def isLabel(line):
    
    if line[0] == "(":
        	return True
        	
    else
        return False
        
def checkInstructionA(line):
    
    if line[0] == "@":
        return True
        
    else 
        return False
        
def checkInstructionC(line):
    
    # I need to get rid of the  state/time dependency/spaghetti code
    if (isLabel(line) == False) and (isComment(line) == False) and (checkInstructionA(line) == False) 
    # the first instruction can't be a space(we passed in line.strip().
    	return True

def getInstructionType(line):
    
    if checkInstructionA(line) == True:
        return "A"
    
    elif checkInstructionC(line) == True:
        return "C"

def loadInstructionA(line):
    
    if getInstructionType(line) == "A":
        return True
    else
        return False
        
def loadInstructionC(line):
    
    if getInstructionType(line) == "C":
        return True
    else
        return False
        
def getTemp()

    temp = ""   # holds the instruction to execute

    # iterating through each character in the present line    
    
    for c in line.strip():

        print(c)

        ########### comments and whitespace #################

        if c == " ": # this works becaused we passed in line.strip(), so there are no whitespaces in the beginning 
            break.   # when do we make this false though?

        elif isComment(line.strip()) == True:
            break

        ############## Actual instructions ##############     

        elif isLabel(line.strip()) == True:
            break
    
        elif loadInstructionA(line.strip()) == True:
                
            if c == "@":
                continue
                
            else
                temp += c  #also handles variable declaration
                
        # probably can replace this with is valid instruction
        elif loadInstructionC(line.strip()) == True:
            temp += c      #oh, I already need to store it.        

    return temp
    
# no, don't open file just parse the file
def parse_file():    # so many things are inside on function....

    f = open(r"C:\Users\JUVER\Downloads\nand2tetris\nand2tetris\projects\06\pong\Pong.asm", "r")
    g = open(r"C:\Users\JUVER\Downloads\Nand_Folder\nand2tetris\projects\06\pong\Pong.hack", "w")

    variableAdress = 16

    line = f.readline()

    while line:  # if there are more lines to read?

        #FLAGS

        # maybe I should just use a reset function for these        

        parsedest = False
        parsecomp = False
        parsejump = False

        label = False
        load_label = False

# what if there are like multiple instructions I won't be able to handle that
# I feel like my code is so sloppy should like do this in C++ to know how bad my code is

        dest = ""
        comp = ""
        jump = ""

        # how do I run each character

        print(line.strip())
      
        #replace temp with query
        temp = getTemp()

# This is still in the current line

        # process the instruction
        # this will only work it I don't allow spaces within instructions

# parse instruction and translate

        #if toTranslate is not None: .....

        if line.strip() is not "":     # why did not None not work?

            if getInstructionType(line.strip()) == "A":

                print("a instruction")

                gotmachinecode = False

                #I can try looping through these functions with a list

                # check if temp is in the symbol table
                for key in symboldict:
                    if key == temp:


                        machinecode = convert2binary16(symboldict[temp])
                        gotmachinecode = True


                # check if its a number then

                if gotmachinecode == False:

                    isNumber = checkifnumber(temp)

                    if isNumber == True:

                        machinecode = convert2binary16(temp)
                        gotmachinecode = True


                # it must be a variable then
                # How the hell do I fucking use encapsulation?
                if gotmachinecode == False:

                    symboldict[temp] = str(variableAdress)

                    machinecode = convert2binary16(str(variableAdress)) # notice that it should be a string
                    gotmachinecode = True


                    variableAdress += 1


            elif getInstructionType(line.strip()) == ":

                print("ey! C instruction!")

                parsedest = True

                # check if we should jump:

                for c in temp:

                    # these need to come first

                    if c == "=":
                        parsedest = False
                        parsecomp = True

                    # what if there is no semicolon?

                    elif c == ";":

                        if parsecomp == True:
                            parsecomp = False
                            parsejump = True

                        elif parsecomp == False:

                            #c'mon man this is stupid
                            parsedest = False



                            comp = dest   # this is probably not how you assign a srting
                            dest = "null"

                            parsejump = True


                    # then we add
                    # why must we use elif

                    elif parsedest == True:
                        dest += c

                    elif parsecomp == True:
                        comp += c

                    elif parsejump == True:
                        jump += c     # make this false after?

                ### decode dest #####

                # do an op-code

                machinecode = ""

                machinecode += "1"

                machinecode += "11"    # unused bits?

                ### decode comp #####

                for id in compdict:

                    if id == comp:
                        machinecode += compdict[comp]

                for id in destdict:

                    if id == dest:   # how to check it two strings are equal?

                        machinecode += destdict[dest]


                ### decode jump #####

                for id in jumpdict:

                    if id == jump:

                        machinecode += jumpdict[jump]

                if parsejump == False:
                    machinecode += jumpdict["null"]


            #write the machine code onto the file
            #opening another file inside of a file, where should I put this though?

            if not isComment:

                # I know the problem, it still writes even though it is not an instruction

                g.write(machinecode + "\n")

        line = f.readline()

    f.close()
    g.close()


# machine language specification:

def code_generation():
    pass

if __name__ == "__main__":

    numberfile()
    parse_file()
