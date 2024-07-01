"""
URL configuration for budgeting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from MAIN.views import bucket_overview, transaction_list, assign_bucket, assign_simple_description

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buckets/', bucket_overview, name='bucket_overview'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('assign_bucket/<int:transaction_id>/<int:bucket_id>/', assign_bucket, name='assign_bucket'),
    path('assign_simple_description/<int:transaction_id>/', assign_simple_description, name='assign_simple_description'),


]
