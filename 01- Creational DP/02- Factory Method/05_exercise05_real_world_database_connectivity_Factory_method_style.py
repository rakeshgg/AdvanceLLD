from abc import ABC, abstractmethod


# FACTORY METHOD DP #
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


# 3. abstract Creator (Factory)
# factory how creation is done
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass


# 4. concrete Creators (Factory)
class MySQLConnectionFactory(DatabaseConnectionFactory):
    # 4.1 Factory Method
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()


class PostgreSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()


class OracleConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return OracleConnection()


# 5. Client Code
def connect_to_database(factory: DatabaseConnectionFactory):
    connection = factory.create_connection()
    print(connection.connect())


# use Factory to call them
mysql_factory = MySQLConnectionFactory()
connect_to_database(mysql_factory)

postgres_factory = PostgreSQLConnectionFactory()
connect_to_database(postgres_factory)

oracle_factory = OracleConnectionFactory()
connect_to_database(oracle_factory)

"""
Factory pattern we didnot required differnt abstarct Factory
and concreate Factory
Other way to Implemnts

direclty create Class Factory
class DataBaseFactory:
   def __init__()
     create dictionary of Fcatory
     self.factroy = dict(mysql=MySQLConnection)
     # creating a products
     def create_connection(self, db_name):
       if db.name in self.factory:
         connection = self.factory.get(db_name)()
         return connection
# client
db_factory = DataBaseFactory()
mysql = db_factory.create_connection('mysql')

"""
