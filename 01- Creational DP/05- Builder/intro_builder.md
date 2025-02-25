
- It's a creational DP, used to create complex objects step by step and allow
  you to produce different types and represenation of objects using the same
  construction code.
- main idea is seperate the construction of complex objects from its representation
  same construction process can create different represenation of objects.
# used when
- Builder pattern is useful only when you have to create objects with a large
  number of optional parameters.
  as it allows you to specify which parameters to use and in what order, without
  creating multiple construction signature.

# Real word use case
a. Document creation application: In application that generates documents, such as
  PDF, HTML files, the builder pattern is used to create different documents type
  and styles.
b. Gui Creation: In GUI is used to create complex user interface with different layouts
                 options and controls.
c. Meal ordering system: In resturant or food oredring system builder pattern is used to
                          create complex meal orders with differnt options, such as topping
                          types and beverages.
d. car manufacturing: builder pattern is used to create cars with differnt
                     options and configurtions such as engine size, color and features.
e. WebsiteCreation: builder is used to create differnt types of webpages, with differnt layout and contents.

f. Gamelevel Design: builder pattern is used to create differnt levels with differnt enemies
                   obstacles and power-ups.
g. DatabaseQuery: The builder pattern is used to genrate SQL queries of differnt parameters
                  options and commands.

# Important Builder classes
A. product: The complex obj to constructed. it has multiple parts and required step by step
            process to constructs. this could be any objects like database query, game, network,
            website etc.
B. builder: an abstarct interfcae that define step required to build the objects. it declares
            methods for creating and assembling parts of the products.
C. ConcreteBuilder: provide Impelementation of builder methods. it defines and keep track
                    of the represenation it creates.
D. Director: class that controls the constrution process. it knows which builder to use
             and what order to call builder methods to create products.
E. Client: A class module that use the builder pattern to create the products.
           it is responsible for creating the director obejcts. and configuring it with
           the appropriate builder. the client can also work directely with the builder
           if it need more controls over the construction process.
 


# class Instaintiation
class House:
   def __init__(self, floor, wall, roof)

# Direct Initialization Issue
- Complex construction signature: when class has multiple attribute or optional params
  the construction signature can become long and hard to read. it may challenging to remember
  order and meaning of each parametrs. leading to potential errors when instatinating the class.
- Limited Flexibility: you need to provide value during obejct creation, limit flexibility.    especially delaing with optional and default values.
- code redability and maintainability: harder to maintian the code all construction logic
  is centeralized within the constructors. it can result in bloated and tightly coupled code.
  making it difficult to modify or extend the class in future
- Lack of Encaptulation: The direct instatiation approch exposes the internal stucture and dependecies of class to the client code. The client need to know the specific order and meaning of construtor parms. which breaks encaptulations. changes to the class internal stucture or constructor signature may require modification to the client code. leading to coupling and potential bugs.


# when to use Builder Design Patterns
- When you need to create complex objects that have multiple parts or
  properties, with different value or combinations
- When construction process involves Multiple process or steps or dependecies
  that need to be resolved or configured dynamically.
- When you want to isolates the construction codes from the rest of code base
  or clients. to Improve modularity and maintainability.
- When you want to support Multiple represenations or variants of the same obejcts
  without duplicating the construction Logic.
- When you want to construct obejcts using a fluent or redable sytax That
  allow you to chain multiple methods call and set differnt options and 
  properties.

# Advatage and DisAdvatages
- Decouples an abstractions from its Implemenation so that two can vary Independetly
- Improve extensibility by allowing new Implemenation to be added Easily
- Reduces the number of subclasses that need to be created for both The absatrction
  and the Implemenation
- Provides the way to switch between differnt Implemntaion at Runtime
- Increse the Flexibility and reusability of code

# Disadvatges
- Increses the overall complexity of the code by Introducing a New Layer of Abstarctions
- can make the code more difficult to understand and maintain due to added complexity
- can lead to performance overhead due to extra layer of indirection.
- can make the code harder to test beacuse of added layer of abstarction
- It's not always the best solution for all problems, its Important to Evaluate
  it its best pattern for the particular problem you're trying to solve.

# Things to Note Builder in Python
- Python Provides several ways to define and initialize obejcts, such as object
  literals, keyword arguments, and data classes. The builder pattern is not always
  necessary or best solution for Every situations.
- Python allows optional and defualt args in function and method defination
  which can simlify the builder Interfcae and Implemenation. Instead of defing
  seperate methods for each optional parts, you can provide default values or
  use keyword args.
- python flexible sytax and dynamic typing make it easier to create a Fluent interface
  for the builder. where each method return the builder objects itself. this allow
  for more redable and consise construction process.
- Python support for decorators and metaclass can be used automatically genrate
  the builder class or its methods, reducing boilarplate code and reducing
  maintainability.
- Python dynamic nature also make it harder to enforce type constarints and
  ensure the consistency of the obejcts being built. you may need to use
  additional tools or libraries, such as type annotaion, type checkers
  or schema validators, to ensure correctenss and prevent runtime Errors.


  