from django.urls import path
from . import views
from stackusers.views import user_questions_list

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('products/', views.products, name="products"),
    path('teams/', views.teams, name="teams"),
    path('developers/', views.dev, name="dev"),
     path('collab/', views.bus, name="bussiness"),





    # CRUD Function
    path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="question-create"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="question-detail"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="question-update"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name="question-delete"),
    path('questions/<int:pk>/comment/', views.AddCommentView.as_view(), name="question-comment"),
    path('like/<int:pk>', views.like_view, name="like_post"),
    path('my-questions/',user_questions_list, name='user_questions_list'),

]
