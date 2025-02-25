# State Design pattern

- allow an object to alter the behaviour when its internal state changes. it enables an object
  to appear as if it is chnaging its class as the object behaviour is determined by its current
  state. the state pattern prmotes encaptulation and seperation of concerns by representing
  different state as seperate classes. each Implemneting a common interfcae.
- the main idea behind state pattern is to encaptulates the behaviour associtated with
  each state into seperate classes, known as state classes. there state classes define the
  methods and actions that are specific to that particualr state. the context class. which
  represents the objects whose behaviour is being controlled by the state, contains a refernce
  to the current state objects.
- The state design pattern is useful in senarios where an object behaviour varies based on
  its internal state. and when you want to acheive cleaner code organisation, Improved mainatinbility
  and extensibility.

# Real word use case

- document processing - manage different state of docs, such as Editing, reviewing, or Finalizing
  each state can define its own behaviour and restiction to the documents.
- WorkFlow managements - Pending for approval,In progress,completed the state patetrn can applied
  to handle state transation, and associated actions.
- traffic Light system:
- online shopping cart - differnt state of shooping cart such as Empty, active, or checked out
- game charcter AI - state can represents mood or actions of non-player charcters such as Idle
  Aggregasive, or Friendly and determine there Intercation with players.
- Music Player - playback state, play, pause or stopped
- ATM (Automated teller machine) - such as idle, card inserted, pin entered, and transaction in progress each state guide through the correct sequnce of steps.
- booking System: for hotel, flights can use the state pattern to manage various state of a reservation, such as Reserved, confirmed, Checked-in, or cancelled, each state can enforce the
  specific rule and triggered appropriate actions.
- network connction - connected, diconnected , error each state can handle connection establishemnt,
  data transfer, error handling differently.
- Coffee machine - coffe machine with different modes with Breawaing, heating, or standby can utilize the state pattern to manage its behaviour and interaction based on the current mode.

# Terminologies

- Context : refer to objects that contains the state and whose behaviur was affected by state
  it maintains the refernce to the current state objects and delgates the state specific behaviour
  to that objects. The context class define methdos and properties that are used by state objects
  to transation between state.
- State - represents specific behaviour or state of the context object. it is usally implemnted as
  Interface or an abstarct base class that define a set of methods that the context can call to
  perform state-sepcific operations. each state class provides its won Implemantion for these methods
- Concreate State: each concreate state class represents a particular state of the context objects
  and provide Implenation for the methods define in the state interface.
- Transaitions: when the context obj changes its state from one to other, usally triggerd by specific events or conditions that caused it transaction to different state. transaiction are handled by state obejct them self and decide which state to transaition to based on the current
  state and triggering events.
- Clinet - interacts with context objects

# When shoudl we use it

- object behaviour dependes on its state
- multiple conditional statements
- Simplifying complex state machine
- Adding new sattes and behaviour - in future
- Encaptulate state specific logic

# Advatges

- Enacaptultes state specific behaviour
- Simplifies complex state machine
- open for extension and closed for modification
- prmotes cleaner code - swicth statemnts, conditional are not required
- Enhance testbility

# disadvatges

- incresed number of classes
- potential overhead
- potential for misuse
- Increased complexity for simple cases

# Things to Note

- Define absatrct base class - for state class
- concrete state classes
- maintain a refernce to a current state
- Encaptulates state specific logics
- handle state transaitions
- use polymorphisum - call specific methods using objects
- consided initialization and shared context
