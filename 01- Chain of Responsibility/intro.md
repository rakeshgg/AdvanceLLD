# CRP
- CRP pattern is beahvioual that provide a way to pass a request along to chain
  of potential handalers until one of them handle the request. the pattern
  decouples sender and receiver of a request. allowing multiple objects
  to have a chnace to handle the request without explicitly knowing which
  object will handle it.
- When client send a request, it receive by first handelr in the chain. this
  handler examines the request and decides wheather it can handle it or not.
  if it can it process the request and completes the handling, if not passes
  the request to the next handler in the chain. This process continue until
  the handler handles the request or until the end of chain is reached.
- promotes loose coupling between sender and receivers, and neither have to
  dorect knowledge of each other. it allows for flexible and dynamic handling
  of request, as chain can be modified or extended at runtime.

# real word use case
- Event Handling and GUI: GUI often use the CRP to handle user input events.
  for eg when button is clicked the event is passed through the chain of 
  event handlers, such as mouse click handlers focus handlers, or action
  handlers each handle decide wheather it can handle the events or passes
  to next handler in the chain.
- LoggingSystem: logging framework may utilize CRP to process log message with
  differnet level of severity. each handlers in the chain determines wheather
  it can handle the log message based on its servity level, for intsnaces
  handler for error message may print to them to the console.
- MiddleWare in web dev: web framework use CRP to implemnts middleware functionality.
  middleware components in the chain process incoming HTTP requests and can perform
  various task as such as authentication, request parsing, request validation, or logging
  each middleware components can decide to handle the request or pass it to next middleware
  in the chain
- ExceptionHandling: Multiple exception handlers can be organised in a chain, wheather its
  handler can check if it can handle a specific type of exceptions. if handler cannot 
  handle the exception it passes it to next handler in the chain, until an appropriate
  handler is found or exception is not handled at all.
- WorkflowSystem: it employ the chain of responssibility pattern to define and execute
  sequnce of task or steps, each step in workflow is represented by handler which perform
  its specific task and decide wheather to pass the control to the next handler or terminate
  the workflow.

# Terminnologies
- Handler: also know as the abstarct handler, or base handler it is interface of abstract
    or abstarct class that define the common interface for all concrete handler. it declares the
    handler_request() method that concreate handler must Implemnt. the handler usally contains
    a reference to the next handler in the chain.
- concreate handler: it decide wheather it can handle a request it process it; otherwise it passes
  to the request to the next handler in the chain.
- Succesor: it refer to next handler in the chain
- client - initiates the request and start processing the chain, it is responsible for creating
  the chain of handlers and sending the request to the first handler in the chain.
- requeest: it represent request being passed to the chain handler, The request can be 
  a specific objects or datastucture that encaptulates the information or context required
  for handling and processing.

# when shoudl we use it?
- Multiple objects need to handle a request independently: if a request that can be handleed by
  different objects, and each object can handle the request in its own way or pass it to next
  object in the chain, the chain of resposibility pattern is a good choice. The pattern promotes
  loose coupling between the sender of request and the receiver objects.
- The set of objects that can handle the request should be dynamic: it allow you to
  easily add or remove handlers in a chain at runtime providing flexibility in the
  composition of the chain. This make suitable for scenarios where the set of objects that can handle the request can change dynamically.
- The order of handling matters: CRP can esnure that each handler in the chain process the request
  in specific order, each handler either choose to handle the request or pass it to the next handler
  allowing for sequntial processing.
- Yes you want to decouple the sender and receiver: CRP helps to decouples the sender of request
  from the receiver objects. the sender doesnot need to know which specific objects will handle the
  request. and the receiver objects don't need to have direct knowledege of the sender. this promotes
  a more flexible and maintainaible design.
- You want to avoid coupling the sender to specific handler classes: by using CRP, the sender only need to interact with the first object in the chain without knowing the specific handlers involved
this promotes encaptulation and avoid tight couppling the sender and the handler classes.
- overall the CRP is suitable when you have a set of objects that can handle a request in
  a specific order, and you want to promote flexibility, decoupling and dynamic comsposition
  of the handlers.

# Things to Note:
- Define a common interface
- Establish the chain - linking the handler each handler have its succesor link
- Handle the request
- considerd using termination chain: based on specific criterira no more handler in chain
- order of handling the handler
- Error handling and exceptions
- Testing and debuging
- Documenation and clarity








