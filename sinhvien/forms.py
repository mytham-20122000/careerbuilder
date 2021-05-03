from django.forms import ModelForm
from .models import Job, SkillPhu, SkillChinh, JobSkill, SkillJob

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        labels = {
            'ma_viec_lam': 'Mã việc làm',
            'ten_viec_lam':  'Tên việc làm',
            'ten_ky_nang': 'Kỹ năng yêu cầu',
            'cap_do': 'Cấp độ yêu cầu',
        }
class JobUpdateForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        labels = {
            'ma_viec_lam': 'Mã việc làm',
            'ten_viec_lam':  'Tên việc làm',
            'ten_ky_nang': 'Kỹ năng yêu cầu',
            'cap_do': 'Cấp độ yêu cầu',
        }


class SkillPhuForm(ModelForm):
    class Meta:
        model = SkillPhu
        fields = '__all__'
        labels = {
            'ma_sinh_vien': 'Mã Sinh Viên',
            'ten_ky_nang':  'Tên kỹ năng',
            'cap_do': 'Cấp độ',
            # 'ten_mon_hoc': 'Được học từ  môn học'
        }
class SkillPhuUpdateForm(ModelForm):
    class Meta:
        model = SkillPhu
        fields = '__all__'
        labels = {
            'ma_sinh_vien': 'Mã Sinh Viên',
            'ten_ky_nang':  'Tên kỹ năng',
            'cap_do': 'Cấp độ',
            # 'ten_mon_hoc': 'Được học từ  môn học'
        }

class SkillChinhForm(ModelForm):
    class Meta:
        model = SkillChinh
        fields = '__all__'
        labels = {
            'ma_sinh_vien': 'Mã Sinh Viên',
            'ten_ky_nang':  'Tên kỹ năng',
            'cap_do': 'Cấp độ',
            # 'ten_mon_hoc': 'Được học từ  môn học'
        }
class SkillChinhUpdateForm(ModelForm):
    class Meta:
        model = SkillChinh
        fields = '__all__'
        labels = {
            'ma_sinh_vien': 'Mã Sinh Viên',
            'ten_ky_nang':  'Tên kỹ năng',
            'cap_do': 'Cấp độ',
            # 'ten_mon_hoc': 'Được học từ  môn học'
        }

