# Facade
- Facade design pattern is is stuctural design pattern that provide a simplified interface
  to a complex subsytem of code, making it easier to use and understand. the pattern involves
  creating a single class, called the facade, that represent an entire subsytem or set of related
  objects. and provide a simplified interface to acess the Functionalities of the subsytem.
- The facade pattern act as Intermediatery between the client and subsytem, shielding the
  client from the complexity of subsytem and providing a unified inteerface for the client to
  access the subsytem functionalities, by using the facade pattern clients can focus on
  using the simplified interface providing by the facade object, instead of dealing of 
  the complexity of underlying subsystem.
- simplify complexity of large system, provide simple and easy to use interface that abstract
  away the underlying complexity. making it eaier to use and maintain the system.

# Real word use cases:
- Operating system API's: an os provide vast range of low-level apis to interact hardware device
  and system resources. these apis are hard and complex to use. making difficult for developers
  to build application. os use the facade pattern to provide simplified apis such as window API
  or POSIX API, that provide a unified interface to access system resources.

- mobile dev Framework - simplified api to access native api
- payemnt Gateways - paypal, stripe, gateway can provide simplified interface
- Media Players - VLC, window, media file and codec, use facade pattern to play seek etc
- Web Developments: framework djnago, ruby acess backend services.

# Terminolgies
Facade: it is simplified interface that provides the access to complex subsytem, system
        it provide a single point of entry to the underlying system. and it encaptulates
        the complexity of the system from the client.
ComplexSubsytem: the complex subsytem is set of classes or components that provide a
        a complex set of functionalities, these classes are typically interdependen
        and they have complex relationship with each other.
Client: object use to interact with Facade

# when to use it
- Define a clear Interface: The facde should provide a clear and consise interface that hides
         the complexity of system. it should not expose unnecessary details of the client.
- Encaptulates the subsystem: the subsytem should encaptulates behind the Facade. client
          should not able to access subsytem directely
- abstarction 
- keep it simple
- use good naming convention - what facade does

# Advatage and Disadvatages
- Simplifies the complex system by provding simple interfcae
- Improves maintainability and reduces coupling: single interface
- promotes loose coupling and abstractions
- Increase reusability

# disadvategs
- can lead to bloaded interface
- Limit Flexibility - fixed interface
- can create performnace issue - if interface not designed properly
- May not suitable for complex system

# Things to Note:
- Declare a clear interface
- Enacptulates the subsytem
- Use abstarction
- keep it simple
- use good naming convention
- test the facade Throughly


