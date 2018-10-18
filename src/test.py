from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property

# https://neo4j.com/blog/py2neo-3-1-python-driver-neo4j/

class Person(GraphObject):
    __primarykey__ = "name"

    name = Property()
    id = Property()


graph = Graph(host='localhost', port = 7687, password='')

graph.nodes.match("Person", name='Bob')
print GraphObject.match(graph).where('_.name = "Bob"')

#graph.create(a)
#graph.create(ab)
