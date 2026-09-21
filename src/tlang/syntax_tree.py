from dataclasses import dataclass

@dataclass
class StringLiteral:
    value: str


@dataclass
class NumberLiteral:
    value: int


@dataclass
class VariableExpression:
    name: str


@dataclass
class PrintStatement:
    expression: object


@dataclass
class VariableDeclaration:
    name: str
    initializer: object