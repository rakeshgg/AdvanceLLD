# Singelton Design patterns

- Singelton design pattern is a design pattern that ensure a class has only one instances
  and provide a global point to access to it.
- It is often used for objects That need to be shared across the entire application
  such as logging database connection and configuartion settings.
- the basic implemenation of singelton pattern involves creating a private constructors
  a static instances variable and static methods that return the instances.
- the instance is created first time the method is called and all subsequnt
  calls return the same instances.
- This ensure that only one instances of the class exists, while still providing a covinet
  way to access it.

# Real Word use case

1. Database connections: A singelton class can be used to create a singelton connection
   to a database. This ensure that only one connection is open at a time, which can help
   to Improve performance and reduce the risk of connection errors.
2. Logging: A singelton class can be used to create a single instances of a logging class
   This ensure that all log messages are written to the same file or stream, making it easier to
   read and analyze the Logs.
3. Configuration Setting: used to store configuration wide setting. this ensure that all part of
   application use the same settings and allow for easy updates and managements of the settings
4. ThreadPool: A singelton class can be used to manage a pool of threads. this ensure that
   only one instances of thread pool exists, and that all thread are managed by the same obejcts.
5. Caching: it is used to store data in a cache. this ensure that all parts of application use the
   same cache and allows for easy management and eviction of data.
6. Event manager: A signelton class can be used to manage events in the application this ensure that
   all event are handled by the same objects and that event are handled by the same objects and that
   events are handled in a consistent and predictable way.

Few example of singelton pattern used in real life key advantage of this patterns is
to ensures a single instances of a class is used throughout the application which can Improve
the performance, simplify code and reduce the risk of errors.

# Terminologies

1. Singelton: The singelton class itself, which insures that only one instnaces of the class can
   be created and provide the global point of access to that instances.
2. Instances: The single object created by the singelton class. It is the sole Instance
   of the class that is shared and accessed by differnt part of code.
3. getInstances(): a static method of singelton class that provides access to The single instances
   It creates the instances if it doenot exit. or return the esiting instances if it has already being created.
4. \_\_instance : A private static variable within the singelton class that holds the single instances
   it is typically a class-level variable that is shared by all instances of the class.
5. init() - private constructor methods of the singelton class. it ensures that the class cannot
   be directely instantiated by external code. instead getInstances() method shoule be used
   to obtain the instances.
6. Lazy Initialization: The approch of creating the instances of the singelton class only when it is first requested, rather than creating it eagerly. this can save resource if the instances is always
   not needed.
7. ThreadSafety: Ensuring that the singelton pattern work correctely in a multi-threaded envirnonemnts where multiple thread may attempt to access the getInstances() method concurently
   Proper sysncronization mecanisum are used to prevent race conditions and gurantee the creation of
   single instances.

# Things to Note:

1. In Python, one specific drawback of the singelton pattern is that it may not work correctly
   in a Multi-Threaded envirnoments. python global Interpreter Lock (GIL) ensures that only one
   thread can execute python bytecode at a time, so using a singelton pattern may not provide
   any actual concurency benifits.
2. Another drawback is that, python is dynamic language and its classes are not closed after creation
   and can be modified at runtime. this means that it is possible to change the behaviour of singelton class, which can cause unexpeted side effects.
3. However singelton pattern is useful in python for creating objects that need to be shared across
   different part of code bases such as database conenction, chache or logger, it can also be useful
   for controlling access to shared resources and for Implementing Global state.
