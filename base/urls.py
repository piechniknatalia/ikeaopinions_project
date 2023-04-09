from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('opinion/<str:pk>/', views.opinion, name="opinion"),
    path('', views.home, name="home"),
    path('opinionsproduct/<str:pn>/', views.opinions_by_product, name="opinions_by_product"),
    path('opinionsname/<str:nm>/', views.opinions_by_name, name="opinions_by_name"),
    path('createanopinion/', views.createOpinion, name="createanopinion"),
    path('deleteopinion/<str:pk>/', views.deleteOpinion, name="deleteopinion"),
    path('deleteopinion/<str:pko>/<str:pkc>/', views.deleteComment, name="deletecomment")
]