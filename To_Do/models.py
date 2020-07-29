from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# user, title, category, description, task_done, start_date, end_date
from django.dispatch import receiver


class Task(models.Model):
    cat = (
        ('p', 'programming'),
        ('b', 'bugfixing'),
        ('s', 'something'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=cat)
    description = models.TextField(blank=True)
    task_done = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, editable=False)
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='developer')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervisor')

    def __str__(self):
        name = f"{self.title} {self.developer.username}  {self.task_done}"
        return name


# i was testing this using the shell
def send_mail(sender, *args, **kwargs):
    task = kwargs['instance']
    if kwargs['created']:
        if task.supervisor != task.developer:
            print("you have a new task")


post_save.connect(send_mail, sender=Task)



