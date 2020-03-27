"""Smash_Pros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from smash_app.models import Player, Character, Match

# admin

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username']
admin.site.register(Player, PlayerAdmin)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
admin.site.register(Character, CharacterAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ['winner',  'loser','tourney', 'round', 'date']
    
admin.site.register(Match, MatchAdmin)

# path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("smash_app.urls")),	
]

# images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

