#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeMatch
from py2neo.ogm import GraphObject, Property, NodeMatcher

import sys
import json

from GraphAccessor import *
from EntityFactory import *

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
                 occupation = ['演员', '歌手', '模特'],
                 weight = '42.0kg',
                 type = ['actor', 'singer', 'model'],
           )

    ab = Relationship(eric, 'parent', emma)
    ba = Relationship(emma, 'children', eric)

   # node = Node(GraphAccessor.EntityType, name = '陈凯歌', age = 21)

    acc = GraphAccessor()
    acc.graph.delete_all()
    acc.graph.create(eric | emma | ab | ba)