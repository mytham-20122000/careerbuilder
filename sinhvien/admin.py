from django.contrib import admin
from .models import Job, SkillPhu, SkillChinh, SkillJob, JobSkill
# Register your models here.

admin.site.register(Job)

admin.site.register(SkillPhu)
admin.site.register(SkillChinh)
admin.site.register(SkillJob)
admin.site.register(JobSkill)
