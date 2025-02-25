# InterPreter Design pattern
- It defines a language or grammers and provides a way to interprete and execute
  sentence and expression of that language. it is used to solve the problem related
  to language processing, rule-based system or domian specific language(DSLS), The
  Interpreter pattern allow you to define a grammer for language and provides a way
  to interprete and evaluate the expression in that language. it is often used in senario
  whrer you need to process or eavluate textual expressions, query language, or 
  configuration language.
- The pattern involves representing each grammer rule as an object or class, which
  each rule typically coresponding to a specific operation and behaviour. the grammer
  rule are combined to form complex expression or sentenecs, which can than be interpreted
  and executed.

# Real word use case
- Programing Language Implemnation
- Regual Expression - match and manupulate string, pattern matching
- SQL Parsing and Execution - the interpreter analyze the query check for sysntax and query
  sematics correctness. and execute the query to retrieve data or perform operations on the
  database.
- Math Expression and Formulas - eg sentific caluclator
- Configuration language - useful in iterpreting in configuarions files or languages, this language
  define the configuration parameters and rules for a system or application. The interpreter parser
  and interpret the configuation File applying the specified setting and configiuartion to the system.
- Sysmbolic mathematics system - computer algebra system

# Terminologies
Context: current state or context in which the expression are being evaluated. it holds any necessary data, or variables that are required during the interpretaion process.
- AbstarctExpression: its abstarct class or interface that define common expression for all
  grammer. it typically declare an interpret(), method that accepts, the context as a param
  and define the interpretetion logic.
- Terminal Expression: its a concrete Implemnation of the Abstarct Expression. They represent the
  Lowest level eleemnts, or terminal sysmbol in the grammer. These expression do not have any subexpressions and provide the interpretation logic for specific terminal symbols and literals
- NonTerminalExpression: it represents high level elements, or nonterminal sysmbol in the grammer.
  These expression have more than one subexpression and provide interpretation logic by recursively
  invoking the interpret(), method on their subexpression.
- Client: its responsible for building and configuring the abstarct systax tree(AST) of the expression based on the grammer rule, it typically creates the instances of terminal and nonterminal
expression and assembles them to form AST.
- InterPreter: its a main components that interpretes and evaluates the expression in the given context, it traverse the AST, and applies the interpretation logic defined in the terminal and
nonterminal expressions.
