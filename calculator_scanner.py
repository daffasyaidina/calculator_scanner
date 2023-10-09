import re

def tokenize(source_code): 
    tokens = []
    source_code = source_code.replace(' ', '')  
    token_specification = [
        ('number',   r'\d+(\.\d*)?'), 
        ('assign',   r':='),           
        ('id',       r'[A-Za-z]+'),  
        ('lparen',   r'\('),           
        ('rparen',   r'\)'),          
        ('plus',     r'\+'),           
        ('times',    r'\*'),          
        ('div',      r'/'),           
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, source_code):
        kind = mo.lastgroup
        value = mo.group()
        tokens.append((kind, value))  
    return tokens

def main():
    print("Enter your calculator source code:")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    input_string = "\n".join(lines)

    try:
        tokens = tokenize(input_string)
        for token_type, lexeme in tokens:
            print(f"{token_type}: {lexeme}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
