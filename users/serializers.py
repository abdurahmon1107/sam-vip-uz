from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
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

# _____________________________________________________________________________

# class ProductColorsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductColors
#         fields = "__all__"

# ____________________________________________________________________________

# class ProductImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImages
#         fields = "__all__"

# ___________________________________________________________________________

# class ProductSizeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductSize
#         fields = "__all__"

# ___________________________________________________________________________

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

# ___________________________________________________________________________

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
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




