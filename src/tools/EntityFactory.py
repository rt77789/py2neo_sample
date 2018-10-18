#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import json
import uuid


from py2neo import Graph, Node, Relationship, NodeMatch

# https://neo4j.com/blog/py2neo-3-1-python-driver-neo4j/

'''
Define the tools Type Prototype, e.g. Person, Movie, Book etc.

Person tools is defined as follows.
'''


class EntityFactory():

    @staticmethod
    def createPerson(
                 uri = None,
                 alias = None,
                 birth_date = None,
                 birth_place = None,
                 blood_group = None,
                 education = None,
                 gender = None,
                 height = None,
                 language = None,
                 name = None,
                 name_en = None,
                 nation = None,
                 nationality = None,
                 occupation = None,
                 weight = None,
                 type = None
                 ):

        return Node('Person',
                    uuid = uuid.uuid1().__str__(),
                    uri=uri,
                    alias=alias,
                    birth_date=birth_date,
                    birth_place=birth_place,
                    blood_group=blood_group,
                    education=education,
                    gender=gender,
                    height=height,
                    language=language,
                    name=name,
                    name_en=name_en,
                    nation=nation,
                    nationality=nationality,
                    occupation=occupation,
                    weight=weight,
                    type=type
                    )


