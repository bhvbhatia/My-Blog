from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [

      path('',views.home,name='home'),
      path('about/',views.about,name='about'),
      path('blog/<int:pk>/',views.detail,name='detail'),
      path('cv/',views.cv,name='cv'),
      path('login/',views.login_view,name='login'),
      path('logout/',views.logout_view,name='logout'),
      path('register/',views.register,name='register'),
      path('blog/<int:pk>/comment/', views.comment_form, name='comment_form'),
      path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
      path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
      path('post/new/', views.CreatePostView.as_view(), name='post_new'),
      path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
      path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),


]
