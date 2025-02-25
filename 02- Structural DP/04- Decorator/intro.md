# Decorator pattern
- Coffee with toppings: add dynamically
- Text Fomrating: bold, itlaic, font color: add text dynamically
- Car Customization: leather sheet, sunroof, navigation system
- Cake decoration
- user authenntication: add auth check to application objects
- Logging: log different error, etc

# Terminologies
- Components: refer to interface or absatrct class define common method implemented by concrete
  class and decorators
- ConcreteComponents
- Decorator
- concretedectorator: add aditional functionality
- client

# When to use it
- Adding responsibility dynamically: decorator allow you to attach new behaviours to objects at runtime. this is useful when you want to add the functionality to object incrementally and flexible
without subclassing.
- Open closed principle: it allow yu to extend the behaviour of a class without changing the source code
- Avoiding a class explosion: Instead of creating a large number of classes to handle all possible
  combinations of behaviours, you can use the decorator to mix and match the functionality as needed
  this reduce number of class in your codebase.
- Component  based system: decorator are commonly used in component based artitecture auch as GUIS
  where you can add feature like border, scroolbars, and tooltipl to grpahical elements.
- Logging and profiling: you can use the decorators to add logging and profiling functionality to methods and functions without modifying there core logic. this is used for debugging and performance
analysis.
- caching: you can chache the result of expesnive function calls to improve performance
- Authentication and Authorization: you can decorate methods and endpoints to add authentication
  and authorization checks without cluttering the core logic of your application
- Input validation: decorators can validate Input parameters to ensure that they meet certain criteria before allowing method to execute. help robutness of your code
- Resource managemnts: Decorator can be used for resource managements, such as opening and closing
  database connection, file handling and managing transactions.
- Localization and internationalization: for multi-language application decorator can modify the text
  or content diplayed to users based on their preferd language or locale.
- Security - encryption, datavalidation
- Dependency injection -used to inject dependency into classes or functions, making it eaisr to test
  and change the behaviour of components.
- Cross-cutting Concerns: when dealing with cross cutting concerns like logging error handling
  and performnace monitoring decorator can help keep these concerns seperate from core business logic
# advantages
- openclosed priciple
- Single responsibility principles
- Flexibility and Extensibility
- Easy to maintain
# disadvatage
- Complex code
- Performance overhead
- Dependency Injiection
overall it useful pattern for modifying the behaviour at runtime. however its usages
should be carefully considerd to ensure that it doesnot result in complex or inefficient
code.

# Things to Note:
- The decorator function or class should have same signatures as the function or class its decorating
- Decorator can be stacked on top of each other to add multiple behaviours to the original function
  or class.
- Decorators can be applied both function or class
- decorator should not modify original function or class. Instead they should return a new object
  that has the added functionality
- The decorator function should return a callable object (function, class, or methods)
  that can be called just like a original objects.
- 