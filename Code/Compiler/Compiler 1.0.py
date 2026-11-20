# compiler.py

variables = {}

# Token 
class Token:
    def __init__(self, type_, value):
        self.type = type_   
        self.value = value 

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

# lexer
def lexer(code):
    tokens = []
    words = code.split()

    for word in words:
        if word.isidentifier():
            tokens.append(Token("IDENTIFIER", word))
        elif word.isdigit():
            tokens.append(Token("NUMBER", int(word)))
        elif word in ("=", "+", "-",):
            tokens.append(Token("SYMBOL", word))
        else:
            raise ValueError(f"Unbekanntes Token: {word}")

    return tokens

# parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, value):
        token = self.current_token()
        if token and token.value == value:
            self.pos += 1
            return token
        else:
            raise ValueError(f"Erwartet: {value}, gefunden: {token} Unerwartetes Token")

    def parse_factor(self):
        token = self.current_token()
        if token and token.type == "NUMBER":
            self.pos += 1
            return token.value

        elif token and token.type == "IDENTIFIER":
            var_name = token.value
            self.pos += 1
            if var_name in variables:
                return variables[var_name]
            else:
                raise ValueError(f"Variable '{var_name}' wurde noch nicht definiert.")

        raise ValueError(f"Erwartet eine Zahl oder einen Bezeichner, gefunden: {token}")

    def parse_identifier(self):
        token = self.current_token()
        if token and token.type == "IDENTIFIER":
            self.pos += 1
            return token.value
        else:
            raise ValueError(f"Erwartet einen Bezeichner, gefunden: {token}")

    def parse_expression(self):
        result = self.parse_factor()
        while self.current_token() and self.current_token().value in ("+", "-"):
            op = self.eat(self.current_token().value)
            right = self.parse_factor()
            if op.value == "+":
                result += right
            elif op.value == "-":
                result -= right
        return result

    def parse_statement(self):

        if (self.current_token() and self.current_token().type == "IDENTIFIER" 
            and self.pos + 1 < len(self.tokens) 
            and self.tokens[self.pos + 1].value == "="):

            var_name = self.tokens[self.pos].value
            self.pos += 1
            self.eat("=")
            value = self.parse_expression() 
            variables[var_name] = value

        else: 
            return self.parse_expression()