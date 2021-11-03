from django.db import models

# Create your models here.
class user_details_db(models.Model) :
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, primary_key=True)
    mobilenumber = models.CharField(max_length=20)
    password = models.BinaryField()
    saltvalue = models.BinaryField()
    class Meta:
        db_table: 'user_details_db'