from rest_framework import serializers
from .models import *
from user.models import User
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# _____________________________________________________________________________

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# _____________________________________________________________________________

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"

# __________________________________________________________________________

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

# ___________________________________________________________________________

class Give_offerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Give_offer
        fields = "__all__"

# ___________________________________________________________________________

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

# __________________________________________________________________________

class ProductClearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClearance
        fileds = "__all__"

# _________________________________________________________________________


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'color', 'size', 'description', 'product_count', 'price', 'created_at')
        read_only_fields = ('id', 'title', 'image', 'color', 'size', 'description', 'price', 'created_at')
        changes = ('product_count',)

# ________________________________________________________________________

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)

# ________________________________________________________________________

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category')


# ________________________________________________________________________
        
class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('id', 'name')

# ________________________________________________________________________


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'color', 'size', 'description', 'product_count', 'price', 'created_at')