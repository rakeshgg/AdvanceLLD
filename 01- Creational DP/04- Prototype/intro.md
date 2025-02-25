# Prototype

1. The prototyps patetrn is a creational pattern that creates new objects
   by copying existing objects. rather than creating new obejcts from scratch
2. This can be useful when creating new object is computationaly expensive
   or when creating new objects required lot of complex configurations
3. The prototype pattern involves creating a prototypes object, and making
   copies of that object needed.

# RealWord use case:

1. Graphic design tools: application like adobe photoshop or illustrator often use
   prototype pattern to create copies of graphics object such as shapes or Images,
   to be edited independently.
2. CodeEditor/ IDES: Code Editors are integrated Developemnts environemnts often leverage
   prototypes pattern provide code snippets or templates that can be cloned and customized
   for differnt programing senarions.
3. GamingEngines: game developemnts framework or engines such as Unity or Unreal Engine
   can use the prototype pattern to create copies of game entites. charcters or object
   during gamePlay.
4. 3D modelling software: Application like autodeck maya or blender can benifit from
   the prototype pattern by allowing the creation of dupliacte 3D models for modification
   or reuse.
5. Virtual machine managemnts: like VMWARE, virtualBox, can utilize the prototype pattern
   to clone existing virtul machine configurations to create new instances.
6. E-commerce Platforms: it may employ the prototypes pattern to create copies of product
   templates or configuartions. allowing retailers to easily add customize new products.
7. Document Generation: generating documnts such as PDF, reports, can use prototype
   pattern to clone and modify existing documnt templates with specific data or formatting
8. WebPage template system: web dev framework or content managemnt system often employ
   the prototype pattern to create copies of web page templates that can be customized
   for differnt sections or purposes.
9. CAD Software: AutoCAD, solidWork can utilize the prototype pattern to clone and modify
   existing design for faster creation of new models
10. SpreadSheet Application: SpreadSheet application like microsoft Excel or Google sheet
    can use the prototype pattern to duplicate and modify existing spreadsheet templates
    or formula for differnt data analysis tasks.
11. Document managemnt system: The prototype pattern is used to create new documnts
    from a prototype documents to save time and efforrts

# Terminologies

1. Prototype: it is an interface or absatrct class that declares the methods for cloning itself.
   It act as a blue-print for creating new objects.
2. ConcretePrototype: concrete implemntion of prototype interface It provides cloning Implemenation
   and define the specific properties and behaviour of the object to be cloned.
3. Clone: method to define prototype interface that allows creating a copy or clone
   of an exisiting objects. the clone method typically performs a shallow or deep copy of
   the object state.
4. Shallow copy: only top level of properties of an object are copied. while the refernce
   to nested objects are shared between the original and cloned objects.
5. Deepcopy: it is a type of cloning where both the top level properties and
   nested objects of an obejct are copied creating independet copies of all the
   object components.
6. Client Specific Modification: it refer to customization or modifications made to the
   cloned obejects after it has been created. these modification allow the client to tailor
   the cloned object according to its sepcific requiremnts
7. Registry or Prototype mangers: it is an optional components that maintains a registry of
   prototype objects. It provides a centreal place for storing and retrieving prototype
   objects. making it easier for clients to acess and clone Them.
8. Client: it has entity that use the prototype pattern to create new objects. The client
   interacts with the prototype interface to clone objects rather than creating them
   directely

# Advatages and Disadvatages

- you need to create objects that are similar with slight variation in there properties
- you want to avoid cost of creating of new objects by cloning exiting ones.
- you want to hide the complexity of creating new objects from the client
- you want to easily create new objects with complex Initialization Requiremnts
- You want to create a template from which other objects can be drived

Advatages

- Reducing the cost of creation of new objects : save cost of creating new objects from scratch
- Improving the Performance of the Application: expensive operation, prototype can Improve the
  performance of the application by reducing The time needed to create new objects.
- Encaptulating object creation: the prototype patterns encaptulates the process of creating
  new objects, which make code more maintainable and easier to understand.
- Simplifying object creation: you can simplify the process of creating new objects
  since you can create new objects by modifying the propertis of an existing objects.
- Allowing for dynamic object creation: obj created at runtime by cloning exiting ones
  This can be useful in scenarios where the number of type of objects needed is not known
  at compile time.

Disadvatges

- Increased Complexity - if obj being cloned is itself complex
- object identity - not same identity after cloning This can cause issue if the application
  relies on object identity
- shallow vs deepcopy: shallow copy creates a new objects with reference to the original objects
  properties. while deep copying creates a new objects with new copies of original objects properties
  The choice between deep and shallow copy can effect the behaviour of the application and can be
  difficult to manage.
- managing prototypes is complex
- Securrity issue - cloned senstive data and functionality

# Things to Note

- When Implemnting prototype design pattern GHenrally and python

1. Cloning can be Expensive: depending on size and complexity of obejcts being cloned
   cloning can be costly operations you should consider wheather benifits of cloning
   outweigh the costs.
2. Be aware of shallow copying and deep copying
3. prottype object should be thread safe - in multithreaded environemnts, it is important to
   Ensure that the prototype objects are thread safe to avoid concurency issues.
4. keep the prototype registry organised
5. be aware of obejct identity
6. Avoid sharing Mutable objects - if any change will shared among all the cloned objects
   yu can use Immuatble objects or make defensive copies of mutable objects when cloning.
