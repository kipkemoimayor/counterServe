from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
# router.register(r'user-list',views.UserList)

# add your paths here
urlpatterns = [
    path('', include(router.urls)),
    # path('user-list/', views.UserList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
