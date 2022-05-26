import graphene
from graphene_django import DjangoObjectType
from ..models import Category, Book, Grocery


class BookType(DjangoObjectType):
    class Meta: 
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages', 
            'price',
            'quantity', 
            'description',
            'imageurl',
            'status',
            'date_created',
        )  

class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created',
        )

class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()


class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    pages = graphene.Int()
    price = graphene.Int()
    quantity = graphene.Int()
    description = graphene.String()
    status = graphene.String()

class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        book = Product.objects.get(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = decimal.Decimal(input.price)
        book.quantity = input.quantity
        book.save()
        return UpdateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
