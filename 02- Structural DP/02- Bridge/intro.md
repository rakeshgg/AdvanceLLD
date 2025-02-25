# Bridge design pattern:
- The bridge pattern is a design pattern used in oops that aims is to decouple 
  an abstarction from its Implemnation, allowing both to varry independetly
  it involves creating two seperate hieracies of classes, one for the abstarction
  and one for the Implemnation, and then connecting them through a bridge objects.
- The main idea behind the bridge pattern is to seperate an abstraction (such 
  as an interface, abstarct class or API) from its Implemenation (The actual code)
  That provide the behaviour. by doing so changes to either absatrction or the
  Implemenation will not affect the other, making the system more flexible and 
  easier to maintain.
- Bridge pattern typically involves creating an abstarction class or interface
  that defines the methods and properties That client will use and then Implemnting
  That absatction In a concrete subclasses or classes that provide the specific
  behaviour. The abstraction class will than use an instances of the Implemenation
  class through a bridge objects to perform the desired behaviour

# Real word use case:
1. Graphics design software: it use the bridge pattern to seperate absatrction of
   a shape or objects from its Implemenation. for eg, a rectengle can be defined
   as an abstraction, and its Implemnation can be differnt type of rectangles.
   such as filled or unfilled, with differnt colors, line thickness and so on.
2. Audio and video streaming: streaming services such as Netflix or Youtube use the
   bridge pattern to seperate the abstraction of the user interface From its 
   Implemenation using different technologies, such as HTML5, Flash, or native 
   applications on differnt platforms.
3. Operating system: use the bridge pattern to seperate the absatrction of the user
   Interface from its Implemenation. for example the UI may Implemented using differnt
   window system, such as x11 or wayland on different platforms.
4. Database management system: dbms use brideg pattern to seperate absatrction of 
   query language from its Implemantion. for example the query language may be Implemented
   using differnt database engines such as MySQl, PostgreSQL, or Oracle.
5. RemoteControlDevice: Remote control device use the bridge pattern to seperate
   absatrction of user interface from its Implemenation. for example a remote control
   have different buttons and layout it cotrols. such as TV, DVD player, or streaming
   devices. The absatrction is the same (a remote control) but the Implemnation varies
   based on device it controls.
6. WebApplication FrameWorks: to seperate the absatrction of user interface from its
   Implemenation. for eg, a web application Framework may use differnt rendering engines
   such as HTML, CSS or Javascript to generate the UI.
7. Robotics: robot behaviour from its Implemantion, behavour may be Implemnted using differnt 
  control algo such as proportional-integral-derivatives (PID) control or reinforcements 
  learning.
8. Game Developments: game obejct from there Implemnation, a game engine can define absatrct
   game obejct class and then Implemnt specific game objects such as charcters, enimies,
   or items, that inherit from that class.

Example 

- A colored Shape
  - Shape is the absatrction - the main object to create
    - Circle(Shape), Square(Shape)
  - Color is the Implemnation - attribute to define the obejct
    Red(Color), Blue(Color)
  - Line is also an Implemenation
    A Thick(Line), Thin(Line)
- Create the absatrction with an Implemnation eg. Circle(RED)
  - use the absatrct methods to bridge eg get_color() method to paint 
    the color of the Circle.

# Terminologies
Abstarction: it defines the high level interface of the system and provides a way to access the
      Implemenation details through a bridge object.
Refined Absatrction: it extends the absatrction add more specific functionality ny working with the
      Implemenation objects through the bridge.
Implemenation: it define the interface for the Implemantion object and provides a way for absatrction
      to access them.
ConcreteImplemnation: It Implemnts the interface defined by the Implemnation and provides the actual
      Implemnation for the Functaionality
Bridge: it decouples the absatraction and Implemantion by providing the way for the abstraction to work with the Implemantion objects through a bridge objects.

# when should I use it
- When you have a abstarct class or interface with several Implemnation and you want to
  be able to change the Implemnation at runtime.
- When you want to decouple an abstraction from its Implemnation so that hey can vary
  independetly.
- When you want to avoid permannet binding between an absatrction and its Implemantion
  which can be useful when you want to add or remove Implemnation dynamically
- When you have a complex class hierachy, and you want to avoid the exponetial growth
  of classes that occurs when each class is combined with each variation of another class
- When you want to hide the Implemnation details of an absatrction from clients and provide
  a simpler interface 


# Advatges and disadvages
- Decoupling of Abstarction and Implemnation: The bridge pattern decouples the abstarction
  from its Implemenation, allowing them to vary independeltly. This reduce the complexity
  of system and make it easier to maintain and modify.
- Improved Extensibility: with the bridge patter you can easily add new abstarction and Implemnation
  without modifying the existing code.
- Improved Flexibility: The bridge pattern provides a flexible design that allow you to change
  The Implemnation at runtime. making it easiier to adpat to chnaging requiremnts.
- Improved code reusability: by seperating the absatrction and Implemnation, you can reuse
  the Implemnation in other abstarction and vice versa.
- Reduced Complexity: The bridge pattern reduces the complexity of the system by breaking it
  down to smaller simpler components
- Improved testebaility - by seperating the absatcrtion and Implemnation it become easier to test
  each componect independently.
# disadvatages
- Incresed complexity
- Incresed develpoment time
- Increased code size
- Difficulty in understanding
- potential performance overhead

# Things to Note

- python suppoort for dynamic typing and duck typing make it easy to Implement bridge pattern
  without need of explicit interface or abstarct classes.
- It is important to define the clear absatrctions and Implemnations to ensure that the pattern
  is Implemnted correctly.
- The use of composition if often preferd over Inheritance and Implemnating the bridge pattern
  in python, as it allows for greater flexibility and code reuse.
- consider using context manager protocol with statement to ensure that resource are properly managed
  when working with bridge pattern
- When Implementing with bridge pattern, it is Important to consider the tradeoff between complexity
  and performance and maintainbility. 



