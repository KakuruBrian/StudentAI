"""

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a92f767-cc50-4cd9-a031-af9004f8c72e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
]