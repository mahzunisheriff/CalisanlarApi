from django.urls import path
from .views import AdreslerView, CreateAdresView, UpdateAdresView, DeleteAdresView, ListAdresView, GetByIdView

urlpatterns = [
    #APIViews
    path('AdresEkle/', AdreslerView.as_view()),
    path('AdresGuncelle/<int:pk>/', AdreslerView.as_view()),

    # generics
    path('CreateAdresView/', CreateAdresView.as_view()),
    path('UpdateAdresView/<int:pk>/', UpdateAdresView.as_view()),
    path('DeleteAdresView/<int:pk>/', DeleteAdresView.as_view()),
    path('ListAdresView/', ListAdresView.as_view()),
    path('GetByIdView/<int:pk>/', GetByIdView.as_view())
]