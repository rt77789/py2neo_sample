#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship
from py2neo.ogm import GraphObject, Property, RelatedTo

import uuid

# https://neo4j.com/blog/py2neo-3-1-python-driver-neo4j/
graph = Graph(host='localhost', port = 7687, password='')
graph.delete_all()


a = Node('Person',
         name = '刘德华',
         type = '演员',
         uuid = uuid.uuid1().__str__()
         )
b = Node('Person',
         name = '陈凯歌',
         type = '导演',
         uuid = uuid.uuid1().__str__()
         )
c = Node('Person',
         name = '范志毅',
         type = '运动员',
         uuid = uuid.uuid1().__str__()
         )
d = Node('Person',
         name = '陈红',
         type = '演员',
         uuid = uuid.uuid1().__str__()
         )

ab = Relationship(a, 'FRIEND', b)
ba = Relationship(b, 'FRIEND', a)
ac = Relationship(a, 'FRIEND', c)
bd = Relationship(b, 'SPOUSE', d)

graph.create(a | b | c | ab | ba | ac | bd)
#graph.create(a)
#graph.create(ab)
