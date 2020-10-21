from django.conf.urls import url
from . import views 
app_name = 'exams'

urlpatterns = [
   
    url(r'^$', views.ExamView.as_view() , name='list'),
    url(r'^createExam$', views.create_exam , name='create-exam'),
    url(r'^createQuestion$', views.create_question , name='create-question'),
    url(r'^createSolution$', views.create_solution, name='create-solution'),
    url(r'^createAnswer$', views.create_answer, name='create-answer'),
    url(r'^viewExam$', views.view_full_exam, name='view-exam'),
    
    # url(r'^edit$', views.ExamView.editTest),
    # url(r'^addtest$', views.ExamView.as_view(), name='addtest')
]