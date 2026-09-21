from .lexer import TokenType
from .syntax_tree import (
    PrintStatement,
    StringLiteral,
    NumberLiteral,
    VariableExpression,
    VariableDeclaration,
)


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

        if self.current().type == TokenType.PETTI:
            return self.parse_variable_declaration()

        raise SyntaxError(
            f"Unexpected token: {self.current().type}"
        )

    def parse_print(self):
        self.advance()  # consume cheppu

        if self.current().type != TokenType.LEFT_PAREN:
            raise SyntaxError("Expected '(' after cheppu")

        self.advance()

        if self.current().type == TokenType.STRING:
            value = StringLiteral(
                self.advance().value
            )

        elif self.current().type == TokenType.IDENTIFIER:
            value = VariableExpression(
                self.advance().value
            )

        else:
            raise SyntaxError(
                "Expected a string or variable"
            )

        if self.current().type != TokenType.RIGHT_PAREN:
            raise SyntaxError("Expected ')' after expression")

        self.advance()

        return PrintStatement(value)
        
    def parse_variable_declaration(self):
    # Consume 'petti'
        self.advance()

        if self.current().type != TokenType.IDENTIFIER:
            raise SyntaxError(
                "Expected variable name after petti"
            )

        name = self.advance().value

        if self.current().type != TokenType.EQUAL:
            raise SyntaxError(
                "Expected '=' after variable name"
            )

        self.advance()

        if self.current().type == TokenType.STRING:
            value = StringLiteral(
                self.advance().value
            )

        elif self.current().type == TokenType.NUMBER:
            value = NumberLiteral(
            int(self.advance().value)
            )

        else:
            raise SyntaxError(
            "Expected a string or number"
            )

        return VariableDeclaration(
            name=name,
            initializer=value,
        )
        