from django.urls import path
from app_customer import views
urlpatterns = [
    
   path('', views.home, name='home'),
   path('create_user/', views.createUser, name='create_user'),  
   path('read_user/', views.readUser, name='read_user'),  
   path('update_user/<int:id>', views.updateUser, name='update_user'),
   path('delete_user/<int:id>', views.deleteUser, name='delete_user'),
   path('create_company', views.createCompany, name='create_company'),
   path('read_companies', views.readCompany, name='read_companies'),
   path('update_company/<int:id>', views.updateCompany, name='update_company'),
   path('delete_company/<int:id>', views.deleteCompany, name='delete_company'),
    
 ]
