import datetime
from math import sqrt

from django.core.mail import send_mail

from myproj.celery_app import app
from users.models import Users


@app.task(name="users.tasks.square_root")
def square_root(value):
   return sqrt(value)


@app.task(name="users.tasks.send_message")
def send_message():
   users = Users.objects.all()
   for user in users:
      send_mail("Test subject",
                "Hello!",
                recipient_list=[user.user.email,],
                from_email="test@test.com")


@app.task(name="users.tasks.inactivate_user")
def inactivate_user():
   users = Users.objects.all()
   for user in users:
      not_logged = datetime.datetime.now(datetime.timezone.utc) - user.last_login
      if not_logged.days > 30:
         user.user.is_active = False
         user.user.save()
