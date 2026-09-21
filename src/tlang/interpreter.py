from .environment import Environment

from .syntax_tree import (
    PrintStatement,
    StringLiteral,
    VariableExpression,
    VariableDeclaration,
    NumberLiteral
)

class Interpreter:

    def __init__(self):
        self.environment = Environment()

    def execute(self, statements):

        for statement in statements:

            if isinstance(statement, VariableDeclaration):
                self.execute_variable_declaration(statement)

            elif isinstance(statement, PrintStatement):
                self.execute_print(statement)

            else:
                raise RuntimeError(
                    f"Unknown statement: {statement}"
                )

    def execute_variable_declaration(self, statement):

        value = self.evaluate(
            statement.initializer
        )

        self.environment.define(
            statement.name,
            value
        )

    def execute_print(self, statement):

        value = self.evaluate(
            statement.expression
        )

        print(value)

    def evaluate(self, expression):

        if isinstance(expression, StringLiteral):
            return expression.value
        
        if isinstance(expression, NumberLiteral):
            return expression.value

        if isinstance(expression, VariableExpression):
            return self.environment.get(
                expression.name
            )

        raise RuntimeError(
            f"Unknown expression: {expression}"
        )