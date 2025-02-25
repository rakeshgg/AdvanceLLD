# FlyWeightPattern

- Flyweight pattern aim to minimize the memory usages by sharing as much as data possible
  when app have large number of similar objects that can represented more efficiently by sharing
  there certain part of there state
- created set of light-weight objects, called flyweights, that store shared data was used by
  multiple objects this flyweight are immutable and have a unique identity that can be used to
  looked them up in shared pool. when new object is created it is given a reference to the
  appropriate flyweight objects, which it can use the shared data.
- By using the flyweight the application can reduce memory usages and Improve perormnace
  this pattern is commonly used in graphical applications, where a large number of objects
  with similar charactristic are diplayed on the screen.

# Real word use case
- TextEditors - mange the font size, where many char might share same font size, the text editor 
  can create a flyweight obj for each unique fonts and size, nd reuse these objects for each char
  that need to be diplayed in that font and size.
- WebBrowsers: Display images on a web page. Instead of loading the same object multiple times
  the browser load the image at once and then create a flyweight object for each instances of 
  that image on the page.
- Computer games: game objects, such as trees, rocks and other environmental objects these obj
  are typically repeated throughout the game and the Flyweight pattern allows the game to render
  these objects efficiently.
- MusicPlayers: manage and diplay of album art. each album art is loaded ance and than shared
  by multiple songs in the same album
- Documnt amnagemnt system: diplay of doc properties such as author, date created, and keywords
  each doc have its own set of properties, but many docs might share the same properties and the
  flyweight pattern can be used to avoid duplicating the data.

# Terminologies
- Flyweight - shared object, shared state used by multiple insatnces
- FlyWeightFactory: its responsible for creating and managing flyweight objects. it keep track of
  the flyweight objects and provides a way for client to access them.
- client: the client use flyweight objects to perfom there operations, they typically store
  their unique state data and pass it to the Flyweight objects as needed.
- Shared state: its data that is stored in the flyweight objects and shared by multiple clients
  this data is typically immuatble can can be used by multiple instances of the Flyweight objects.
- UniqueState: that is stored by the client objects and specific to each instances of the client.
  this data is typically mutable and is passed to flyweight objects as needed.
- Context - client-specifc state that is stored by the client objects it is the state
  that is unique o each client objects and used to modify the behaviour of the Flyweight
  object as needed.

# When to use Flyweight pattern
when you have a large number of objects that are similar in nature and share the common properties
and creating and storing individual objects consumes a lot of memory
you can use flyweight design pattern when
- You need to create large number of objects with similar attributes
- The obejcts can be shared and reused across multiple contexts.
- the objects are Immuatble or their state acn be seperated into intrinsic
  and extrinisic state.
- Memory uses is concrernd and you need to optimize memory usages

# Advatges
- memory Efficient
- Performance Improvemnts
- Reusability
- Simplified code

# Disadvatges
- Incresed complexity
- Limited applicability - large number of similar objs
- Loss of Encaptulation : by seperating instrinsic and extrinsic state, we may lose some
   of the encaptulation objects which can lead to code that is harder to maintain and debug
- performance overhead - number obj is relatively small

# Things to Note:
- Seperation of intrinsic and extrinsic state : intrinsic state should be shared among multiple
  objects, while extrinsic state should be passed in from the outside and not shared.
- Imutability of intrinsic state - accidental modification
- use of caching: to avoid unnecessary creation of flyweight objects, you can use caching techniques
  like memoization and reuse exiting objects.
- proper Implemnation of Factory - responsible of manging and creation of flyweight, caching
- Consideraation of concurrency: if multi threaded or multi-process you need to ensure that
  the flyweight objects are accesed in a thread-safe manner to prevent race-conditions.
- Testing



