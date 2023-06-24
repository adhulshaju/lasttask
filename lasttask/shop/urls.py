from django.urls import path, include
from . import views
from .views import load_courses

app_name='shop'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('school/',views.school,name='school'),
    path('school/schoolform/',views.scholform,name='schoolform'),
    path('shop/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),

]