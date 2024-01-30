def is_valid_identifier(identifier):
    """Check if the given identifier is valid according to C naming rules."""
    return identifier.isidentifier()

def validate_variable_declaration(declaration):
    """Validate a variable declaration."""
    valid_types = ["int", "char", "float", "double"]
    parts = declaration.split()
    if parts[0] not in valid_types:
        return False
    
    # Split by comma to handle multiple declarations
    for part in parts[1:]:
        # Remove potential semicolon
        part = part.replace(";", "")
        # Split by equals to handle initialization
        name_initialization = part.split("=")
        if not is_valid_identifier(name_initialization[0].strip()):
            return False
    return True

def validate_function_declaration(declaration):
    """Validate a function declaration."""
    valid_types = ["int", "char", "float", "double", "void"]
    # Remove semicolon and split declaration into return type, function name, and parameters
    declaration = declaration.rstrip(";")
    return_type, rest = declaration.split(maxsplit=1)
    if return_type not in valid_types:
        return False
    
    # Extract function name and parameters
    function_name, params = rest.split("(", 1)
    params = params[:-1]  # Remove closing parenthesis
    
    if not is_valid_identifier(function_name.strip()):
        return False
    
    if params.strip() and params.strip() != "void":
        for param in params.split(","):
            type_name = param.strip().split()[0]
            if type_name not in valid_types:
                return False
    return True

# Input processing
n = int(input().strip())
for _ in range(n):
    test_case = input().strip()
    if test_case.startswith("1"):
        # Variable declaration
        declaration = test_case[2:]
        if validate_variable_declaration(declaration):
            print("VALID VARIABLE DECLARATION")
        else:
            print("INVALID VARIABLE DECLARATION")
    elif test_case.startswith("2"):
        # Function declaration
        declaration = test_case[2:]
        if validate_function_declaration(declaration):
            print("VALID FUNCTION DECLARATION")
        else:
            print("INVALID FUNCTION DECLARATION")
