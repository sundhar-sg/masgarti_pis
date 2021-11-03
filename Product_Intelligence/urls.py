from django.urls import path, include
from . import views

urlpatterns = [
    path('admin-dashboard', views.admin_dashboard, name='admindashboardview'),
    path('', views.homepage, name='homepage'),
    path('user-login', views.loginpage, name='loginview'),
    path('user-signup', views.signuppage, name='signupview'),
    path('', views.logout, name='logoutview'),
    path('user-signup-success', views.signupsuccess, name='signupsuccessview'),
    path('user-details', views.user_accounts, name='user-details-view'),
    path('edit-user-details', views.edit_user_accounts, name='edit-user-details'),
    path('edit-user-password', views.edit_user_password, name='edit-user-password'),
    path('customization-page', views.customization_page, name='customization_page_view'),
    path('electronics/', views.electronics, name='electronics'),
    path('clothing/', views.clothing, name='clothing'),
    path("clothing/MensTShirts/", views.menstshirts, name='menstshirts'),
    path("clothing/WomensTShirts/", views.womenstshirts, name='womenstshirts'),
    path("clothing/OfficeWears/", views.officewearstore, name='officewearstore'),
    path('electronics/CustomLaptops/', views.laptopsstore, name='laptopsstore'),
    path('electronics/CustomTablets/', views.tabletsstore, name='tabletsstore'),
    path('business_promotions/', views.business_promotions, name='business_promotions'),
    path('business_promotions/Flyers', views.flyerstore, name='flyerstore'),
    path('business_promotions/Brochures', views.brochurestore, name='brochurestore'),
    path('business_promotions/LetterHeads', views.letterheadstore, name='letterheadstore'),
    path('business_promotions/VisitingCards', views.visitingcardstore, name='visitingcardstore'),
    path('business_promotions/PostalCovers', views.postalcoverstore, name='postalcoverstore'),
]