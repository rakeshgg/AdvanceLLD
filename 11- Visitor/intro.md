# Vistor Design patter

- allow to seperate stutcure of objects hierachy from the operations that can be
  performed on that hierachy. it is used when you have a complex object stucture
  composed of differnet type of objects and you want to define a new operations
  on this stucture without modifying the existing classes. In other word it allow
  you to add new behaviour of existing class hierachy without altering any exiting code
- the main idea behind the visitor pattern is to define the seperate visitor class
  that conatins new operations you want to perform on the object stucture. the visitor
  class visit each elemnts of stucture and performed a desired operation on it. the
  elements of stucture accpte the visitors and provide the necesary access to their
  Internal state, allowing visitors to perform its operations.
- By using the vistor pattern, you can achieve a clear sperations between the objects
  stucture and the operation performed on it. making it easier to add new operations
  without effecting the existing code. This pattern is particularly useful when the
  object stucture is stable, but new operation need to be added frequntly

# Real word use case

- Documnet processing: various operation such as spell checking, word count, formatting
  and generating statics, Each visitors represents a specific operations performed on the
  doc elements like paragraph, heading, images etc
- Code Compilers: Visitor pattern can be used to Implemnt different stage of code analysis
  and transformation, Each visitor represents a specific analysis or transformation operation
  performed on abstract sysntax tree(AST) node
- GUI Componects: operations like rendering, event handling, or data validation on various components
  of the user interface, such as buttons, text fields, checkboxes etc
- database query optimization: it is used to traverse the query execution plan and perform various
  optimization or statical analyses on each step of plan.
- Finacial calculations:In fincacial applications employed to perform calculation on different
  financial instruments such as stocks, bonds, option, each visitor can represent a specific financial calulations such as protfolio valuation, risk analysis, or performance mesaurements
- XML/Json processing: perform differnt operation on data extraction, validation or transformation
- Document Converters: In a document conversion system, when doc need to converted between different
  formats, eg pdf to html, a visitor pattern can be employed to travserse the doc elements and perform the necessary conversion operations.
- Network protocols - process different network pattern, each represents a specific protocol
  operations, such as packet decoding, encryption and compression.
- Game Developments: utilized to Implemnts different gameplay-related operations on game entities
  such as collision detection, artificial interligence decision making or rendering effects.
- Medical Information system: perform operations like data analysis, diagnosis, or patient
  record processing on various medical data elements, such as symptoms, test result or medical
  history

# Terminologis

- Visitor: This is interface or an abstarct class that define the visit methods corresponding to each elemnets type in the object stucture each visit methods represents a specific operation need to
  performed on the elements. concreate visitor class implements this visit methods to provide the actual Implemnation of the the operations.
- ConcreateVisitors: it implemnts the visit methods define how operations are performed on the elements.
- Elements: it define the accept methods, it take visitor methods as parameters and allwo visitor to
  access the Internal state of the elements. each concreate elements class Implemnts the accept methods, enabling the vistor to visit and perform operation on the elements.
- concreateElements: accept methods provide access to its internal state. it allow the vistor to visit and operate on the specific elements.
- ObjectStucture: This allow collection of hierachy of elements that visitors operates on. the obejcts stucture typically provide a way to access the elements allowing visitor to traverse and
  perform operations on Them.

# Why shoudl i use it?

- when you have a complex object stucture with fixed set of classes and you want to define a new
  operations on those classes without modifyning there implemnation. The visitor patterns allows
  to add new operations by defning new visitor classes.
- when you have set of related operations that need to be perfomed on differnet type of objects
  and these operations depends on type of objects. the visitor pattern allow you to encaptulates
  the operations in visitor classes and dispatch them based on the type of objects.
- when you want to seperate the logic that operates on an object stucture from the objects themselves. the visitor pattern acheive this seperation by introducing visitor classes that can
  visit and operate on the elemnts of the object stucture.
- When you want to avoid polluting the object classes with method that are not directely realted
  to their primary responsibility. the visitior pattern keep the operations seperate by defning them
  in vistor classes.
- when you need to perform operation on object stucture that are not known during the design phase
  and may vary dynamically at runtime. the vistor pattern allow you to add new visitors without modifying the exiting elemnents or their stucture.

# advatges

- seperation of concrerns
- Extensibility
- open/closed principle
- Improved maintanability
- Double Dispatch - appropriate method is selected based on both visitor and the elemnets being visited
- Incresed complexity
- Object Hierachy and coupling
- Limited access to Elemnets state
- Difficulty in adding new elements
- performance overhead
