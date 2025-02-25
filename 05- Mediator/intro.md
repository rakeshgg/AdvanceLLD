# mediator

- its a behavioural design pattern that promotes loose coupling between a set of objects
  by centeralizing their commnuincation through a mediator objects. it allows objects to
  intercat with each other indirecetely through mediator, rather than direcetely comunicating
  with each other. this help to reduce the dependency between objects. simplifies there
  interaction and enhance their reusability.
- the mediator objects encaptulates the communication logic and control the flow of messgae between
  objects. it acts a centralized hub or facilator that coordinate the intercation among the participant objects. instead of objs comnunicate between them directely. they send message
  to the mediator which than handle the routing and delivery of those message to the mediator
  which than handle the routing and delivery of those message to the appropriate objects.
- by decoupling objects and relying on mediators the mediator pattern enables the objects to focus
  on their individual responsibilites without being aware of the details or exitence of other
  objects this promotes better encaptulation and modular design.

# Real word use case

- Air Traffic control system: different aircraft need to comunicate and coordinate their
  movements. the air traffic control centre acts as a mediator, receving message from the
  aircraft and relying them to to appropriate aircraft, ensure safe and efficient operations
- OnlineMarketPlace: multiple seller and buyer interact with each other, marketplace acts as
  mediator handling comunication between seller and buyers. seller can send the product information
  and updates while buyer can send purchase request and inqueries, all facilated through the platform
- chat application - central chat message act as mediator distributed to them, the server can handle
  task such as message routing, user presence management, and notification delivery
- Smart Home Automation System: device like lights thermostat, and sensor need to interact and co-ordinate their actions, a central automation controller can acts as mediator
- Event driven artictecture: multiple components and microservice comunicate through event, an event
  bus or message broker can act as a mediator receving events from different components and routing them to intrested suscribers, this enables loosly coupled comunication between components.
- MultiPlayer Game: multiplayer game interact to each other and with the game world. a game server
  can acts as a mediator, handling player actions, updating the game state, and brodcasting the
  relevant information to all players, ensuring syncronized gameplay.

# Terminologies

- Mediator: it define the interface for comunication between objects and encaptulates the
  comunication logic, the mediator receive message from objects and handle their distribution
  to the appropriate recipients.
- colleague: also know as participants, these are objects that interact with each other indirectely
  through the mediator, colleague are unware of each other existence and comunicate with mediator
  to send and receive message.
- concrete mediator - corodiantes between colleague objects, maintinas reference of participants
  colleaguege and determine how message are routed and delivered.
- colleague Interface: define the interface that colleague objects must Implement, it typically include methods for sending message and receiving message from the mediator.
- Concreate Colleague: refer to specific Implemnation of a colleague objects. concreate colleague
  counicate with the mediator using the method defined in the colleague interface.
- Mesaage - info need to exchange

# When shoudl is use it

- when set of objects comunicate in a complex manner
- when you want to reduce dependenices between objects
- when adding new components becomes easier.
- when you want to promote code reusability
- when you need centalized coordiante points
- its important to note that mediator pattern shoudl use judisiouly. it is more
  benificial when the complexity of communication between objects justifies the
  introduction of the mediator, for simpler senarion direct object-object
  comunication may be more appropriate.

# advatges

- Decoupling of components
- centralized control
- simplified communication logic
- reusability and extensibility

# disadvategs

- Increased complexity of the mediator
- performance overhead
- potential single point Failure
- lack of visbility between components

# Things to Note

- Define mediator class - methdos for register, send and receive message
- define colleague class - refernce to mediators
- Encaptulates comunication logic
- keep dependecies minimal
- favour compistion over inheritance
- considerd the scalability and complexity
- test and verfiy comunications
- Document and cmunicate the design
