# from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *

class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

# __________________________________________________________________________________

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# __________________________________________________________________________________

class SubcategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

# __________________________________________________________________________________

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# __________________________________________________________________________________

class Give_offerCreateAPIView(CreateAPIView):
    queryset = Give_offer.objects.all()
    serializer_class = Give_offerSerializer

# __________________________________________________________________________________

class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# __________________________________________________________________________________

class ProductClearanceSerializer(CreateAPIView):
    queryset = ProductClearance.objects.all()
    serializer_class = ProductClearance


# __________________________________________________________________________________
    
class ProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# __________________________________________________________________________________
    
class CenterListAPIView(ListAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


# __________________________________________________________________________________
    

class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)

        return queryset
