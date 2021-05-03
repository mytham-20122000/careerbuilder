from django.urls import path
from . import views
from sinhvien.views import JobListView, JobDetailView, JobCreate, JobUpdate
from sinhvien.views import SkillPhuListView, SkillPhuDetailView, SkillPhuCreate,SkillPhuUpdate
from sinhvien.views import SkillChinhListView, SkillChinhDetailView, SkillChinhCreate,SkillChinhUpdate
from sinhvien.views import SkillJobListView, SkillJobDetailView
from sinhvien.views import JobSkillListView, JobSkillDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.Detail, name="Detail"),
        
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/detail/<int:pk>', JobDetailView.as_view(), name='job-detail'),
    path('job/create/', JobCreate.as_view(), name='job-create'),
    path('job/update/<int:pk>',  JobUpdate.as_view(), name='job-update'),

    path('skillphu/', SkillPhuListView.as_view(), name='skillphu-list'),
    path('skillphu/detail/<int:pk>', SkillPhuDetailView.as_view(), name='skillphu-detail'),
    path('skillphu/create/', SkillPhuCreate.as_view(), name='skillphu-create'),
    path('skillphu/update/<int:pk>',  SkillPhuUpdate.as_view(), name='skillphu-update'),

    path('skillchinh/', SkillChinhListView.as_view(), name='skillchinh-list'),
    path('skillchinh/detail/<int:pk>', SkillChinhDetailView.as_view(), name='skillchinh-detail'),
    path('skillchinh/create/', SkillChinhCreate.as_view(), name='skillchinh-create'),
    path('skillchinh/update/<int:pk>',  SkillChinhUpdate.as_view(), name='skillchinh-update'),

    path('skilljob/', SkillJobListView.as_view(), name='skilljob-list'),
    path('skilljob/detail/<int:pk>', SkillJobDetailView.as_view(), name='skilljob-detail'),

    path('jobskill/', JobSkillListView.as_view(), name='jobskill-list'),
    path('jobskill/detail/<int:pk>', JobSkillDetailView.as_view(), name='jobskill-detail'),
]