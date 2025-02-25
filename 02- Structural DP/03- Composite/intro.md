# Composite Design pattern
- allows client to treat individual objects and group of objects uniformally
  it is used when we want to represent the hierarchical tree-like stucture 
  of objects, and we need to perform the operations on them as single object
  or group of objects.
- we have a component interface that define the common methods that can be performed on
  both individual objects and group of objects. the componect interface can be Implemented
  by a leaf node that represents am Individual objects, or composite node that represent
  a group of objects.
- composite node have one or more child components of the same interface it can delegate the
  method calls to its child components and it can also perfom additional operation on them
  This allow us to perform operation on the entire tree stucture as a single objects or on
  a specific components.
- Overall the composite design pattern helps to create hierachical object stucture that
  can be treated as a single object or a group of objects, providing flexibility and
  scalability to the design.

# Real word use case
- File System : best example of it, directory can contains files or subdirectories, and
  subdirectory can have files and subdirectory inside it, forming a hireachical stucture
- Organisational chart - depart, teamps, emp is leaf
- GUI - window can contains other window or components such as buttons, text boxes, and menus.
- Music Playlists: when playlist can contain individual songs or other playlist, forming a
  hierachical stucture.
- HtML documntes - html elemnts paragraph, link etc
- MenuSystme - menu can contains submenu and menu items.
- Computer Network - network contains sub network such as devices, switches, routers

# Terminnologies
- Components: This  is a common interface shared by all objects in the composite. it delares the
  methods that are common to both simple and complex objects.
- Leaf: basic Implemnation of the component interface. A leaf object has not any children
- Composite: complex implemnation of component interface. it can contains other components
  including other composite objects.
- Client: This is the code that uses the Component intrface to interact with the object in
  composition
- Recursive Composition: key feature of composite pattern, where composite obejcts
  can constains other composite obejcts in recursive manner forming like tree stucture

# When to use it
- Hieracical stucture of obejcts, tree-like stucture of objects each object as type
  object of same type
- add and remove objects from tree stucture at runtime

# Advatges
simplified code
Flexible stucture
Uniform interface
Enacptulation 
Extensibility

# disadvatges
- performance overhead
- Limited type hierachy : if yu have a hierachy of objects of diffent type of objects, this is not best fit
- Lack of type safety

# Things to Note:
- Define common interfcae: all shoud implents, all components treated in Uniform ways
- Implemnt the composite objects: composite objects contains list of child objects
- implemnt the leaf objects: also implemt the common interface
- use Recursion
- be aware of type safety
- be aware of performance - complex hierachies

 



