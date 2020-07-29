Ticket System notes.

using the faker
>>> from To_Do.models import Task
>>> from faker import Faker
>>> faker = Faker()
>>> faker.name()

py manage.py shell
from django.contrib.auth.models import User
user = User.objects.create(username='kojo')
user1 = User.objects.create(username='kwesi')
from To_Do.models import Task
user  = User.objects.get(username='andoh')
task = Task.objects.create(title='Java', category='something', description
='it is not part', developer=user1, supervisor=user)

