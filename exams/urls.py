from django.conf.urls import url
from . import views 
app_name = 'exams'

urlpatterns = [
   
    url(r'^$', views.ExamView.as_view() , name='list'),
    url(r'^createExam$', views.create_exam , name='create-exam'),
    url(r'^createQuestion/(?P<exam>[\w-]+)$', views.create_question_form , name='create-question'),
    url(r'^createSolution$', views.create_solution, name='create-solution'),
    url(r'^createAnswer$', views.create_answer, name='create-answer'),
    url(r'^updateQuestion$', views.update_question, name='update-answer'),
    url(r'^assignExam/(?P<slug>[\w-]+)$', views.assign_exam, name='assign-exam'),
    url(r'^deleteExam/(?P<slug>[\w-]+)$', views.delete_exam, name='delete-exam'),
    url(r'^editQuestion/(?P<exam>[\w-]+)/(?P<number>[\w-]+)$', views.edit_question, name='edit-question'),
    url(r'^markExam$', views.mark_exam, name='mark-exam'),
    url(r'^(?P<slug>[\w-]+)$', views.view_full_exam, name='view-exam'),
   
    
    # url(r'^edit$', views.ExamView.editTest),
    # url(r'^addtest$', views.ExamView.as_view(), name='addtest')
]