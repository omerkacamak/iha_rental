from django.db import models
from django.contrib.auth.models import User
from iha.models import Iha

class RentalOperation(models.Model):
    process_number = models.CharField(max_length=10, unique=True)
    renting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rental_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    end_date = models.DateField()
 
    def __str__(self):
       return f"[{self.renting_user}] - {self.iha} - {self.created_at} - {self.end_date}" 

    class Meta:
        models.UniqueConstraint(
            fields=['user','created_at','end_date'], name= 'user_rentalOperation_date'
        )

    

