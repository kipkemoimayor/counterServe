from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.utils import timezone
from rest_framework import status


from .serializers import GroupSerializer, UserSerializer, PostSerializer
from .models import Post

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = (AllowAny,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-pub_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     print(self.request)
    #     serializer.save(user=self.request.user.id)
# class UserList(APIView):
#     serializer_class = [TemplateHTMLRenderer]
#     template_name = '/users/view_users.html',

#     def get(self, request):
#         users = User.objects.all()
#         return Response({'users': users})


def users(request):
    users = requests.get('http://127.0.0.1:8000/users',
                         auth=('collo', 'Collins@24'))
    users_list = users.json()
    # users_list=users_list['results']
    print(users_list['results'])
    return render(request, 'users/view_users.html', {"users": users_list['results']})
