# Select, from, WHERE, Group By, Limit
"""
real word SQL Query Builder
construct different Query
added incremently making construction process
managable

"""
# type Hinting
from typing import List


class QueryBuilder:
    def __init__(self):
        self._query = ""
        # all query statemts stired

    def select(self, columns: List):
        self._query += f"SELECT {', '.join(columns)} "
        # give back query buildder objects
        return self

    def from_(self, table):
        # table name
        self._query += f"FROM {table} "
        return self

    def where(self, conditions: List):
        self._query += f"WHERE {' AND '.join(conditions)} "
        return self

    def order_by(self, columns: List):
        self._query += f" ORDER BY {', '.join(columns)} "
        return self

    def group_by(self, columns: List):
        self._query += f" GROUP BY {', '.join(columns)} "
        return self

    def limit(self, limit):
        self._query += f"LIMIT {limit} "
        return self

    # return genrated query
    def get_query(self):
        return self._query


if __name__ == "__main__":
    query_builder = QueryBuilder()
    # chain of query genrators
    # chaining differnt query builder
    query = (
        query_builder.select(["name", "age"])
        .from_("users")
        .where(["age > 25", "gender = 'male'"])
        .group_by(["name"])
        .order_by(["name", "age"])
        .limit(10)
        .get_query()
    )
    print(query)
