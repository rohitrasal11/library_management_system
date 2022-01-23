from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=100)
    publish_date=models.DateField()
    author=models.CharField(max_length=100)

    class Meta:
        db_table="books"
