"""iskedyul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path("test", views.TestView.as_view(), name="test"),
    path("", views.TimetableListView.as_view(), name="set_list"),
    path("table/new/", views.TimetableCreateView.as_view(), name="set_create"),
    path("table/<int:pk>/", views.TimetableDetailView.as_view(), name="set_detail"),
    path("table/<int:pk>/edit/", views.TimetableUpdateView.as_view(), name="set_update"),
    path("table/<int:pk>/delete/", views.TimetableDeleteView.as_view(), name="set_delete"),
    # blocks
    path("table/<int:set_id>/event/new/", views.EventCreateView.as_view(), name="block_create"),
    path("table/<int:set_id>/event/<int:pk>/edit/", views.EventUpdateView.as_view(), name="block_update"),
    path("table/<int:set_id>/event/<int:pk>/delete/", views.EventDeleteView.as_view(), name="block_delete"),
]
