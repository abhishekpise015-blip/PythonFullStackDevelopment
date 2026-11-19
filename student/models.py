from django.db import models

class Student_table(models.Model):
    reg_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(default='example@gmail.com')
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.reg_no}"