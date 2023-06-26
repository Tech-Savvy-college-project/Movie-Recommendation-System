from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from accounts import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router = DefaultRouter()
# router.register("login",views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('user/', include('authentication.urls')),
    #path('api/user/',include('account.urls'))
#    path('api/user/',include('profiles.urls'))
#    path('api/account/',include('accounts.urls')),
   path('regi/',include('users.urls')),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#    path('movie')
]

# urlpatterns += router.urls
