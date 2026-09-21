from dataclasses import dataclass


@dataclass
class StringLiteral:
    value: str


@dataclass
class PrintStatement:
    expression: StringLiteral