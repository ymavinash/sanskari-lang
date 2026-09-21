import sys

from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 -m src.tlang.main <file.tl>")
        return

    filename = sys.argv[1]

    with open(filename, "r") as file:
        source = file.read()

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    interpreter.execute(ast)


if __name__ == "__main__":
    main()