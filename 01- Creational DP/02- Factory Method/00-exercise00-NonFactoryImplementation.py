# Genral Impemenation
# type of action we take based on if else
# Not Effective to Implements some draw back thats why Factory
# Design pattern take care of this
"""
Draw back of non Factory method code:
1. Voilation of single Responsibility Principle
   its responsible for creating and starting of differnt type of vechiles
   voilates SRP, class have only one reason to change
   In the absence of FM, Vechiles class take responsility
   of objects creations, along with primary responsibilituy
   of starting vechiles.
2. Tight Coupling
  client code direct creates instances of vechiles car = Vehicle('car')
  create tight coupling between client code and specific vechiles type
  if new vechiles added client need to updated accordingly which increse
  Mainatince efforts and introduce Risk of Introducing Errors.
3. Lack of Abstarction
  code lack on abstarction layer that represents a common interfcae for
  differnt
  type of vechiles. the absence of abstarction make it difficults
  to introduce new
  vechile type without modifying vechiles class. also limit the ability
  to substitute different vechiles type at runtime or extend the
  code to handle more complex senario Involving differnt behaviour
  for each vechile type.
4. Code Duplication
   The conditional method in Start() result in code duplication
   each time new vechile type is added same code is repeated
   This voilates DRY Principles, mainatince challanges as any
   chnages or fixes to logic would required to update multiple
   places.
5. Limited Flexibility and Scalability: harder to extend the code base
   with new type of vechiles or introducing changes to exiting vechiles
   creation and behaviour, The lack of clear seperation of concerns and
   tight coupling between the client code and the Vechile class make the
   code less flexible and scalable.
By appliying factory methods these draw back can be addressed the pattern
provides a stuctured approch to object creation, decouples the client code
from specific Implemenation, introduce abstraction and Flexibility and promotes
better code organization and maintainability.

"""


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        if self.vehicle_type == "car":
            print("Starting the car...")
        elif self.vehicle_type == "motorcycle":
            print("Starting the motorcycle...")
        elif self.vehicle_type == "bicycle":
            print("Starting the bicycle...")
        else:
            print("Invalid vehicle type!")


# Client code
car = Vehicle("car")
car.start()

motorcycle = Vehicle("motorcycle")
motorcycle.start()

bicycle = Vehicle("bicycle")
bicycle.start()

# chaage to code in next
