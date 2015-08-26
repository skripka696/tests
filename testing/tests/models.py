from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Question(models.Model):
    theme = models.ForeignKey(Theme)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '{0}'.format(self.name)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=255)
    status = models.BooleanField()

    def __unicode__(self):
        return '{0} {1}'.format(self.answer, self.status)


class StatusTest(models.Model):
    user = models.ForeignKey(User)
    status_question = models.ForeignKey(Question)
    status_answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return '{0} {1}'.format(self.question, self.answer)
