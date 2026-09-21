from .ast import PrintStatement, StringLiteral


class Interpreter:

    def execute(self, statements):

        for statement in statements:

            if isinstance(statement, PrintStatement):
                self.execute_print(statement)

            else:
                raise RuntimeError(
                    f"Unknown statement: {statement}"
                )

    def execute_print(self, statement):

        value = self.evaluate(statement.expression)

        print(value)

    def evaluate(self, expression):

        if isinstance(expression, StringLiteral):
            return expression.value

        raise RuntimeError(
            f"Unknown expression: {expression}"
        )