from django.urls import path

from . import views

urlpatterns = [
	path('', views.addExpenseEarningView,name='addexpenseearning')
]