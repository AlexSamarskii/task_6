from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('ask/', views.ask_form, name='ask'),
    path('tag/<slug:tag_name>', views.tag, name='tag'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:question_id>', views.question_form, name='one_question'),
    path('admin/', admin.site.urls),
    path('profile/edit/', views.profile, name='profile'),
    path('questionLike/', views.questionLike, name='questionLike'),
    path('answerLike/', views.answerLike, name='answerLike'),
    path('correctAnswer/', views.correctAnswer, name='correctAnswer'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
