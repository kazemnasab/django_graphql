from re import S
from turtle import title
from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene import ObjectType, String, Int, List
from .category import Mutation as CategoryMutation, Query as CategoryQuery
from .book import Mutation as BookMutation, Query as BookQuery
from django.db import models

  

class Query(graphene.ObjectType):
    hello = String(required=True, name=String())
    def resolve_hello(parent, info, **kwargs):
        name = kwargs.get('name', 'World')
        return f'Hello1, {name}!'


class SuperQuery(Query, BookQuery, CategoryQuery, graphene.ObjectType):
    pass

class SuperMutation(BookMutation, CategoryMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=SuperQuery, mutation=SuperMutation)