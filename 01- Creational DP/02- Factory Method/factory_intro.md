# Factory methods and Introductions

- It provide and Interface for creating an objects but allow subclasses to decide
  which class to instantiate. its types of oops patterns that promotes loose coupling
  and adheres to open closed principles. which states classes shoudl be open for
  Extension and closed for modification.
- The factory design pattern is useful when you want to delegate the reposibility
  of object creation to subclasses. rather than having base class directly create
  objects. This allows for greater Flexibility and Extensibility. as new subclasses
  can be added without modifying the existing code.
- By using the Factory method pattern, you can encaptulates the object creation Logic
  within subclasses, providing the consistent way to create objects while allowing
  for flexibility and customization. this pattern is often used in FrameWorks and
  Libraries where the excat objects type needed is determined by the client
  code at runtime.

# Real Word use Cases

1. Document processing: text editors or documnt processing software often use the Factory
   Method pattern to create different documnt types, such as word documnts, PDFS, HTML Files.
2. Logging FrameWorks: Logging FrameWorks Utilizes Tha Factory method pattern to create different
   loggers based in desired output formats. such as console loggers, file loggers, or database loggers.
3. Databaseconectivity: database connectivity libraies may Employ the Factory method pattern
   to create specific database connection objects for differnt database vendors, like mysql,
   PostGreSql, or Oracle.
4. GUI Component Libraries: GUI Frameworks use often to create various UI components such as
   button, text fields, checkBoxes, based on platform specifc requirements.
5. ObjectSerialization: Serailalization Libraies levarage The Factory method pattern
   to create serializers, for different data formats, such as JSON, XML, or binary
   Formats.
6. PayemntGateways - it use to create instances of differnt payemnts Gateway classes
   based on the selected provider, such as paypal, stripe, braintree.
7. Maze Genartion Algorithums: to create different maze obejcts instances with various stucture
   such as simple mazes, randomize mazes, or maze with specifc patterns.
8. VechileManufaturing: create differnt type of vechiles, such as car trucks, motercycle,
   based on customer requiremnts.
9. Plugin System: Software plugin use this pattern to create instances of plugin objects
   based on user selection or dynamically loaded plugins.
   10.GameDevelopemnts: Game Developments framework may used the factroy method pattern to
   create different game obejcts. such as characters, weapons, or power-ups based on game logic
   or user input.
   1

# Terminology:

A. Products: refer to abstarct base class or interface that define the common menthods
and properties that all products (objects) created by Factory will have.
B. ConcreteProducts: These are concrete classes that implemnts the product Interfcae.
Each concrete product represents a specific variations or type of obejcts
that can be created by the Factory. => product interfcae
C. Creator: it is abstract base class or interface that declare the factory methods
it provide the contract of creating objects. but doesnot specify the concrete class
it may also contains other methods that operate on the products.
D. ConcreteCreators: These are concrete classes that inherit from the creator and implements
tha Factory methods. each concrete creators is responsible for instantiating
a specific concrete product class.
E. FactoryMethods: it is an abstract methods declared in the creators that define the contracts
for object creation. subclasses of the creator implemnts this method to create instances
of concrete product classes. The factory method is resposnible for deciding which
subclass of products to instatiate.
F. Client: The client use the FactoryMethod to create obejcts. it interact creator through abstarct
base class or interfaces. without being aware of concrete classes being instantiated.

# When to Use It.

. Object creation - when you want to encaptulates the object creation Logic
in a seperate component or class. The fcatory method patern allows you to
delegate the responsibility of object creation to subclasses or specilaized
Factory classes.
. Decoupling - When you want to decouple the client code from specific classes
it creates. by using the Factory method pattern, the client code can interact
with the abstract factory interfcae ans is not directly depend on
concrete Implemenations.
. Extensibility - when you need add or modify types of objects created without
modifying existing client code. the factory method provide an extension point
by allowing the addition of new subclasses or factory classes without impacting
existing code.
. Variation in object creation: when there are multiple variations or configurations
of objects that need to be created. The factory method pattern allows different
subclasses or factories to provide the specialized Implemenation of object
creation based on specific criteria and requirements.
. Testing and Mocking

# Advatage and Disadvatage

. Encaptulation - encaptulate objects creation logic in a seperate components and class
it promotes a more modular and organized code stucture.
. Flexibility and Extensibility - easy addition or modification of object types without
modifying the existing client code.
. Dependency Inversion: it promotes dependency inversion by allowing client code
to depend on absatrction rather than concreate Implemnation
. Code reusability: by providing a consistent and reusable mecanisum for creating objects.
it avoid dupliacte object creation logic throughout the code base.
. testing and mocking

# Disadvatages

. Complexity - sublcasses and multiple factory classes delaing with large number of objects types
. Increased number of classes
. Indirection - Fcatory method pattern introduces an additional layer of indirection between
client code and object being created. this can make code more abstarct and required depper
understainding of the underlying object creation process.
. RuntimeOverhead - dynamic object creation, additional class
. Tight coupling with Factories

# Things to Note

- Abstarction - define absatrct base class or interface that represents the
  common interface of all products created by the factory. this absatrction
  shoudl declare the factory method that subclasses or specilaized Fcatory
  classes will Implement.
- Concerete Implemenation - concrete class represents specific products that
  factory can create
- Fcatory class - Enacaptulates the objects creation logic. the factory class shoud
  define the factory methods as a static or a class methods. this method should create
  and return instances of desired product based on clients request or specific conditions.
- client code - interact with factory through factory method
- Extensibility
- Dependecy Injection
- Error handaling - you can choose to raise excetion or return a default objects
  or implemnt a fallback strategy based on the specific requiremnts of your application
- naming Conventions - choose menigful name of your class and methods.
- Documentation and comments
