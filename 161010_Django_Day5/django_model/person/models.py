from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    @property
    def full_name(self):
        return '%s%s' % (self.last_name, self.first_name)


class School(models.Model):
    title = models.CharField(max_length=30)


class Major(models.Model):
    title = models.CharField(max_length=50)


# class Coffee(models.Model):
    num = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=30)


class Computer(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)