test_count = -1

while test_count < 0:
    test_count = int(input(">"))

for i in range(test_count):
    declaration = input(">")
    declaration = declaration.split()
    type = int(declaration.pop(0))
    variable_types = ['int', 'float', 'char', 'double']
    if type == 1:
        if declaration[0] in variable_types:
            declaration.pop(0)
        else:
            print("INVALID VARIABLE DECLARATION")
        
        has_one_variable = True
        for i in declaration:
            i = i.strip()
            if declaration.index(i) == 0:
                if i[-1] == ',':
                    has_one_variable = False
            else:
                
        
    elif type == 2:
        print(declaration)

    

        
