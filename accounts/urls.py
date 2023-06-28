from django.urls import path
from .views import profile , profile_edit , signup , my_reservation




app_name='accounts'




urlpatterns = [
    #path('<str:username>/activate', user_activate, name = 'user_activate'),
    #path('dashboard',dashboard,name='dashboard'),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/edit', profile_edit , name='profile_edit'),
    path('profile/booking', my_reservation , name='my_reservation'),
    

]
