#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property, NodeMatcher

import sys
import json

from EntityFactory import *

reload(sys)

sys.setdefaultencoding('utf-8')
# https://neo4j.com/blog/py2neo-3-1-python-driver-neo4j/

'''
Neo4j 对应的Entity 映射，融合代码.
'''
class GraphAccessor():
    ## tools 类型
    #EntityType = 'Person'
    ## 匹配Node使用的key名称
    #MatchKey = 'name'

    def __init__(self):
        self.graph = Graph(host='localhost', port = 7687, password='')
        self.nodeMatcher = NodeMatcher(self.graph)

    '''
    根据 entity_type, key, value 匹配获得对应的 Node.
    @return: 
    '''
    def matchNode(self, entity_type, key, value):
        return self.graph.nodes.match(entity_type).where(' _.{} = "{}" '.format(key, value))
        #return self.nodeMatcher.match(self.graph).where(' _.{} = "{}" '.format(key, value))

    '''
    根据输入Entity获得对应的Node映射结果，返回Node对象.
    '''
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

    '''
    根据uuid查询获得对应的Node. 
    '''
    def findNode(self, uuid):
        this_node = self.graph.nodes.match(self.EntityType).where(' _.{} = "{}" '.format('uuid', uuid))
        if not this_node :
            return None
        if this_node.__len__() != 1:
            print sys.stderr << 'multiple node has same uuid.'
            return None
        return this_node.first()

    '''
    根据 entity_type, key, value 匹配获得对应的 Node.
    '''
    def findNodes(self, entity_type, key, value):
        this_node = self.graph.nodes.match(entity_type).where(' _.{} = "{}" '.format(key, value))
        return this_node

    def findNodeOne(self, entity_type, key, value):
        this_node = self.graph.nodes.match(entity_type).where(' _.{} = "{}" '.format(key, value))
        assert len(this_node) <= 1

        return this_node.first()
    '''
    Graph添加新的node, 返回node对象。
    '''
    def addNode(self, node):
        self.graph.create(node)
        return self.findNode(node.__uuid__)

    '''
    根据开始、结束结点，查询获得对应的边，可能为空；不考虑边关系。
    '''

    def findRelation(self, start_node, end_node):
        #return self.graph.relationships.match().first()
        return self.graph.match_one(nodes=[start_node, end_node])

    '''
    根据开始、结束结点以及边关系，查询获得对应的边，可能为空。
    '''
    def findRelationOne(self, start_node, end_node, r_type):
        #return self.graph.relationships.match().first()
        return self.graph.match_one(nodes=[start_node, end_node], r_type=r_type)

    '''
    删除NodeMatch下所有Node
    '''
    def deleteNodes(self, nodes):
        try:
            for n in nodes:
                self.graph.delete(n)
        except TypeError:
            try:
                self.graph.delete(nodes)
            except TypeError:
                print "deleteNodes nodes type error."

    def displyNodes(self, nodes):
        for n in nodes:
            print json.dumps(n, ensure_ascii=False)

if __name__ == '__main__':
    ## 创建若干结点，用于测试

    eric = EntityFactory.createPerson(uri = 'uri1',
                 alias = None,
                 birth_date = '1956年4月18日',
                 birth_place = '美国密西西比州',
                 blood_group = None,
                 education = None,
                 gender = '男',
                 height = '1.78m',
                 language = '英语',
                 name = '埃里克·罗伯茨',
                 name_en = None,
                 nation = '美国',
                 nationality = '美国',
                 occupation = '演员',
                 weight = None,
                 type = 'actor'
           )

    emma = EntityFactory.createPerson(uri = 'uri2',
                 alias = '小萝卜丝',
                 birth_date = '1991年2月10日',
                 birth_place = '美国密西西比州',
                 blood_group = 'A型',
                 education = '莎拉劳伦斯学院',
                 gender = '女',
                 height = '1.57m',
                 language = '英语',
                 name = '艾玛·罗伯茨',
                 name_en = None,
                 nation = '美利坚民族',
                 nationality = '美国',
                 occupation = list('演员', '歌手', '模特'),
                 weight = '42.0kg',
                 type = list('actor', 'singer', 'model'),
           )

    ab = Relationship(eric, 'parent', emma)
    ba = Relationship(emma, 'children', eric)

   # node = Node(GraphAccessor.EntityType, name = '陈凯歌', age = 21)

acc = GraphAccessor()

#print json.dumps(acc.nodeMap(node), ensure_ascii = False)
node = acc.findNodeOne('Person', 'name', '艾玛·罗伯茨')
print node
node = acc.findNodeOne('Person', 'name', '埃里克·罗伯茨')
print node
#start_node = acc.findNode('b2629c33-d07f-11e8-b578-80e6500746ca')
#end_node = acc.findNode('b262a5c2-d07f-11e8-a62e-80e6500746ca')
#end_node = acc.findNode('b2613805-d07f-11e8-8f50-80e6500746ca')

#print json.dumps(start_node, ensure_ascii = False)
#print json.dumps(end_node, ensure_ascii = False)

#print acc.findRelationOne(start_node, end_node, r_type='FRIEND')
#print acc.findRelationOne(end_node, start_node, r_type='FRIEND')

#graph.create(a)
#graph.create(ab)
