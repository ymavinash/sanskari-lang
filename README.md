# Sanskari

> A programming language built from scratch with Python.

**Sanskari** is an experimental programming language designed and implemented from the ground up to explore how programming languages work internally.

The project is being built step by step, starting with a lexer and parser and gradually evolving into an interpreted and eventually compiled language.

---

## 🚧 Project Status

**Early Development**

Sanskari is currently under active development.

### Currently implemented

- [x] Lexer
- [x] Tokenization
- [x] Parser
- [x] Abstract Syntax Tree (AST)
- [x] Tree-walk interpreter
- [x] Variables
- [x] String literals
- [x] Number literals
- [x] `cheppu` — output statement
- [x] `petti` — variable declaration
- [x] `.san` source files
- [ ] Arithmetic expressions
- [ ] Boolean expressions
- [ ] Comparisons
- [ ] Conditional statements
- [ ] Loops
- [ ] Functions
- [ ] Arrays / collections
- [ ] Modules
- [ ] Compiler
- [ ] Standard library

The feature roadmap will evolve as the language develops.

---

## ✨ Example

A simple Sanskari program:

```san
petti naam = "Avinash"
petti age = 22

cheppu(naam)
cheppu(age)
```

Output:

```text
Avinash
22
```

---

## 🧠 Language Architecture

Sanskari follows a traditional language-processing pipeline:

```text
              Sanskari Source
                    │
                    ▼
                 Lexer
                    │
                    ▼
                  Tokens
                    │
                    ▼
                 Parser
                    │
                    ▼
                   AST
                    │
              ┌─────┴─────┐
              ▼           ▼
         Interpreter    Compiler
              │           │
              ▼           ▼
           Runtime     Target Code
```

The current implementation focuses on the interpreter.

The long-term goal is to support both:

- **Interpreting** Sanskari programs directly
- **Compiling** Sanskari programs to another target

---

## 🏗️ Project Structure

```text
sanskari-lang/
│
├── examples/
│   └── hello.san
│
├── src/
│   └── sanskari/
│       ├── __init__.py
│       ├── environment.py
│       ├── interpreter.py
│       ├── lexer.py
│       ├── main.py
│       ├── parser.py
│       └── syntax_tree.py
│
├── tests/
│
├── .gitignore
├── README.md
└── ...
```

### Components

**Lexer**

Converts source code into tokens.

```text
petti age = 22
```

becomes conceptually:

```text
PETTI
IDENTIFIER
EQUAL
NUMBER
```

**Parser**

Consumes the tokens and builds the program's structure.

**AST**

The Abstract Syntax Tree represents the meaning of the source program.

**Interpreter**

Walks the AST and executes the program.

**Environment**

Stores variables and their values during execution.

---

## 🔤 Current Syntax

### Variable Declaration

Use `petti` to declare a variable:

```san
petti naam = "Avinash"
petti age = 22
```

### Output

Use `cheppu` to print a value:

```san
cheppu(naam)
cheppu(age)
```

You can also print a string directly:

```san
cheppu("Namaskaram, Sanskari!")
```

---

## ▶️ Running Sanskari

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/sanskari-lang.git
cd sanskari-lang
```

Run an example:

```bash
python3 -m src.sanskari.main examples/hello.san
```

Example output:

```text
Avinash
22
```

---

## 🛠️ Built With

Sanskari is currently implemented using:

- **Python**
- Python `dataclasses`
- Python `enum`
- Git / GitHub

No parser-generator framework is currently used. The lexer and parser are being implemented manually to understand the fundamentals of language design.

---

## 🗺️ Roadmap

### Phase 1 — Language Foundation

- [x] Project structure
- [x] Lexer
- [x] Parser
- [x] AST
- [x] Interpreter
- [x] Variables
- [x] Strings
- [x] Numbers

### Phase 2 — Expressions

- [ ] Addition
- [ ] Subtraction
- [ ] Multiplication
- [ ] Division
- [ ] Operator precedence
- [ ] Parenthesized expressions
- [ ] Expression evaluation

Example:

```san
petti x = 10
petti y = 20

cheppu(x + y)
cheppu(x * y)
```

### Phase 3 — Control Flow

- [ ] Boolean values
- [ ] Comparisons
- [ ] `if`
- [ ] `else`
- [ ] `while`
- [ ] `for`

### Phase 4 — Functions

- [ ] Function declarations
- [ ] Parameters
- [ ] Return values
- [ ] Function calls
- [ ] Local scope

### Phase 5 — Language Features

- [ ] Arrays
- [ ] Strings improvements
- [ ] Built-in functions
- [ ] Error handling
- [ ] Modules
- [ ] Standard library

### Phase 6 — Compiler

The long-term goal is to introduce a compiler alongside the interpreter.

```text
Sanskari Source
      │
      ▼
    Lexer
      │
      ▼
    Parser
      │
      ▼
     AST
      │
      ▼
   Compiler
      │
      ▼
 Target Language
```

Potential compilation targets will be evaluated as the language matures.

---

## 🎯 Why Sanskari?

The name **Sanskari** comes from the Sanskrit-derived word commonly associated with being cultured, refined, and rooted in values.

The language is named this way as a nod to its Indian linguistic inspiration while being built using modern programming-language engineering concepts.

The goal is not to recreate an existing language, but to understand and experiment with the fundamentals of language design.

---

## 📚 Learning Goals

This project is also a hands-on exploration of:

- Lexical analysis
- Parsing
- Abstract Syntax Trees
- Interpreters
- Compilers
- Runtime environments
- Expression evaluation
- Scope and state
- Programming-language design
- Language implementation

---

## 🤝 Contributing

Sanskari is currently primarily a learning and experimental project.

As the language matures, contribution guidelines and development documentation will be added.

If you are interested in programming languages, compilers, interpreters, or language design, feel free to explore the project.

---

## 📜 License

License information will be added as the project develops.

---

## ⭐ Project

**Sanskari — A programming language built from scratch.**

Built with curiosity, code, and a little bit of `cheppu()`.
