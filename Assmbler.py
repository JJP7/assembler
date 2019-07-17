# Converting hack assembly langauge to machine code as part of the nand2tetris course

destdict = {"null": "000", "M": "001", "D": "010", "MD": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111"}
compdict = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100", "A": "0110000", "M": "1110000", "!D": "0001101", "!A": "0110001", "!M": "1110001", "-D": "0001111", "-A": "0110011", "-M": "1110011", "D+1": "0011111", "A+1": "0110111",
            "M+1": "1110111", "D-1": "0001110", "A-1": "0110010", "M-1": "1110010", "D+A": "0000010", "D+M": "1000010", "D-A": "0010011", "D-M": "1010011", "A-D": "0000111", "M-D": "1000111", "D&A": "0000000", "D&M": "1000000", "D|A": "0010101", "D|M": "1010101"}
jumpdict = {"null": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
symboldict = {"R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5", "R6": "6", "R7": "7", "R8": "8", "R9": "9", "R10": "10", "R11": "11", "R12": "12", "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4"}

def string_test(toTest):   # do something like for test in unit test check test

    passtest = False

    if type(toTest) == str:   #should I use is isinstance instead?

        passtest = True

    return passtest

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

def isNoise(line): 

    if (isComment(line) == True) or (line[0] == " ") or (line == ""):
        return True
        
    else
        return False
           
def isInstruction(line):
    
    if (isNoise(line) == False) and (isLabel(line) == False):
        return True
        
    else
        return False
        
def getLabel(line):
    
    label = ""
    
    for c in line.strip():
        
        if c == ")":
            break
            
        elif c is not "(":
            	label += c
            	
     return label
        
        
# should have followed the proposed API I suppose

def numberfile():

    global symboldict

    f = open(r"C:\Users\JUVER\Downloads\nand2tetris\nand2tetris\projects\06\pong\Pong.asm", "r")

    # mapping the line number to the instruction number

    linenum = 0
    instruction_num = -1

    for line in f:

        #I'll just deal with them the simple way lol, can't be bothered                            	                
                     
        if isInstruction(line.strip()) == True
            instruction_num += 1
            
        elif isLabel(line) == True:
            label = getLabel(line.strip())
            symboldict[label] = str(instruction_num + 1)# address of the next instruction, do we count comments in?
   
        else 
            break                                                     # let's no store this in binary
        
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
    if (isLabel(line) == False) and (isNoise(line) == False) and (checkInstructionA(line) == False): 
    # the first instruction can't be a space(we passed in line.strip().
    	return True

def getInstructionType(line):
    
    if checkInstructionA(line) == True:
        return "A"
    
    elif checkInstructionC(line) == True:
        return "C"

def loadInstructionA(line):
    
    temp = ""
    
    for c in line:
        
        if c == " ":
            break
            
        if c is not "@":
            temp += c
            
    return temp
               
def loadInstructionC(line):
    
    temp = ""
    
    for c in line:
        
        if c == " ":
            break
            
        else
            temp += c
            
     return temp      
        
def getTemp(line):

    # iterating through each character in the present line    
    
    if (isNoise(line.strip()) == True) or (isLabel(line.strip()) == True):
        return None    # do nothing
        
    elif getInstructionType(line.strip()) == "A":
        temp = loadInstructionA(line.strip())
        
    elif getInstructionType(line.strip()) == "C":
        temp = loadInstructionC(line.strip())                                                                                                              
                   
    return temp

def getMachineCodeA(temp, variableAdress):
    
    gotmachinecode = False  #I can try looping through these functions with a list

    # check if temp is in the symbol table
    machinecode, gotmachinecode = checkTempIfSymbol(temp)                     

    # check if its a number then
    if gotmachinecode == False:
        machinecode, gotmachinecode = checkTempIfNumber(temp)
                   
    # it must be a variable then
    if gotmachinecode == False:
        machinecode, gotmachinecode, variableAdress = checkTempIfVariable(temp, variableAdress) 

    return [machinecode, variableAdress]

def getMachineCodeC(temp):
        
    dest = getdest(temp)
    comp = getcomp(temp, dest)
    jump, parsejump = getjump(temp) # parsejump is for addimg 000 in the machinecode if its False
  
    # do an op-code

    machinecode = "111"   # unused bits?

    ### decode comp #####

    for id in compdict:

        if id == comp:
            machinecode += compdict[comp]
            
    ### decode dest #####

    for id in destdict:

        if id == dest:   # how to check it two strings are equal?

            machinecode += destdict[dest]

    ### decode jump #####

    for id in jumpdict:

        if id == jump:

            machinecode += jumpdict[jump]

    if parsejump == False:
        machinecode += jumpdict["null"]
    
    return machinecode

def checkTempIfSymbol(temp):
    
    thisDict = {"machinecode": None, "gotmachinecode": None}
    
    for key in symboldict:
        if key == temp:

            thisDict["machinecode"] = convert2binary16(symboldict[temp])
            thisDict["gotmachinecode"] = True
   
    return thisDict.values()

def checkTempIfNumber(temp):
    
    output = {"machinecode": None, "gotmachinecode": None}
    
    if checkifnumber(temp) == True:

        output["machinecode"] = convert2binary16(temp)
        output["gotmachinecode"] = True
    
    return output.values()

def checkTempIfVariable(temp, variableAdress):
    
    global symboldict
    
    output = {"machinecode": None, "gotmachinecode": None, "variableAdress": variableAdress}
    
    symboldict[temp] = str(variableAdress)

    output["machinecode"] = convert2binary16(str(variableAdress)) # notice that it should be a string
    output["gotmachinecode"] = True

    output["variableAdress"] += 1
     
    return output.values()
    
def findEqualSign(temp):
    
    for c in temp:
        if c == "=":
            return True
            
    return False
    
# The previous approach was probably much faster like about ~ O(n).
def getdest(temp):
    
    dest = ""
    
    if findEqualSign(temp) == True:
           
        for c in temp:
            if c == "=":
                break
            else 
                dest += c
               
    else
        dest = "null"
    
    return dest

def getcomp(temp, dest):
    
    comp = ""
    
    if dest is "null":          
        for c in temp:
            comp += c
    else:
        load = False
        for c in temp:
            
            if c is == "=":
                load = True
            
            elif load == True:
                if c == ";":
                    break
                    
                else
                    comp += c
    
    return comp
    
def getjump(temp):
    
    jump = ""
    parsejump = False
    load = False
    
    for c in temp:
        if c == ";":
            load = True
            parsejump = True
            
        elif load == True:
            jump += c
        
    return [jump, parsejump]
    
# no, don't open file just parse the file
def parse_file():    # so many things are inside on function....

    f = open(r"C:\Users\JUVER\Downloads\nand2tetris\nand2tetris\projects\06\pong\Pong.asm", "r")
    g = open(r"C:\Users\JUVER\Downloads\Nand_Folder\nand2tetris\projects\06\pong\Pong.hack", "w")

    variableAdress = 16

    line = f.readline()

    while line:          

        print(line.strip())
             
        temp = getTemp(line.strip())   

        if getInstructionType(line.strip()) == "A":

            print("a instruction")
            
            machinecode, variableAdress = getMachineCodeA(temp, variableAdress)
                           
        elif getInstructionType(line.strip()) == "C":
            
            print("ey! C instruction!")                                                                                                                                                                                                                                                                                                        
                                  
            machinecode = getMachineCodeC(temp) 
            
            #opening another file inside of a file, where should I put this though?

        if (isNoise(line.strip()) == False) and (isLabel(line.strip()) ==False):                
            g.write(machinecode + "\n")

        line = f.readline()

    f.close()
    g.close()

if __name__ == "__main__":

    numberfile()
    parse_file()
