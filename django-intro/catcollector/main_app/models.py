from django.db import models

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

  
class Cat(models.Model):
     name = models.CharField(max_length=100)
     breed = models.CharField(max_length=100)
     description = models.TextField(max_length=250)
     age = models.IntegerField()
  
def __str__(self):
         return self.name

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    ) 
    # Create a cat_id FK
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)


    def __str___(self):
        return f"{self.get_meal_display()} on {self.date}"
        