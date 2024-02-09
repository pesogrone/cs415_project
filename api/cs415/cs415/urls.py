"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cs415 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserAPIView.as_view()),
    # path('categories/', views.CategoriesAPIView.as_view()),
    # path('items/', views.ItemsAPIView.as_view()),
    # path('orders/', views.OrdersAPIView.as_view()),
    # path('payment/', views.PaymentAPIView.as_view()),
    # path('profile/', views.ProfileAPIView.as_view()),
    # path('reviews/', views.ReviewsAPIView.as_view()),
    # path('transactions/', views.TransactionsAPIView.as_view()),

    path('users/user/<int:id>/', views.SingleUserAPIView.as_view()),
    # path('categories/category/<int:id>/', views.SingleCategoryAPIView.as_view()),
    # path('items/item/<int:id>/', views.SingleItemAPIView.as_view()),
    # path('orders/order/<int:id>/', views.SingleOrderAPIView.as_view()),
    # path('payment/payment/<int:id>/', views.SinglePaymentAPIView.as_view()),
    # path('profile/profile/<int:id>/', views.SingleProfileAPIView.as_view()),
    # path('reviews/review/<int:id>/', views.SingleReviewAPIView.as_view()),
    # path('transactions/transaction/<int:id>/', views.SingleTransactionAPIView.as_view()),

]
