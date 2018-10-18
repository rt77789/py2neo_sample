#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property, NodeMatcher

import sys
import json

from EntityFactory import *
from GraphAccessor import *

if __name__ == '__main__':

    acc = GraphAccessor()

    nodes = acc.findNodes('Person', 'name', '艾玛·罗伯茨')
    acc.displyNodes(nodes)
    if len(nodes) <= 1 and nodes.first():
        this_node = nodes.first()
        this_node['occupation'].append('美女')
        acc.graph.push(this_node)
    acc.displyNodes(nodes)
    #acc.deleteNodes(nodes)

    nodes = acc.findNodeOne('Person', 'name', '埃里克·罗伯茨')
    acc.displyNodes(nodes)
    #acc.deleteNodes(nodes)



#start_node = acc.findNode('b2629c33-d07f-11e8-b578-80e6500746ca')
#end_node = acc.findNode('b262a5c2-d07f-11e8-a62e-80e6500746ca')
#end_node = acc.findNode('b2613805-d07f-11e8-8f50-80e6500746ca')

#print json.dumps(start_node, ensure_ascii = False)
#print json.dumps(end_node, ensure_ascii = False)

#print acc.findRelationOne(start_node, end_node, r_type='FRIEND')
#print acc.findRelationOne(end_node, start_node, r_type='FRIEND')

#graph.create(a)
#graph.create(ab)
