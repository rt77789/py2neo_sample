#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property, NodeMatcher

import sys
import json

from EntityFactory import *
from GraphAccessor import *

class BaikeLoader:
    acc = GraphAccessor()

    def __init__(self):
        pass

    def insertNodes(self, filename):
        ## open file and insert line by line.
        with open(filename) as fin:
            line = fin.readline()
            while line :
                o = json.loads(line)

                ## 如果已经存在当前uri的Node，则忽略该Entity
                if not self.acc.findNodes('Person', key='uri', value=o['/people/person/uri']):
                    node = EntityFactory.createPerson(
                        uri=o['/people/person/uri'],
                        alias=o['/people/person/alias'],
                        birth_date=o['/people/person/birth_date'],
                        birth_place=o['/people/person/birth_place'],
                        blood_group=o['/people/person/blood_group'],
                        education=o['/people/person/education'],
                        gender=o['/people/person/gender'],
                        height=o['/people/person/height'],
                        language=o['/people/person/language'],
                        name=o['/people/person/name'],
                        name_en=o['/people/person/name_en'],
                        nation=o['/people/person/nation'],
                        nationality=o['/people/person/nationality'],
                        occupation=o['/people/person/occupation'],
                        weight=o['/people/person/weight'],
                        type='Person'
                    )
                    self.acc.graph.create(node)

                line = fin.readline()

            fin.close()

    def insertRelations(self, filename):
        ## open file and insert line by line.
        with open(filename) as fin:
            line = fin.readline()
            while line :
                tk = line.strip().split(',')
                assert(len(tk) == 3)
                print 'start_node={},end_node={}'.format(tk[0].strip(), tk[2].strip())
                start_node = self.acc.findNodeOne('Person', key='uri', value=tk[0].strip())
                end_node = self.acc.findNodeOne('Person', key='uri', value=tk[2].strip())

                ### 如果起始Node都存在，且没有同样关系的边，则插入；否则忽略
                if len(start_node) >= 1 and len(end_node) >= 1:
                    ab = Relationship(start_node, tk[1].strip(), end_node)
                    if not self.acc.findRelationOne(start_node=start_node, end_node=end_node, r_type=tk[1].strip()):
                        self.acc.graph.create(ab)

                line = fin.readline()

            fin.close()

if __name__ == '__main__':

    loader = BaikeLoader()
    BaikeLoader.acc.graph.delete_all()

    loader.insertNodes('../../data/nodes_json_sample.txt')
    loader.insertRelations('../../data/relation_csv_sample.txt')
