from email.policy import default
import graphene
from graphene_django import DjangoObjectType
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class CategoryType(DjangoObjectType):
     class Meta: 
        model = Category
        fields = ('id','title')

class Query(graphene.ObjectType):
    categories = graphene.List(
        CategoryType,
        title=graphene.String(),
        id=graphene.Int()
    )

    category = graphene.Field(
        CategoryType,
        id=graphene.Int()
    )

    def resolve_category(root, info, **kwargs):
        id = kwargs.get('id', 0)
        category = Category.objects.get(pk=id)
        return category

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        id = kwargs.get('id', 0)
        title = kwargs.get('title', "")
        dd = Category.objects.all()
        if(id > 0):
            dd = dd.filter(id=id)
        if(title != ""):
            dd = dd.filter(title!=title);
        return dd

class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        title = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title="eeeeeeee"):
        category = Category()
        category.title = title
        category.save()
        return CreateCategory(category=category)
    
    def validate(self, fields):
        title = fields.get('title', None)
        raise graphene.FieldError('fields are the same value')


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category= CreateCategory.Field()
