"""URL configuration for rsum.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# pylint: disable=invalid-name
# from django.contrib import admin
from django.urls import path
# from django.urls import re_path

import home.views
import export.views

urlpatterns = [
    path('', home.views.index, name='main'),
    path('docx/', export.views.index, {'graphics': True}, name='docx'),
    path(
        'docx/boring', export.views.index, {'graphics': False}, name='boring'),
    path('thecraiglist/', home.views.thecraiglist, name='thecraiglist'),
]
