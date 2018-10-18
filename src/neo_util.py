#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property, NodeMatcher

import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

# https://neo4j.com/blog/py2neo-3-1-python-driver-neo4j/

'''
Neo4j 对应的Entity 映射，融合代码.
'''
class NeoAccessor():
    ## tools 类型
    EntityType = 'Person'
    ## 匹配Node使用的key名称
    MatchKey = 'name'

    def __init__(self):
        self.graph = Graph(host='localhost', port = 7687, password='')
        self.nodeMatcher = NodeMatcher(self.graph)

    def matchNode(self, key, value):
        return self.graph.nodes.match(self.EntityType).where(' _.{} = "{}" '.format(key, value))
        #return self.nodeMatcher.match(self.graph).where(' _.{} = "{}" '.format(key, value))

    def nodeMap(self, node):
        key = self.MatchKey
        value = node[key]
        node_list = self.matchNode(key, value)
        if node_list.__len__() > 0:
            ## 源Entity -> Neo4j Entity映射计算，获得对应的Entity ID
            return node_list.first()
        else:
            ## 如果Neo4j 暂无当前Entity，则添加新的Node
            return self.addNode(node)
        return None

    def findNode(self, uuid):
        this_node = self.graph.nodes.match(self.EntityType).where(' _.{} = "{}" '.format('uuid', uuid))
        if not this_node :
            return None
        if this_node.__len__() != 1:
            print sys.stderr << 'multiple node has same uuid.'
            return None
        return this_node.first()

    def findNodeOne(self, key, value):
        this_node = self.graph.nodes.match(self.EntityType).where(' _.{} = "{}" '.format(key, value))
        return this_node

    def addNode(self, node):
        self.graph.create(node)
        return self.findNode(node.__uuid__)

    def findRelationOne(self, start_node, end_node, r_type):
        #return self.graph.relationships.match().first()
        return self.graph.match_one(nodes=[start_node, end_node], r_type=r_type)

node = Node(NeoAccessor.EntityType, name = '陈凯歌', age = 21)

acc = NeoAccessor()
print json.dumps(acc.nodeMap(node), ensure_ascii = False)

start_node = acc.findNode('b2629c33-d07f-11e8-b578-80e6500746ca')
#end_node = acc.findNode('b262a5c2-d07f-11e8-a62e-80e6500746ca')
end_node = acc.findNode('b2613805-d07f-11e8-8f50-80e6500746ca')

print json.dumps(start_node, ensure_ascii = False)
print json.dumps(end_node, ensure_ascii = False)

print acc.findRelationOne(start_node, end_node, r_type='FRIEND')
print acc.findRelationOne(end_node, start_node, r_type='FRIEND')

#graph.create(a)
#graph.create(ab)
