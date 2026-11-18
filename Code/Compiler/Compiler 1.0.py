# compiler.py

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

    def parse_number(self):
        token = self.current_token()
        if token and token.type == "NUMBER":
            self.pos += 1
            return token.value
        else:
            raise ValueError(f"Erwartet eine Zahl, gefunden: {token}")
