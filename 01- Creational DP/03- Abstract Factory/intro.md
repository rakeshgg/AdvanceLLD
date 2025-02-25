# Abstract Design Pattern

- is a creational design pattern that provide interfcae for creating famlies
  of related dependent objects without specifying there concrete classes.
- It seperate the process of creating objects from the actual Implemnation
  of Those objects, allowing for greater flexibility and ease of modification
- It is often use when system should be independent of how its products are created
  composed and represented.
- It is similar to Factory methods only that it creates groups/ families of realted
  objects Intead of single objects Like Factory methods.

# Real word use case of Abstarct factory Design

- GUI Toolkits: GUI toolkits such as QT and GTK use the abstarct factory design pattern to create
  widgets for differnt platform (window, mac, linux) The Factory creates the appropriate widget based on the platform it is runing on. allowing the same codebases to be used across different
  platforms.
- GameEngine: GameEngine use the Abstarctfactory pattern to create objects such as characters
  weapons, and levels. The factory create objects based on the game setting. allowing the same
  codebase to be used for different type of games.
- DatabaseConnections: application that need to connect to differnt types of databases use the
  Abstarct factory pattern to create the appropriate database connection. The factory creates
  a connection based on the configuartion setting, allowing the same codebase to be used differnt
  type of databases.
- DocumntGenerators - diffenrnt type of docs html, pdf etc
- Automobile manufaturing: use to create differnt type of vechiles, cars, truck, buses on the
  same production line. the factory creates appropriate vechiles based on customer order. allowing for effiecient productsion and customization.
- PaymentGateway - use to create differnt type of payemnt methods credit card, netbanking, debitcard
  for differnt countries. the factory creates appropriate payemnts menthods based on customer location, allowing for seamless payemnts across differnt countries.
- LoggingFrameWork: create differnt type of loggers, console, file, database depending on requirements of the application.

- Builders: Builders use AFD to create differnt type of building (houses, apartment, commercial building) based on the requirements of the clients. the factory create appropriate building based
  on the client need allowing for effiecient cunstruction and customization.

# Terminologies for AFDP

1. Abstarct factory: This is the interface or absatrct class that declares methods for
   creating the products. it provide common interface for creating objects of various type
   within a family.
2. concreteFactory: these are concrete implemenation of absatrct factory. each concrete factory
   is responsible for creating a specific family or related products. Concrete factories implemnts
   the methods declares in the abstract factory.
3. AbstarctProducts: This is the interface or abstract class that declare the common methods
   that the products within the family must implement. the absatrct product defines the contracts
   for all the products in a specific Family.
4. ConcreteProducts: These are the concrete Implemnetaion of absatrct products. each concrete
   products corresponds to a specific type within a family. Concrete products implement the methods
   declared in the absatrct products.
5. ProductFamily: refer to a group of related products that are created by the some concrete Factory
   each product family typically consists of multiple concrete products that share the common theme
   or purpose.
6. FactoryHierachy: In some cases, the AFDP can have of hierachial stucture, where there may be
   an abstarct factory that define common methods or provides default implemnation. and than multiple
   sub-factories that inherit from the abstract factory and provide sepcialized Implemenations for
   different product families.
7. Client: The client is the code and Components that use AFP. it interact with abstratc factory
   and abstraact product classes to create and work with the products. the client code remain
   unaware of the specific concrete classes and Implemnation details.

# Factory Vs Abstarct Factory

Purpose:

1. Factory Method Design pattern: focus on creating objects with specific class Hierachy
   it provides an interface for creating objects, allowing subclasses to decide which concrete
   class to instantiate.
2. AbstarctFactory Design: familes of related dependent objects. it provide an interface for
   creating families of related objects without specifying their concrete class.

Object Creation:

1. Factory Method Design pattern: it provides methods in a base class (or interfaces)
   that subclasses can override to create specific instances of a class. Each subclass
   of factory decides which concrete class to instantiate.
2. AbstarctFactory Design: provides set of factroy methods or an abstract factory class
   with multiple absatrct methods. each factory methods create a specific object or a family
   of related objects.

Relationship between objects:

1. Factory methods Design pattern - client code depend on base class or interfcae and interact
   with the created objects through the common Interfcae
2. AbstarctFactory Design: create families of obejcts with specific relationship. the client
   code depend on absatrct factory or set of factory methods to create objects and interact with them
   through there common interfcae.

Scope of variations

1. variation with single class hiearcies, each subclass of the factory can introduce new variation
   by Implemenating the factory methods.
2. variation across mutiple class hiearcies, or families of objects. Each concrete factory represents
   a family of related objects and can introduce new variation by Implemnting the factory Methods.

Granularity:

1. it operates at the level of individual objects and their instantiation, it provides
   to create obejcts one at a time
2. it operates at higher level and provides a way to create a familes of obejcts. it provides
   a way to create Multiple realted obejcts together.

# Advatages and Disadvatages - AFDP

- Encourages Loose coupling - client unware of concete class
- sipport product family creation
- provides consistent interface - only work if abstact details
- Enable easy swapping of implemnation - change concrete class
- Facilitates extensibility - easy to make new families of objects by creating new
  concrete factories.

# Disadvatages

- Increased complexity
- Limited Flexibility in adding new product type
- Increased code duplication
- Tight coupling betwen factory and product
- Limited runtime flexibility

# Things to Note

1. Define absatrct interfaces - create abstract interfaces (abstarct base classes or ABCS in python)
   for the product and factories. these interfaces should declare the methods that concrete products
   and Factory classes must Implemnts.
2. Implemnt concrete product classes.
3. Implemnt concrete Factory classes
4. Use Dependency Injection or configuarion - client code not depend on Concrete class depend on interface and receive concrete factory instances.
5. Encourage adherence to Liskov Substitution Principle(LSP)
6. consider using a registery or configuartion files.
7. Aim for High cohesion and Low coupling
8. Follow naming Conventions
9. Document the purpose and responsibility of each class
10. Test Thoroughly
