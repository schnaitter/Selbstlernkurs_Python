# Python Syntax Elements - Cheatsheet Todo List

Based on content from chapters 1-3 (000-Einleitung, 010-Installation_Technik, 020-Projekt_Taschenrechner)

## Basic Operations and Data Types

### Arithmetic Operators
- [ ] Addition: `+` (e.g., `2 + 2`, `a += 1`)
- [ ] Subtraction: `-` (e.g., `5 - 3`, `a -= 2`)
- [ ] Multiplication: `*` (e.g., `3 * 4`)
- [ ] Division: `/` (returns float, e.g., `3/2` → `1.5`)
- [ ] Floor division: `//` (returns integer, e.g., `3//2` → `1`)
- [ ] Modulo: `%` (remainder, e.g., `5%3` → `2`)
- [ ] Exponentiation: `**` (e.g., `2**3` → `8`)

### Assignment Operators
- [ ] Basic assignment: `=` (e.g., `a = 5`)
- [ ] Compound assignment: `+=`, `-=`, `*=`, `/=` (e.g., `a += 1`)

### Number Formats
- [ ] Integers: `42`, `1_000_000` (underscores for readability)
- [ ] Floats: `3.14`, `1234e-2` (scientific notation)
- [ ] Large numbers support (arbitrary precision integers)

### Data Type Conversion
- [ ] Convert to integer: `int()` (e.g., `int(3.14)` → `3`)
- [ ] Convert to float: `float()` (e.g., `float(15)` → `15.0`)
- [ ] Convert to string: `str()`

## Variables and Basic I/O

### Variables
- [ ] Variable assignment: `variable_name = value`
- [ ] Variable naming conventions (lowercase with underscores)

### String Literals
- [ ] Single quotes: `'Hello, World!'`
- [ ] Double quotes: `"Hello, World!"`
- [ ] Escape characters: `\'`, `\"`

### Input/Output
- [ ] Print function: `print()` (e.g., `print("Hello")`, `print(variable)`)
- [ ] User input: `input()` (e.g., `name = input("Enter name: ")`)
- [ ] String formatting with f-strings: `f"text {variable} more text"`

## Control Flow

### Conditional Statements
- [ ] `if` statement: `if condition:`
- [ ] `elif` statement: `elif condition:`
- [ ] `else` statement: `else:`
- [ ] Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- [ ] Logical operators: `and`, `or`, `not`
- [ ] Indentation for code blocks (4 spaces)

### Loops
- [ ] `while` loop: `while condition:`
- [ ] Loop control variables and patterns
- [ ] Breaking out of loops with conditions

## Functions

### Function Definition
- [ ] Function definition: `def function_name(parameters):`
- [ ] Function parameters: `def func(param1, param2):`
- [ ] Return statement: `return value`
- [ ] Function docstrings: `"""Documentation string"""`

### Function Calls
- [ ] Calling functions: `function_name(arguments)`
- [ ] Using function return values: `result = function_name(args)`

## Comments and Documentation

### Comments
- [ ] Single-line comments: `# This is a comment`
- [ ] Inline comments: `code  # comment`

### Documentation
- [ ] Function docstrings with parameters and returns sections
- [ ] Help function: `help(function_name)`

## File Handling and Modules

### Python Files
- [ ] Creating `.py` files
- [ ] Running Python files: `python3 filename.py`
- [ ] Interactive mode with files: `python3 -i filename.py`

### Imports
- [ ] Import specific function: `from module import function`
- [ ] Import entire module: `import module`
- [ ] Import with alias: `import module as alias`
- [ ] Accessing module functions: `module.function()`

## REPL (Read-Eval-Print-Loop)

### REPL Usage
- [ ] Starting Python REPL: `python3`
- [ ] REPL prompts: `>>>` (main), `...` (continuation)
- [ ] Exiting REPL: `quit()` or `Ctrl+D`
- [ ] Understanding REPL states: Read, Eval, Print, Loop

## Error Handling Concepts

### Basic Error Awareness
- [ ] Understanding that `input()` returns strings
- [ ] Type conversion errors (e.g., `int("abc")` causes `ValueError`)
- [ ] Undefined variable errors: `NameError`

## Programming Concepts

### Code Structure
- [ ] Code execution order: top to bottom
- [ ] Indentation significance (4 spaces for blocks)
- [ ] Code blocks in functions, if statements, loops

### Boolean Logic
- [ ] Boolean values: `True`, `False`
- [ ] Boolean expressions in conditions
- [ ] Combining conditions with `and`, `or`, `not`

### Advanced Concepts Introduced
- [ ] Function scope and local variables
- [ ] Parameter passing
- [ ] Return values vs. print output
- [ ] Module system basics
- [ ] Interactive programming patterns

## Best Practices Mentioned

### Code Style
- [ ] Using meaningful variable names
- [ ] Proper indentation
- [ ] Comment usage for explanations
- [ ] Function documentation

### Programming Patterns
- [ ] REPL pattern for interactive programs
- [ ] Input validation concepts
- [ ] Modular code organization
- [ ] Separation of concerns (functions for specific tasks)