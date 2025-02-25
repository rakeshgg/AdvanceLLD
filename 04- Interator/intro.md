# Iterator 

- It provides way to access the elements of aggregate objects(such as list, array, collections)
  sequntially without exposing its underlying represenation. it allow traversal of the eleemnts
  of a container objects in a consistent and efficient manner.
- The key idea behing the iterator pattern is to seperate the traversal logic from the conatiner
  object itself. this seperation improves the flexibility and extensibility of the code by allowing
  differnt traversal algo to use with the same container, without modifying the container stucture.
  this pattern is commonly used by many libraries in python to traverse elements in them.
- by using the iterator pattern, client code can iterate over the elements of container objects
  without being concerned about the underlying stucture or Implemenation details. this promotes
  the loose coupling between the client code and the container objects. making the code more maintainable and reusable.

# Real word use case
- Iterating over database result set
- File system traversal - hierachial stucture, travese and process files
- Social media feeds: Social media have a feed that display a stream of posts or update from the differnt users. The iterator pattern can be used to iterate over these feeds, allowing user to
scroll through and view the content in the sequntial manner.
- Menu Nvaigation: user interface menu is used to provide a stucutured ways to access differnt options or commands. the iterator pattern can employed to iterate over the menu items, enabling the
navigation and selction of menu options.
- Inverntoty managemnts - iterate over the items in the Inventory, allowing opertaions like searching
  counting, updating each stucture without exposing the underlying data stucture
- Music Playlist managemnts - collection of songs, provide method to play, skip, or remove songs
  in a consistent and controlled manner.
- parsing and processing xml or json documents - when parsing and processinng data formats like
  xml, json, iterator pattern is used to iterate over the elelemnts in the documnts, making it easier to extract and process the required data.

# Terminologies
- Iterator - an interface base class that define the operation for accesing and travesing the
  elements in the container. it typically includes methods like next(), reset() etc. The itertator
  provides a common way to iterate over elements regardless of the specific contianer types.
- ConcereteIterator: provide actual implemnation traversing the elemnets of actual container.
  it keep track of current position within the container and provides the necessary methods
  to move the next elements. and retrive the current elements.
- Aggregate: it represents the container obejcts that hold collections of elemnts. it 
  provide a methods usally called createiterator(), that return an iterator objects for
  traversing the elements. the aggreagte may also define the to manupulate the collections
  of elements, such as adding or removing the elements.
- ConcreateAggregate: it define specific container objects and stucture it create and appropriate
  concreateIterator objects and return to client through createIterator() method.
- Client - refer to code that use the iterator patetrn to traverse the eleemnts of the container
  The client request and iterator objects to aggreagte and uses its to iterate over the elements
  without being aware of the conatiner specific Implemnation details.

# when shoud i use it
- when you want to acees the elemnts of collection sequntially without exposing its underlying
  represenation. The Itertaor provides a uniform interface to iterate over the collections
  regardless of its Implemnation.
- when you want to decoupled traversal algo from collection class.
  by sperating the iteration logic into an interator object, you can change or extend the iteration
  algo independtly of the collection class.
- when you want to provide multiple iteration strategies from the same collections. The iterator
  design pattern allows you to define different iterators for the same collections each with its
  own traversal strategy, and switch between them seamlesslay.
- when you want to provide a standard interface for iterating over different type of collections
  . by adhering the iterator interface, different collection classes can be iterated in a consistent
  maner, making it easier to work with various collection types in a generic ways.
- When you want to simplify client code that iterate over a collections. the iterator pattern
  enacptulates the iteration logic within the iterator objects. reducing the complexity
  and clutter in the client code.
- when you want to support lazy or on-demand traversal of large dynamically generated collections
  the iterator pattern allows you to retrieve elements one at a time as needed, without loading the
  entire collection into memory upfront.

# Advatages
- Simplifies the client code
- Encpatulates iteration Logic
- Support multiple traversal strategies
- Hide the collection Implemntion details
- Allow for lazy or on-demand traversal

# disadvatges
- additional complexity
- Increased code and classes
- Limited functionality
- Not suitable for all senarieos: random acess traversal required
- iteration order Limitation

# Things to note
- abc module - interface or abstarct base class
- Implemnt the iterator interface
   - has_next()
   - next()
- Consider Implenting the iteraable objects: in python common to make the collection class
  iteratable by implementing the iter() method. this method should return the iterator objects
  itself or create and return the new iterator objects. this allow collection objects to be
  used in for loop and other iterable operations.
- raise StorInteration
- Decide on iteration order - specific logic in iterator class to control the order of iteration
- Consider the Lazy Evaluations - working with large or dynamically generated collections,
  you may consider Implemnting the lazy evaluation. This means elemnts are retreived and processed
  only when requested. rather than loading the entire collections into memory upfront.
- Leverage existing python utilities: built-in utilites for iteration such as generator and comrehension, 






