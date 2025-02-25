# Observer design pattern

- It establish one to many dependency between objects, it define a suscription mecanisum
  where one object called the (subject or observable) manintain a list of objects(called observers)
  and notifies them automatically of any changes in the state.'
- main goal is to ensure that multiple observer can be notified and updated when the state of
  the subject changes, without the subject needing to have direct knowledge of the observer
  enabling a more flexible and maintianable system.
- In the observer pattern the subject maintains a list of observers, and provide a method to
  suscribe and unsuscribe the observers. when the subject state changes, it notifies all the
  suscribed observes, typically by invoking a methods on each observer. the obsrver can then
  perform there specific logic based on the updated information receive from the subjects
- This pattern is widely used in evet-deriven system,gui, and many system that decoupling of
  components is desired.

# Real word use case

- stock markets - price chnage of specific stock, stock market acts as the subject and
  Investor are the observer. when price chnaged it notified all the suscribed Inverstors.
  allowing them to make informed decision.
- Wheather Monitoring - wheather station collect data about temperature, humidity and other
  atomospheric conditions, multiple diplay devices such as mobile apps, or weather website
  acts as observer and suscribe to receive updates from wheather station. whenever wheather
  consitions changes the wheather station notififes all the suscibed diplay device enabling them to
  display the updated wheather Information.
- Event handling in gui - observer pattern to user interaction, consider button on GUI, button serve
  as subject and various listners or events, handles acts as observer when the button is clicked
  it notified all the suscribed event hanlders allowing them to perform their specific actions
  in response to click events.
- traffic mangements - multiple traffice lights at intersctions, can observe a central control system
  acting as the subject, the central control system monitor the traffic conditions and notifies the
  traffice lights, when light sequnce need to change the traffic lights as observer update their state accordingly to regulate the flow of vechiles.
- socialmedia notfification - user can suscribe notification about new messages, friend req, comments or lieks, social media acts as a subject and the user are observer when a new notification is generated the platform notifies the suscibed users esnsuring they are promptly informed about
  relevant activites.
- Distributed system - multipel data and replica of db acts as observer of main node, allowing them mintain consistency and syncronization in distribited db.e

# Terminologies

- Subject(also known as observable or publisher) -it is the object that maintains a list of observers
  and send a notification to them when its state chnages, the subject provide methods to suscibe,
  unsuscibe and notify observers.
- Observers(also know as suscriber or Listner): it is the interface or base class Implemnted by the
  observers, the observer define the update methods that is called by the subject when the state change occurs. observer are the receipents of the notification from the subject.
- ConcreateSubject(concreateObserbable, ConcreatePublisher) - specifc implemnstion of subject or
  interface of a class. the concraete subject holds the actual state ans send the notification to
  the registerd observer when changes occurs.
- ConcreateSubject/obserbale/Publisher - it is a spcific Implemnation of subject interface or class.
  it holds the actual state and send the notiffication of registerd observer when changes occurs.
- ConcreateObserver - specific implemneation of observer interface or class
- suscriptions - process of observing registering with subject to receive notifications. when an
  observer suscribes, it added to the subject list of the observer.
- unsuscriptions - process of unregistering objs from a subject. removes from the list
- Notifications - act of informing the observer about state change in the subejct when subject
  state changes it iterate over its list of observer and calls their respective update methods
  to notify them about the changes
- State - represenst the data or condition being obsereved by the subject. when state of the subject changes, it triggers notification of registerd observer.

# Advatge

- loose coupling between subejct (observeble) and observers
- Flexibility extensibility
- Decenatralized control
- Even driven artitecture
- Reusability

# Disadavtges

- Performance overhead
- unexpected updates
- Complexity
- order of notifications - if sequnce is important then issue

# when shoudl i use it

- Event driven system : obs need to react with event chnages
- user interface components - notify changes, syncronized ui updates
- ditributed system - different nodes or components may need to comunicate and syncronize their state. the observer pattern can be used to establish a pusblish-suscribe mecanisum, where node can
  suscibe as observer to receive updates or events from other nodes.
- Logging and auditing: logging specific events or changes provide modular and extensible logging mecanisum.
- DataSyncronization - multiple data source or caches that need to syncronized the observer pattern can be employeed. chnages in one data source can be propgated to other observer esuring the data
  consistency across the system.

# Things to Note

- define clear observer interface
- use data stucture for manging observeers, list, set
- attaching and detaching from observers
- Implemnt notification mechanisum
- considerd order of notification - observer arr notify order
- avoid tight coupling
- Thread safety and syncronization
- performance consideration
-
