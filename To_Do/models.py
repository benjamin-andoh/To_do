from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# user, title, category, description, task_done, start_date, end_date
class Task(models.Model):
    cat = (
        ('programming', 'programming'),
        ('bugfixing', 'bugfixing'),
        ('something', 'something'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=cat)
    description = models.TextField(blank=True)
    task_done = models.BooleanField(default=False, editable=True)
    start_date = models.DateTimeField(auto_now_add=True, editable=False)
    end_date = models.DateTimeField(null=True, editable=False)
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        name = self.title + " " + self.developer.username + " " + str(self.task_done)
        return name


# i was testing this using the shell
def send_mail(sender, instance, **kwargs):
    task = Task()
    if task.supervisor != task.developer:
        print("you have a new task")


post_save.connect(send_mail, sender=Task)