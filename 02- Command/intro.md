# Command Design pattern
- it provide a way to encaptulates a request as an object. Thrby allowing user to
parameterize client with different requests, queue or log requests and support undoable
operations it decouples the sender of the request from the objects that perfom the
actions, provinding flexibility and extensibility is designig and managing requests.
- CP is to represent request as an objects, which allow handling actios and intercations
- the CP allows decoupling of object involved in a request, making the system more flexible
  and scalable it enables the construction of complex system based on small reusable command
  objects, and support operation such as undeo and redo by keeping history of executed commands
  additional it facilites the implemantion of feature like logging, queuing, and sceduling of the
  commands.

# Real word use case
- GUI: user action button click, each button or menu item can have a corresponding command object
  associated with it, which is executed when the user interacts with the UI eleemnts.
- udeo/redo functionality - each executed command is stored in command history
- Remote control Systems
- Transaction managemnts: in db, each transaction is represented by command object, and execution of 
  transaction is carried out by invoking the execute() method on the command, this allow atomoticity
  and transactional intergirity
- Jos Sceduling:  differnt task and job need to executes in a specific times and intervals, each job
  is enacpatulated as a command and the scedular invoke the execute method of the command when the
  sceduled time is reached.
- Text Editors: various edit operations, insert delete , copy, paste etc can be encaptulated as the command objects. allowing easy extensibility and customization of editor functionality
- Robotics and automations- move, forward, turn, pickup
- Multilevel menu

# Terminologies

- Command: interface or abstarct class that declares the execution methods execute(), it represents the request and provide a common interface for all concreate commands.
- ConcreteComands: The impplemnation classes that encaptulates specific request and bind them to receivers, They implent the execute methods by invoking the corresponding operations on the receivers
- Receiver: conatins actual bussiness logic, operation, it define actions concreateCommand objects can perform.
- Invoker: holds reference of command objects, and responsible for executing coammand when requested
  it invokes the execute methods, on the command but it doesnot know the specific command impleemnation.
- Client: act as intitiator of request
- client application: the applications or system that utilize the command pattern to execute the request.
- command queue: A data stucture (eg a list of queue) that sored a command in the order they are
  received, it allows for delayed execution or sceduling of commands. 
- MacroCommand: command obj that encaptulates command of other obejcts, it allow multiple command
  to execute as a single command. enabling complex operations or batch processing.
- Undoable Command: undoing the executed command it typically provide additional method
  undo() to reverse the effect of execute methods
- CommandHistory - undeo, redo operations, Implemnted as stack or list

# When shoudl i Use
- Decoupling The invoker and receiver: 
- supporting undeo/redo operations
- Implemnting transatcional behaviour - group of trns either commit or rollback
- supporting extensibility and customization
- Implementing callback Functionality: By encaptulating the request as a command objects
  you can pass it to other objects, as a callback allowing them to execute the command at a
  later time or in response to specific events.

# Advatges
- Decoupling - sender request to receiver
- Flexibility and Extensibility
- Undeo/redo transactional support
- Support of callback and async operation : event driven systm
- centralized control

# disadvatges
- Increased Complexity
- potential performance overhead
- Increased memory usages
- Potential overuse - not benifit in all situations
- Learning curve

# Things to Note
- Use Interface or abstract base classes: although python doesnot enforce strcit interface like some
  other language its good practise to define interfaces or abstarct base classes to represent the command and receiver objects, This help to ensure that all commands adhere to common interface 
  and make the code more maintainable and understandable.
- commands and First class objects: in python functions are first class objects, so you cab use
  function as a command object directly this similifies the imple of command pattern by avoiding the
  need of seperate command classes. however you have more complex command or need to encaptulates
  additiional data, defning command class may be more appropriate.
- Consider using lambada Functions: use effectively if simpler command objects
- Carefully manages refernces: command obj don't hold strong refernces to large objects or data stucture. as it can leak to memory, consider weak refernce or carefully managing obj lifecyle if
necessary.
- Undeo/redo functiolity - state changes need to recorded, use memento pattern in conjustion with 
  command pattern
- Use invoker as centeral control points
- considerd error handling
- Test thoroughly



