from .views import CreateOtzivView
from django.urls import path, include


urlpatterns = [
    path('', CreateOtzivView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # new

]
