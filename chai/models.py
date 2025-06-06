from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# one to many

class ChaiReview(models.Model):
    RATING = [
        ('1', 'NOT_GOOD'),
        ('2', 'GOOD'),
        ('3', 'AVERAGE'),
        ('4', 'BEST'),
        ('5', 'BETTER'),
    ]
    chai = models.ForeignKey(ChaiVarity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField(max_length=1,choices=RATING)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    

#many to mamy

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity,related_name='stores')

    def __str__(self):
        return self.name
    

#one to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField

    def __str__(self):
        return f'certificate for {self.name.chai}'

