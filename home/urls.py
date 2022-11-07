from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = "Anshuman Admin"
admin.site.site_title = "Portfolio Portal"
admin.site.index_title = "Welcome to Anshuman Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('verify', views.verify, name='verify'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout_fun,name='logout_fun'),
    path('delete/', views.delete_session),
]