from rest_framework import serializers
from . import models
from users.models import Product


class AddDelete(serializers.ModelSerializer):

    all_price = serializers.DecimalField(max_digits=2, decimal_places=10)

    class Meta:
        model = models.AddDelete
        fields = ('client', 'product_count', 'deleted_at', 'text_answer_date', 'answer', 'all_price')


    def get_all_price(self):
        return Product.product_count * self.all_price
    