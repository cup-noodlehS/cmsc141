"""
I declare, upon my honor, that I did this machine problem assignment by myself
using references from the lecture notes and MPs.

I declare, upon my honor, that I did this machine problem assignment by myself
using online resources from the following:
- https://www.w3schools.com/python/

Further, my solution is not a copy from the aforementioned sources.

I declare, upon my honor, that I did this machine problem assignment as a
collaboration with Arwin Delasan.
Further, my solution is not a copy of any of my collaborators' solutions.
"""

def split_input(input_string):
    punctuation = set("(),;")
    output = []
    current_word = ""
    
    for char in input_string:
        if char.isalnum() or char == "-":
            current_word += char
        elif char in punctuation or char.isspace():
            if current_word:
                output.append(current_word)
                current_word = ""
            if char in punctuation:
                output.append(char)

    if current_word:
        output.append(current_word)
    
    return output

def valid_variable_name(name):
    if not name or not name[0].isalpha() and name[0] != "_":
        return False
    if name in ["int", "char", "float", "double", "void"]:
        return False

    for c in name:
        if not c.isalnum() and c != "_":
            return False
            
    return True

def valid_variable_value(type, value, variables):
    if value in variables[:-1]:
        return True
    if type == 'int' or type == 'double':
        try:
            int(value) if type == 'int' else float(value)
            return True
        except ValueError:
            if type == 'int':
                return len(value) == 3 and value.startswith("'") and value.endswith("'")
            return False
    elif type == 'float':
        try:
            float(value)
            return True
        except ValueError:
            return False
    elif type == 'char':
        if len(value) == 3 and value.startswith("'") and value.endswith("'"):
            return True
        else:
            try:
                int(value)
                return True
            except ValueError:
                return False

def validate_variable_declaration(declaration):
    variable_types = ['int', 'float', 'char', 'double']
    variable_type = ''
    variables = []

    has_var_type = False
    has_next_var = False
    last_step = False
    check_var_value = False
    
    for i in declaration:
        if declaration.index(i) == len(declaration) - 1:
            last_step = True

        # check if variable type is defined
        if not has_var_type:
            if i in variable_types:
                has_var_type = True
                has_next_var = True
                variable_type = i
                continue
            else:
                return False
            
        if not has_next_var and not check_var_value and '=' not in i and i != ';':
            return False
        
        # check if end of declaration
        if i[-1] == ';':
            has_var_type = False
            i = i[:-1]

        if i == '=':
            if variables.count(variables[-1]) > 1:
                return False

            check_var_value = True
            continue



        # check if variable name is valid
        if has_next_var:
            # check if variable has "=" sign
            if '=' in i:
                x = i.split('=')
                x = [item.strip() for item in x]
                if not valid_variable_name(x[0]):
                    return False
                else:
                    variables.append(x[0])
                    if x[1][-1] == ',':
                        x[1] = x[1][:-1]
                        has_next_var = True
                    else:
                        has_next_var = False
                    
                    if not valid_variable_value(variable_type, x[1], variables):
                        return False
            else:
                # check if variable name has comma
                if i[-1] == ',':
                    x = i[:-1]
                    if not valid_variable_name(x):
                        False
                    else:
                        variables.append(x)
                        has_next_var = True
                else:
                    has_next_var = False
                    if not valid_variable_name(i):
                        return False
                    else:
                        variables.append(i)
        elif not last_step and not has_next_var and not check_var_value and '=' not in i:
            return False
        
        if check_var_value:
            check_var_value = False
            if i[-1] == ',':
                i = i[:-1]
                has_next_var = True
            else:
                has_next_var = False
            
            if not valid_variable_value(variable_type, i, variables):
                return False
            
        if not has_next_var and not check_var_value and '=' in i:
            x = i.split('=')
            x = [item.strip() for item in x]
            if x[1][-1] == ',':
                x[1] = x[1][:-1]
                has_next_var = True
            else:
                has_next_var = False
            
            if not valid_variable_value(variable_type, x[1], variables):
                return False

        # LAST check if declaration is valid
        if last_step:
            return not has_var_type
        
    return True

def validate_funciton_declaration(declaration):
    declaration = split_input(declaration)
    function_types = ['int', 'float', 'char', 'double', 'void']
    
    stage = 0
    for item in declaration:
        if stage == 0:
            if item in function_types:
                stage = 1
                continue
            else:
                return False
        elif stage == 1:
            if item not in function_types and item != ',' and (item[0] == '_' or item[0].isalpha()):
                if valid_variable_name(item):
                    stage = 2
                    continue
                else:
                    return False
            else:
                return False
        elif stage == 2:
            if item == '(':
                stage = 3
                continue
            else:
                return False
        elif stage == 3:
            if item in function_types:
                stage = 4
                continue
            elif item == ')':
                stage = 5
                continue
            else:
                return False
        elif stage == 4:
            if item == ',':
                stage = 3
                continue
            elif item == ')':
                stage = 5
                continue
            elif item not in function_types and (item[0] == '_' or item[0].isalpha()):
                if valid_variable_name(item):
                    stage = 4
                    continue
                else:
                    return False
            else:
                return False
        elif stage == 5:
            if item == ';':
                stage = 6
                continue
            elif item == ',':
                stage = 1
                continue
            else:
                return False
        elif stage == 6:
            if item != ' ':
                if item in function_types:
                    stage = 1
                    continue
                else:
                    return False
            elif item == ' ':
                return True
            else:
                return False
                
    return stage == 6

test_count = -1
output = []

while test_count < 0:
    test_count = int(input())

for i in range(test_count):
    declaration = input()
    var_declaration = declaration.split()
    func_declaration = declaration[2:]
    type = int(var_declaration.pop(0))


    if type == 1:
        if (validate_variable_declaration(var_declaration)):
            output.append("VALID VARIABLE DECLARATION")
        else:
            output.append("INVALID VARIABLE DECLARATION")
    elif type == 2:
        if (validate_funciton_declaration(func_declaration)):
            output.append("VALID FUNCTION DECLARATION")
        else:
            output.append("INVALID FUNCTION DECLARATION")

for i in output:
    print(i)