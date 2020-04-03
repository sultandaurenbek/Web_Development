from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='description')
    city = models.CharField(max_length=100)
    address = models.TextField(default='address')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='description')
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }