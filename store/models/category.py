from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)



    @staticmethod
    def get_all_Categories():
        return Category.objects.all()    # get categories from database



    def __str__(self):
        return self.name

