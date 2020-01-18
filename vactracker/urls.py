"""vactracker URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from board import views as board_views
from calen import views as calen_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$',board_views.home,name='home'),
    url(r'^addemployee$',board_views.addemployee,name='addemployee'),
    url(r'^deleteemployee$',board_views.deleteemployee,name='deleteemployee'),
    url(r'^manageEmployee$',board_views.manageEmployee,name='manageEmployee'),
    url(r'^calendar/$', calen_views.CalendarView.as_view(), name='calendar'),
    url(r'^updateVacation/$',calen_views.updateVacation,name='updateVacation'),
    url(r'^event/new/$', calen_views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', calen_views.event, name='event_edit'),
    url(r'^deleteVacation$',board_views.deleteVacation,name='deleteVacation'),
]
