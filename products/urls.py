from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addProduct', views.add),
    path('showProduct',views.show),
    path('editProduct/<int:id>', views.edit),
    path('updateProduct/<int:id>', views.update),
    path('deleteProduct/<int:id>', views.destroy),
    ]

