from django.db import models
from users.models import  Product
from user.models import User


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.created_at} - {self.updated_at}"


class AddDelete(BaseModel):
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    product_count = models.ForeignKey(Product, on_delete=models.PROTECT)
    deleted_at = models.DateField(auto_now=True)
    text_answer_date = models.DateField(auto_now_add=True)
    answer = models.CharField(max_length=200)


    def __str__(self):
        return self.id




class Center(models.Model):
    name = models.CharField(max_length=1000)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.id
