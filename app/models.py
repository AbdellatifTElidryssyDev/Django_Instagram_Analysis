from django.db import models


class Insight(models.Model):
    follower = models.IntegerField('Follower')
    follows = models.IntegerField('Follow')
    label = models.CharField('Created date', max_length=100)

    def __str__(self):
        return str(self.label)


class Post(models.Model):
    like = models.IntegerField('How nice')
    comments = models.IntegerField('comment')
    count = models.IntegerField('Number of posts')
    label = models.CharField('Posted date', max_length=100)

    def __str__(self):
        return str(self.label)


class HashTag(models.Model):
    tag = models.CharField('hashtag', max_length=100)
    count = models.IntegerField('Number of posts')
    label = models.CharField('Posted date', max_length=100)

    def __str__(self):
        return str(self.label) + ':' + str(self.tag)
