"""
I declare, upon my honor, that I did this machine problem assignment as a
collaboration with Arwin Delasan, using online resources from the following: copilot.
Further, my solution is not a copy of any of my collaborators' solutions.
"""

class Declaration:
    def split_input(self, input):
        delimiters = [' ', '(', ')', ',', ';', "="]
        tokens = []
        token = ''

        for i in input:
            if i in delimiters:
                if token:
                    tokens.append(token)
                    token = ''
                tokens.append(i)
            else:
                token += i
            
        if token:
            tokens.append(token)
        
        return tokens
    
    def is_valid_variable_function_name(self, item):
        for i in item[1:]:
            if not (i.isalpha() or i.isdigit() or i == "_"):
                return False
            
        return True

class Variable_declaration(Declaration):
    """
    Variable inputs:
    0 dtype
    1 space
    2 var
    3 comma
    4 equal
    5 value
    6 semi
    7 dead state
    """
    DATA_TYPES = ['int', 'char', 'float', 'double']
    table = [[8] * 8 for i in range(10)]
    table[0] = [1, 8, 8, 8, 8, 8, 8, 8]
    table[1] = [8, 2, 8, 8, 8, 8, 8, 8]
    table[2] = [8, 2, 3, 8, 8, 8, 8, 8]
    table[3] = [8, 4, 8, 1, 5, 8, 7, 8]
    table[4] = [8, 4, 8, 8, 5 , 8, 7, 8]
    table[5] = [8, 9, 6, 8, 8, 6, 8, 8]
    table[6] = [8, 6, 8, 1, 5, 8, 7, 8]
    table[7] = [8, 0, 8, 8, 8, 8, 8, 8]
    table[8] = [8, 8, 8, 8, 8, 8, 8, 8]
    table[9] = [8, 8, 6, 8, 8, 6, 8, 8]

    def __init__(self, declaration):
        self.declaration = self.split_input(declaration)
        self.state = 0
        self.variables = []
        self.data_type = None

    def is_valid_value(self, item):
        if (self.data_type == "int" or self.data_type == "char") and (item.isdigit()\
        or (item[0] == "-" and item[1:].isdigit()) or (item[0] == "'" and item[-1] == "'")):
            return True
        elif (self.data_type == "float" or self.data_type == "double") and (item.isdigit() or item.count(".") == 1):
            return True
        else:
            return False
        
    def is_value(self, item):
        if item.isdigit() or (item[0] == "-" and (item[1:].isdigit() or (item.count(".") == 1 and item[1:].replace(".", "").isdigit())))\
        or (item[0] == "'" and item[-1] == "'") or (item.count(".") == 1 and item.replace(".", "").isdigit()):
            return True
        
        return False
        

    def input_type(self, item):
        if item in self.DATA_TYPES:
            self.data_type = item
            return 0
        elif item == " ":
            return 1
        elif item[0].isalpha() or item[0] == "_":
            if self.state == 5 or self.state == 9:
                if item in self.variables:
                    return 2
                else:
                    return 7
            elif item not in self.variables and self.is_valid_variable_function_name(item):
                self.variables.append(item)
                return 2
            else:
                return 7
        elif item == ",":
            return 3
        elif item == "=":
            return 4
        elif item == ";":
            return 6
        elif self.is_value(item):
            if self.is_valid_value(item):
                return 5
            else:
                return 7
        else:
            return 7

    def is_valid(self):
        for item in self.declaration:
            self.state = self.table[self.state][self.input_type(item)]
        
        return True if self.state == 7 else False


class Function_declaration(Declaration):
    """
    Function declaration inputs
    0 - dtype
    1 - space
    2 - fun/var name
    3 - comma
    4 - open params
    5 - close params
    6 - semi colon
    7 - invalid
    """

    data_types = ['int', 'float', 'char', 'double', 'void']
    table = [[11] * 8 for i in range(12)]
    
    table[0][0] = 1

    table[1][1] = 2

    table[2][1] = 2
    table[2][2] = 3

    table[3][4] = 4

    table[4][0] = 7
    table[4][1] = 4
    table[4][5] = 5

    table[5][1] = 5
    table[5][3] = 2
    table[5][6] = 6

    table[6][1] = 0

    table[7][1] = 8
    table[7][3] = 9
    table[7][5] = 5

    table[8][1] = 8
    table[8][2] = 10
    table[8][3] = 9
    table[8][5] = 5

    table[9][1] = 9
    table[9][0] = 7

    table[10][1] = 10
    table[10][3] = 9
    table[10][5] = 5


    def __init__(self, declaration):
        self.declaration = self.split_input(declaration)
        self.state = 0
        self.variables = []

    def input_type(self, item):
        if item in self.data_types:
            return 0
        elif item == " ":
            return 1
        elif (item[0].isalpha() or item[0] == "_") and item not in self.variables:
            if self.is_valid_variable_function_name(item):
                self.variables.append(item)
                return 2
            else:
                return 7
        elif item == ",":
            return 3
        elif item == "(":
            return 4
        elif item == ")":
            return 5
        elif item == ";":
            return 6
        else:
            return 7
        
    def is_valid(self):
        for item in self.declaration:
            self.state = self.table[self.state][self.input_type(item)]
        
        return True if self.state == 6 else False




# main
test = int(input())
output = []
output_dict = {
    0: "VALID VARIABLE DECLARATION",
    1: "INVALID VARIABLE DECLARATION",
    2: "VALID FUNCTION DECLARATION",
    3: "INVALID FUNCTION DECLARATION",
}

for i in range(test):
    declaration = input()
    is_1 = True if declaration[0] == '1' else False
    declaration = declaration[2:]

    if is_1:
        test = Variable_declaration(declaration)
        if test.is_valid():
            output.append(0)
        else:
            output.append(1)
    else:
        test = Function_declaration(declaration)
        if test.is_valid():
            output.append(2)
        else:
            output.append(3)

for i in output:
    print(output_dict[i])
