from django.db import models

# Create your models here.
class TestCrud(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)

    # Create / Insert / Add - GET
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE