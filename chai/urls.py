from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.all_chai,name='all_chai'),
    path('tempview/',views.temp,name='temp'),
    path('<int:chai_id>/',views.chai_detail,name='chai_detail'),
    # path('<str:chai_type>/',views.chai_print,name='chai_print'),
    path('chai_store/',views.chai_store_view,name='chai_store'),
]
