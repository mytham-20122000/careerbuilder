from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Job, SkillPhu, SkillChinh, SkillJob, JobSkill
from .forms import JobForm, SkillPhuForm, SkillChinhForm
from .forms import JobUpdateForm, SkillPhuUpdateForm, SkillChinhUpdateForm

class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'
class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobUpdateForm
    template_name = 'job_update_form.html'
    
class SkillPhuListView(ListView):
    model = SkillPhu
    template_name = 'skillphu_list.html'
class SkillPhuDetailView(DetailView):
    model = SkillPhu
    template_name = 'skillphu_detail.html'
class SkillPhuCreate(LoginRequiredMixin, CreateView):
    model = SkillPhu
    form_class = SkillPhuForm
    template_name = 'skillphu_form.html'
class SkillPhuUpdate(LoginRequiredMixin, UpdateView):
    model = SkillPhu
    form_class = SkillPhuUpdateForm
    template_name = 'skillphu_update_form.html'

class SkillChinhListView(ListView):
    model = SkillChinh
    template_name = 'skillchinh_list.html'
class SkillChinhDetailView(DetailView):
    model = SkillChinh
    template_name = 'skillchinh_detail.html'
class SkillChinhCreate(LoginRequiredMixin, CreateView):
    model = SkillChinh
    form_class = SkillChinhForm
    template_name = 'skillchinh_form.html'
class SkillChinhUpdate(LoginRequiredMixin, UpdateView):
    model = SkillChinh
    form_class = SkillChinhUpdateForm
    template_name = 'skillchinh_update_form.html'




class JobSkillListView(ListView):
    model = JobSkill
    template_name = 'jobskill_list.html'
class JobSkillDetailView(DetailView):
    model = JobSkill
    template_name = 'jobskill_detail.html'


class SkillJobListView(ListView):
    model = SkillJob
    template_name = 'skilljob_list.html'
class SkillJobDetailView(DetailView):
    model = SkillJob
    template_name = 'skilljob_detail.html'

