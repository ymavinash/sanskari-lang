from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    CHEPPU = auto()
    STRING = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: str
    
class Lexer:

    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.tokens = []
        
# understanding paranthesis
    def tokenize(self):
        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isspace():
                self.position += 1
                continue

            if current == "(":
                self.tokens.append(
                    Token(TokenType.LEFT_PAREN, current)
                )
                self.position += 1
                continue

            if current == ")":
                self.tokens.append(
                    Token(TokenType.RIGHT_PAREN, current)
                )
                self.position += 1
                continue

            if current == '"':
                self.tokens.append(self.read_string())
                continue

            if current.isalpha():
                self.tokens.append(self.read_identifier())
                continue

            raise SyntaxError(
                f"Unexpected character: '{current}'"
            )

        self.tokens.append(Token(TokenType.EOF, ""))
        return self.tokens
    
# understanding string
    def read_string(self):
    # Skip the opening quote
        self.position += 1

        start = self.position

        while self.position < len(self.source):
            if self.source[self.position] == '"':
                value = self.source[start:self.position]

                # Skip the closing quote
                self.position += 1

                return Token(TokenType.STRING, value)

            self.position += 1

        raise SyntaxError("Unterminated string")
    
# understand cheppu
    def read_identifier(self):
        start = self.position

        while (
            self.position < len(self.source)
            and self.source[self.position].isalnum()
        ):
            self.position += 1

        value = self.source[start:self.position]

        if value == "cheppu":
            return Token(TokenType.CHEPPU, value)

        raise SyntaxError(
            f"Unknown keyword: '{value}'"
        )

# if __name__ == "__main__":
#     source = 'cheppu("Namaskaram, TLang!")'

#     lexer = Lexer(source)
#     tokens = lexer.tokenize()

#     for token in tokens:
#         print(token)