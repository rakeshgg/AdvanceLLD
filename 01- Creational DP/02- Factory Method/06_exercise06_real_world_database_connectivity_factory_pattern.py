from abc import ABC, abstractmethod


# FACTORY DP#
# 1. abstract product
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


# 2. concrete products  #mysql, postgreSQL, oracle
class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL Database.... Established"


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL Database.... Established"


class OracleConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to ORACLE Database.... Established"


class DatabaseFactory:
    def __init__(self):
        self.factory = dict(
            mysql=MySQLConnection,
            postgresql=PostgreSQLConnection,
            oracle=OracleConnection,
        )

    def create_connection(self, db_name):
        if db_name in self.factory:
            connection = self.factory.get(db_name)()
            return connection


# 5. Client Code
if __name__ == "__main__":
    db_factory = DatabaseFactory()

    mysql = db_factory.create_connection("mysql")
    print(mysql.connect())

    pgress = db_factory.create_connection("postgresql")
    print(pgress.connect())

    oracle = db_factory.create_connection("oracle")
    print(oracle.connect())

"""
Factory Pattern over factory methods Advatages

when to use factory methods over Factory patterns
- Flexibility and Extensibility - Factory methods design pattern
allow more Flexibility and Extensibility in objects creation
creation of obejcts is delegated to subclasses. you can
easily introduce subclasses and extend factory functionality
without modifying it. this make easier to add new product
variations or modify the creation logic as needed.

- PolyMorphisum - FD promotes polymorphisum
each subclass return differnt concrete impemenation
of the products, allowing for greater variations
and customization. this is particuar useful when
you have multiple products families or when creation
logic depends on specific condition or params.

- Separtion of Concrens - sepearte the responsibility
of object creation into subclasses. keeping core logic
of factory class clean and focused This seperation of concerns
can Improve the overall design and maintainability of
your codebase.

Testebility - make testing easier, by introducing sublclass of
object created you can easily mock or subsitute this subclasses
during testing enabling more focused and isolated unit testing.

Simplicity - Factory design pattern is generally simple to implement
and understand compared to the Factory Method design pattern
it doesnot required to use of abstarct classes and interface
and the creation Logic is Centralized with a single Factory class
The Simiplicty can be benificial when the creation process is
straignht forward and doesnot required complex
customization or variation.

Centralized Control: the creation logic is contanied within the
single Factory class. this is advatages when you want to maintains
strict control over obejct creation process. it allows to
encaptulate the creation logic and enforce consistent
instantiation rules across all the objects created by Factory.

Less abstraction: the factory design pattern doesn't rely on
abstarct classes or interface for creating objects, this can
be advantageous when you don't need the Level of abstarction
and polymorphisum provided by the Factory Method Design pattern
it can result in simpler and more strainght forward code bases.

code organisation: all object creation code is in factory
making it eaiser to locate and manage, particularly in
smaller scale projects or situation where creation logic
not required more complex customization.

"""
