from django.urls import path
from bigbasketapp import views
app_name="bigbasketapp"

urlpatterns=[
    path('',views.index,name='index'),
    path('customer_register/',views.customer_register,name='customer_register'),
    path('vendor_register/',views.vendor_register,name='vendor_register'),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('base/',views.base,name='base')
]