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

# def write2file():
#
#     done = False
#
#     g = open(r"C:\Users\JUVER\Downloads\Nand_Folder\nand2tetris\projects\06\add\Add.hack", "w")
#
#     while not done:
#
#         # get next instruction
#         next_instruction = get_next_instruction()
#
#         g.write(next_instruction)
#
#
#     g.close()
#


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

            # else:
            #     instructiondict[instruction_num] = linenum
            #     instruction_num += 1


        if isInstruction == True:
            instruction_num += 1

        if addLabel == True:

            symboldict[temp] = str(instruction_num + 1)  # address of the next instruction, do we count comments in?
                                                    # let's no store this in binary


        linenum += 1

    f.close()

    print("symboltable", symboldict)


# no, don't open file just parse the file
def parse_file():    # so many things are inside on function....

    f = open(r"C:\Users\JUVER\Downloads\nand2tetris\nand2tetris\projects\06\pong\Pong.asm", "r")
    g = open(r"C:\Users\JUVER\Downloads\Nand_Folder\nand2tetris\projects\06\pong\Pong.hack", "w")

    variableAdress = 16

    line = f.readline()

    while line:  # if there are more lines to read?

        #FLAGS

        # maybe I should just use a reset function for these
        isComment = False
        instructionA = False
        instructionC = False

        loadinstructionA = False
        loadinstructionC = False

        parsedest = False
        parsecomp = False
        parsejump = False

        slash1 = False   # I should really instead be using data structures.   Learning how to program bruh
        label = False
        load_label = False

# what if there are like multiple instructions I won't be able to handle that
# I feel like my code is so sloppy should like do this in C++ to know how bad my code is

        temp = ""   # holds the instruction to execute
        dest = ""
        comp = ""
        jump = ""

        # how do I run each character

        print(line.strip())


        # iterating through each character in the present line

        for c in line.strip():   #parse_line(line.strip())

            print(c)

            # My code needs to be improved


            # Preprocessing
            # applying some tests on c


            ########### comments and whitespace #################

            if c == " ":   #this isn't white space fucking retard

                if loadinstructionA == True:
                    loadinsructionA = False

                    #let's just break out so that we don't have to deal with the comments
                    break

                elif loadinstructionC == True:
                    loadinstructionC = False
                    break

                # generate no machine code
                continue

            # isComment is False by default
            # maybe I should check temp instead?

            elif c == "/":

                if slash1 == True:     #They need to be consecutive though....
                    isComment = True

                slash1 = True

            elif isComment == True:  #no, if something is commented, I can go to the next line right?
                #ignore these things, but when is something a comment?
                break

            ############## Actual instructions ##############


            # when do we make this false though?

            elif c == "@":
                instructionA = True
                loadinstructionA = True

                #also handle variable declaration.

            elif c == "(":
                isComment = True
                break

            elif (c is not "@") and (instructionA == False):# doing this after the instruction

                #oh, I already need to store it.

                temp += c

                instructionC = True
                loadinstructionC = True

            elif loadinstructionA == True:
                temp += c

            elif loadinstructionC == True:
                temp += c

# This is still in the current line

        # process the instruction
        # this will only work it I don't allow spaces within instructions

# parse instruction and translate

        #if toTranslate is not None: .....

        if line.strip() is not "":     # why did not None not work?

            if instructionA == True:

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

                    isNumber = False
                    isDigit = False

                    for c in temp:

                        isDigit = False

                        # what the hell, that took long, lol
                        for x in range(0, 10):   # so, nine was not included in the checking i see...
                            if c == str(x):
                                isDigit = True
                                break

                        # checking the status after we checked the digit
                        if isDigit == False:
                            isNumber = False
                            break

                        else:   # check the next digit
                            continue

                    # check if it is a numver finally

                    if isDigit == True:

                        isNumber = True


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


            elif instructionC == True:

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

def getBinary(decimal):

    # finding the highest power of two:

    binary = ""

    biggerthan = False
    finished = False

    current_power = 0

    leftover = decimal

    # searching for the largest power of two
    # finding the range...

    while not biggerthan:

        if 2**current_power > decimal:

            biggerthan = True

            current_power -= 1

        else:
            current_power += 1

    # getting binary representation
    while not finished:

        if current_power < 0:
            finished = True

        else:

            current_digit = int(leftover/(2**current_power))
            binary += str(current_digit)

            leftover -= current_digit * (2 ** current_power)

            current_power -= 1

    return binary


def code_generation():
    pass

if __name__ == "__main__":

    numberfile()
    parse_file()


