# from django.core.management.base import BaseCommand
# import factory  
# import factory.django
# from driver.models import *
# # User=get_user_model()

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.Faker('username')
#     password = factory.LazyFunction(lambda: make_password('nikosklaime'))
#     is_staff = False
#     is_superuser = False
#     # store = factory.RelatedFactory(storeFactory, 'user')
#     # driver = factory.RelatedFactory(driverFactory, 'user')

# class driverFactory(factory.django.DjangoModelFactory):  
#     class Meta:
#         model = driver

#     first_name = factory.Faker('first_name')
#     last_name = factory.Faker('last_name')
#     phoneNo = factory.Faker('phoneNo')
#     user = factory.Iterator(settings.AUTH_USER_MODEL.objects.filter(id__lte=50))


# class storeFactory(factory.django.DjangoModelFactory):  
#     class Meta:
#         model = store

#     name = factory.Faker('name')
#     adress = factory.Faker('adress')
#     phone = factory.Faker('phone')
#     user = factory.Iterator(contrib.auth.models.user.objects.filter(id__gte=51))
#     driver = factory.Iterator(models.driver.objects.all())


# class orderFactory(factory.django.DjangoModelFactory):  
#     class Meta:
#         model = order

#     time_to_pickup = factory.Faker('time_to_pickup')
#     adress_to = factory.Faker('adress_to')
#     price = factory.Faker('price')
#     running_now = factory.Faker('running_now')
#     isDelivered = factory.Faker('isDelivered')
#     store = factory.Iterator(models.store.objects.all())



# class Command(BaseCommand):
#     help = 'Seeds the database.'

#     def add_arguments(self, parser):
#         parser.add_argument('--drivers',
#             default=50,
#             type=int,
#             help='The number of fake drivers to create.')
        
#         parser.add_argument('--stores',
#             default=50,
#             type=int,
#             help='The number of fake stores to create.')

#         parser.add_argument('--orders',
#             default=50,
#             type=int,
#             help='The number of fake orders to create.')

#         parser.add_argument('--users',
#             default=100,
#             type=int,
#             help='The number of fake orders to create.')

#     def handle(self, *args, **options):
#         for _ in range(options['users']):
#             UserFactory().create()
#         for _ in range(options['drivers']):
#             driverFactory.create()
#         for _ in range(options['stores']):
#             storeFactory().create()
#         for _ in range(options['orders']):
#             orderFactory().create()
        