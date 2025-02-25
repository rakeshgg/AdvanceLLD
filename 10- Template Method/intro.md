# Template Methods

- way to define the skeleton of an algo, in a base class, while allowing sub class
  to customize or provide specific Implemnation for certain steps of algorithums
- pattern follow principle of inversiion of control where base class often called
  the templte class or absatrct class define a template methods that represents
  the overall algorithums. this templte method consist of series of steps operations
  some which are common to all subclasses. and soem of which may vary.
- whnen client invoke template methods on a subclass, the overall algo is executed in
  predefied sequnces.
- It allow for code reuse encaptulates the common algo stucture and provdie consitent workflow
  across different Implemnation. It promotes nodularity and maintainability by seperating the
  common algorithums from specific Implemnation of Individual steps.

# Real world use case

- database query execution : connecting to db, execting query and retriving the results
  template method pattern can define the base class that provdie overall stucture of the
  query execution algorithums, with subclasses customizing specific steps such as establishing
  a database connection, executing the query, and processing the results.
- Web Application Frame Works - common stucture for handling HTTP request, routing, authentciation
  and response generation
- Bevarge Preperations - common stucture
- report gernaration - financial report, sales report, subclasses customize specific steps such as
  gathering data, formating the report, and generating output in differnt formats
- Game developemnts: dfiffernt level and stategs
- E-commerce order processing: Validating payemnts, updating inventory, and generating shipping Levels.
- test Automation FrameWorks
- Nwteork protocol Implemnation
- Batch processing system - input data reading, performing calculation or transformation, and writing the results of output file.

# Terminolgies

- Absatrct class - also know as base class or template class, it define overall algo stucture
  and provide a Template methods. it may conatins both abstarct and concreate methods.
- Concreate class - Theses are subclasses that Inherit from absatrct class and provide a concreate Implemnation for the abstract method defined in the abstarct class. Each concreate class represents
  a specific variations or customization of algorithums.
- Template Methods - This method is defiend in the abstarct class which provide the overall algorithums stucture. It consist of series of steps and methods calls, some which are Implemnted
  directely in the absatrct class and other that are left to be Implemnted by concrete subclass.
- Absatrct methods - also known as placeholder method, its is method declared in absatct class
  but doesnot have Implemenation. concreate subclass are responsible for providing of the Implemnation of these absatrct methods according to there specific need.
- hook methods - Hook method is an optional methods declared in abstrct class with default and empty implemenation. it is intended to overridden by subclasses to provide additional customization points
  within the algorithum. subclass can be chooosen to override and ignore hook method based on their
  requirements.
- Algorithum - series of steps and methods perfom in a specific order to acheive certain goals
- Inversion of control - The Template method pattern follow the principle of Inversion of control
  when the control of algo is placed in the hand of abstract class. the abstarct class define the
  the stucture of algorithums while concreate subclasses provide specific Implemnation details

# When should is use it?

- common algo with varying implemnation
- reusability and code sharing
- Enforcing a consistent workflow
- Behavioural variation in a related class
- Extensibility and customization

# Advatages

- code reusability
- Encaptulation algorithums
- Flexibility and customization
- Enforces consistency
- Promotes seperation of concerns

# Disadvatges

- limited runtime flexibility
- Inheritance dependency
- Increased complexity
- Limited variation in algo stucture
- voilation of interface segration principles

# things to Note

- Abstarct base class
- Template Methods
- Concreate subclasses
- common stucture
- Inversion of control
- Hooks or abstarct methods - subclasses must implemnts
- Template and starategy : pattern are similar but they differ in the intent the template method pattern forcus on defining overall algorithums stucture, with varying steps. while strategy pattern
  focuses on encaptulating interchnagagble algo. the template method pattern use inheritance where
  starategy pattern use composition.
- Design for Extensibility
- Consisderd dependency Inversion
- use with caution
