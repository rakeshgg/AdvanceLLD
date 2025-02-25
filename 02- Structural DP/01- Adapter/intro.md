# Adapter Design pattern
# Intro

1. ADP is a stuctural pattern that allows object with incompatible interfaces
   to work together by creating an intermediate adapter object. The adpater
   object translate the interface of an object so that another object can
   understand it.
2. In other words adpater pattern helps to convert the interface of one class
   into the interface expected by the client. this pattern involves creating
   an adpter class that acts as a wrapper around existing class. providing
   different interface to the client without modifying the underlying code
   of the original class.
3. The adpater pattern is useful in situations where you have existing code
   that cannot be changed or modified but needs to be intergrated with new code
   or systems. by creating an adpater, you can make these two system work together
   without the need for extensive refactoring or rewriting the code.

# Real word use case
1. Power Adapter: Adapters used to convert power plugs from one country to another
   are a common example of the adpater pattern. These adpater pattern provide a way
   to convert the interface of an electrical device to the interface of different
   electrical socket.
2. USB to Serial Port Adapters: USB to serial port adapters allow devices that only
   have a serial port to connect to a computer via USB. This adpater acts as a
   wrapper that transalate the serial port interface into a USB interface that the
   computer can understand.
3. Audio Adpaters: Audio adpaters are used to convert the interface of audio device
   to different connectors or formats. for example a sterio mini jack to RCA adapter
   can be used to connect a smartphone to a home sterio system.
4. Database Adpaters: Database adapters provide a way to connect to a database system
   using a differnt interface than the one that the database system supports. This can be
   useful when working with legacy system or when migrating data from one system to another.
5. language Transalators: Language transalators can be seen as an example of the adpater
   pattern as they provide a way to transalate the interface of one language into the interface
   of another language, allowing people who speak differnt language to comnuicate.
6. Printers - Printers often required adpaters to connect to differnt type of computer 
   device, such as USB to parallel port adapters. these adpaters provide a way to convert
   the interface of the computer to the inertafce of printer

# Terminologies
1. Target: This is the interface that the client code uses to interact system the target define
   the methods that the client code can call to achieve the desired functionality.
2. Adaptee: This is the existing system that needs to be adpated to work with the target
   interface. The adpatee has the different interface than the target, and the client code
   cannot use the Adaptee directely.
3. Adpater: This is the class that adapt the adpatee to the target interface. the adpater
   Impleemnts the target interface and uses an insatnces of the Adaptee to provide the desired
   functionality.
4. Client: This is the code that uses the target interface to interact with the system. the client
   code is unware of the adpatee and the adpater, and only interacts with the target interface.

# When should we use the adpater pattern
- when you want to reuse the existing code that has a different interface from what you need
- when you have a class with a complex interface that is difficult to use, and you want to
  provide a simpler interface
- When you want to create a class That can work with Multiple classes That have different 
  interface, but perform the same task.
- When you want to create a class that can work with future classes that have different
  Interface, but perform the same task.
- In summary the adapter pattern is useful when you want to use and existing class,
  but its interface is not compatible with the interface you need. you can use the
  Adpater pattern to provide a wrapper class that adapts The interface of the existing class
  to the interface you needed, without modifying the exiting class.

# Advatages and Disadvatges
- Flexibility: The adapter pattern provides a way to adapt the interface of an existing class
  to the interface required by the client code. This makes it possible to use exiting code
  that was designed for a different interface without modifying that code.
- Reusability: The adapter pattern allows you to reuse the exiting code, even if it has a
  different interface from what you need. you can create an Adpater class That adpats
  the interface of exiting code to the interface you need, and then use the adpater class
  in your client code.
- Maintainability: The adpater pattern makes it easy to maintain the exiting code, if you
  need to change the interface of an existing class, you can create a new adapter class
  that adapts the new interface to the old interface. This way you can avoid making
  changes to exiting code.
- Scalability: The adapter pattern allows you to create a class that can work with
  multiple classes, that have differnt interface but perform the same task. this makes
  it possible to create scalable solutions that can handle future changes in the system.
- Simplification: The adapter pattern simplifies the client code by providing a simplified
  Interface to the exiting code. This make easier for the client code to use the exiting
  code.
- Performance: The adapter pattern have a negative impact on performance, especially if adapter
  class needs to perform the complex operation to adapt the inertafce required by the client
  code. This can result in slower execution times and Increased resource usage.
- Maintaince - While adpater pattern make easier to maintain existing code. it can also
  make code more difficult to maintain, if there are multiple adapter class Involved
  if you need to make changes to the exiting code, you may need to modify multiple adpater
  classes.
- Dependency Inversions: The adpater patetrn can voilates the dependecy inversion principle
  which state that high level module should not depend on low level module but should depend
  on abstarctions. In the adapter pattern the client code depends on the Adapter class, which in
  turn depend on the existing code. this can make harder to write testeable and modular code.

# Things to Note
- Choose the right type of Adpater: There are two type of adapter patetrns object adapter and
  class adpater. object adapter are used composition to adpat the interface of the exiting class,
  while class adpater use multiple inheriatnce. In python it is generally use object adapters,
  since multiple inheriatnce can be more complex.
- Use Interface or abstarct classes: to ensure that your adpater class can be used with multiple type
  of classes, it is good idea to use interface that your adpater class can implemnt, even if The classes you are adpating have differnt interfaces. 
- test adpater class throughly
- keep adpater class simple as possible: the adpater class shoul only responsible for adpating
  the interface required by the client code, and should not perform any other tasks.
- Follow the naming convention - XyzAdpater, method request adpats request


