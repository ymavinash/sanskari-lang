from .lexer import TokenType
from .ast import PrintStatement, StringLiteral


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        return self.tokens[self.position]

    def advance(self):
        token = self.current()
        self.position += 1
        return token

    def parse(self):
        statements = []

        while self.current().type != TokenType.EOF:
            statements.append(self.parse_statement())

        return statements

    def parse_statement(self):
        if self.current().type == TokenType.CHEPPU:
            return self.parse_print()

        raise SyntaxError(
            f"Unexpected token: {self.current().type}"
        )

    def parse_print(self):
        self.advance()  # consume cheppu

        if self.current().type != TokenType.LEFT_PAREN:
            raise SyntaxError("Expected '(' after cheppu")

        self.advance()

        if self.current().type != TokenType.STRING:
            raise SyntaxError("Expected a string")

        value = self.advance().value

        if self.current().type != TokenType.RIGHT_PAREN:
            raise SyntaxError("Expected ')' after string")

        self.advance()

        return PrintStatement(
            StringLiteral(value)
        )
        
if __name__ == "__main__":
    from .lexer import Lexer