from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Job(models.Model):
    ma_viec_lam = models.CharField(max_length=255,null=True,blank=True)
    ten_viec_lam = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.ten_viec_lam
    def get_absolute_url(self):
        return reverse("job-detail", kwargs={"pk": self.pk})

class SkillPhu(models.Model):
    ten_viec_lam = models.ForeignKey(Job, null=True, on_delete=models.CASCADE)
    ten_ky_nang_phu = models.CharField(
        max_length=30,
        choices=[
            ('Giao tiếp & Thuyết trình', 'Giao tiếp & Thuyết trình'),
            ('Hợp tác & làm việc nhóm', 'Hợp tác & làm việc nhóm'),
            ('Phân tích & xử lý vấn đề', 'Phân tích & xử lý vấn đề'),
            ('Quản lý bản thân', 'Quản lý bản thân'),
            ('Tạo lập mối quan hệ hiệu quả', 'Tạo lập mối quan hệ hiệu quả'),
            ('Tin học ứng dụng', 'Tin học ứng dụng'),
            ('Lãnh đạo & quản lý', 'Lãnh đạo & quản lý'),
            ('Học hỏi & thích ứng', 'Học hỏi & thích ứng'),
            ('Học thuật & toán học', 'Học thuật & toán học'),
            ('Tinh thần & thái độ làm việc', 'Tinh thần & thái độ làm việc'),
            ('Phân tích chiến lược', 'Phân tích chiến lược'),
            ('Hoạch định tài chính', 'Hoạch định tài chính'),
            ('Phân tích dữ liệu', 'Phân tích dữ liệu'),
            ('Lập kế hoạch và điều phối', 'Lập kế hoạch và điều phối'),
            ('Khai thác các phần mềm TMĐT', 'Khai thác các phần mềm TMĐT'),
            ('Bán hàng và trưng bày cửa hàng', 'Bán hàng và trưng bày cửa hàng'),
            ('Tư Duy Nhạy Bén', 'Tư Duy Nhạy Bén'),
            ('Đào Tạo Nhân Viên', 'Đào Tạo Nhân Viên'),
            ('Tư Duy Logic', 'Tư Duy Logic'),
            ('Lập trình ứng dụng', 'Lập trình ứng dụng'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Kỹ năng tạo động lực', 'Kỹ năng tạo động lực'),
            ('Hiểu Biết Về Công Nghệ', 'Hiểu Biết Về Công Nghệ'),
            ('Thương Mại Điện Tử', 'Thương Mại Điện Tử'),
            ('Phát Triển Thương Hiệu', 'Phát Triển Thương Hiệu'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Marketing', 'Marketing'),
            ('Adobe Photoshop', 'Adobe Photoshop'),
            ('Thuyết phục và đàm phán', 'Thuyết phục và đàm phán'),
            ('Ecommerce Vendor', 'Ecommerce Vendor'),
            ('Ecommerce Platfrom', 'Ecommerce Platfrom'),
            ('Digital Marketing', 'Digital Marketing'),
            ('Tiếng Anh', 'Tiếng Anh'),
            ('Microsoft Office', 'Microsoft Office'),
            ('Marketing Online', 'Marketing Online'),
            ('Phát Triển Thị Trường', 'Phát Triển Thị Trường'),
            ('Quảng Cáo', 'Quảng Cáo'),
            ('Quản lý nhóm', 'Quản lý nhóm'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
        ],
        default='',)
    cap_do = models.CharField(
        max_length=1,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ],
            default='',)

    def __str__(self):
        return self.ten_ky_nang_phu
    def get_absolute_url(self):
        return reverse("skill-detail", kwargs={"pk": self.pk})

class SkillChinh(models.Model):
    ten_viec_lam = models.ForeignKey(Job, null=True, on_delete=models.CASCADE)
    ten_ky_nang_chinh = models.CharField(
        max_length=30,
        choices=[
            ('Giao tiếp & Thuyết trình', 'Giao tiếp & Thuyết trình'),
            ('Hợp tác & làm việc nhóm', 'Hợp tác & làm việc nhóm'),
            ('Phân tích & xử lý vấn đề', 'Phân tích & xử lý vấn đề'),
            ('Quản lý bản thân', 'Quản lý bản thân'),
            ('Tạo lập mối quan hệ hiệu quả', 'Tạo lập mối quan hệ hiệu quả'),
            ('Tin học ứng dụng', 'Tin học ứng dụng'),
            ('Lãnh đạo & quản lý', 'Lãnh đạo & quản lý'),
            ('Học hỏi & thích ứng', 'Học hỏi & thích ứng'),
            ('Học thuật & toán học', 'Học thuật & toán học'),
            ('Tinh thần & thái độ làm việc', 'Tinh thần & thái độ làm việc'),
            ('Phân tích chiến lược', 'Phân tích chiến lược'),
            ('Hoạch định tài chính', 'Hoạch định tài chính'),
            ('Phân tích dữ liệu', 'Phân tích dữ liệu'),
            ('Lập kế hoạch và điều phối', 'Lập kế hoạch và điều phối'),
            ('Khai thác các phần mềm TMĐT', 'Khai thác các phần mềm TMĐT'),
            ('Bán hàng và trưng bày cửa hàng', 'Bán hàng và trưng bày cửa hàng'),
            ('Tư Duy Nhạy Bén', 'Tư Duy Nhạy Bén'),
            ('Đào Tạo Nhân Viên', 'Đào Tạo Nhân Viên'),
            ('Tư Duy Logic', 'Tư Duy Logic'),
            ('Lập trình ứng dụng', 'Lập trình ứng dụng'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Kỹ năng tạo động lực', 'Kỹ năng tạo động lực'),
            ('Hiểu Biết Về Công Nghệ', 'Hiểu Biết Về Công Nghệ'),
            ('Thương Mại Điện Tử', 'Thương Mại Điện Tử'),
            ('Phát Triển Thương Hiệu', 'Phát Triển Thương Hiệu'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Marketing', 'Marketing'),
            ('Adobe Photoshop', 'Adobe Photoshop'),
            ('Thuyết phục và đàm phán', 'Thuyết phục và đàm phán'),
            ('Ecommerce Vendor', 'Ecommerce Vendor'),
            ('Ecommerce Platfrom', 'Ecommerce Platfrom'),
            ('Digital Marketing', 'Digital Marketing'),
            ('Tiếng Anh', 'Tiếng Anh'),
            ('Microsoft Office', 'Microsoft Office'),
            ('Marketing Online', 'Marketing Online'),
            ('Phát Triển Thị Trường', 'Phát Triển Thị Trường'),
            ('Quảng Cáo', 'Quảng Cáo'),
            ('Quản lý nhóm', 'Quản lý nhóm'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
        ],
        default='',)
    cap_do = models.CharField(
        max_length=1,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ],
            default='',)

    def __str__(self):
        return self.ten_ky_nang_chinh
    def get_absolute_url(self):
        return reverse("skill-detail", kwargs={"pk": self.pk})
class SkillJob(models.Model):

    ten_ky_nang_job = models.CharField(
        max_length=30,
        choices=[
            ('Giao tiếp & Thuyết trình', 'Giao tiếp & Thuyết trình'),
            ('Hợp tác & làm việc nhóm', 'Hợp tác & làm việc nhóm'),
            ('Phân tích & xử lý vấn đề', 'Phân tích & xử lý vấn đề'),
            ('Quản lý bản thân', 'Quản lý bản thân'),
            ('Tạo lập mối quan hệ hiệu quả', 'Tạo lập mối quan hệ hiệu quả'),
            ('Tin học ứng dụng', 'Tin học ứng dụng'),
            ('Lãnh đạo & quản lý', 'Lãnh đạo & quản lý'),
            ('Học hỏi & thích ứng', 'Học hỏi & thích ứng'),
            ('Học thuật & toán học', 'Học thuật & toán học'),
            ('Tinh thần & thái độ làm việc', 'Tinh thần & thái độ làm việc'),
            ('Phân tích chiến lược', 'Phân tích chiến lược'),
            ('Hoạch định tài chính', 'Hoạch định tài chính'),
            ('Phân tích dữ liệu', 'Phân tích dữ liệu'),
            ('Lập kế hoạch và điều phối', 'Lập kế hoạch và điều phối'),
            ('Khai thác các phần mềm TMĐT', 'Khai thác các phần mềm TMĐT'),
            ('Bán hàng và trưng bày cửa hàng', 'Bán hàng và trưng bày cửa hàng'),
            ('Tư Duy Nhạy Bén', 'Tư Duy Nhạy Bén'),
            ('Đào Tạo Nhân Viên', 'Đào Tạo Nhân Viên'),
            ('Tư Duy Logic', 'Tư Duy Logic'),
            ('Lập trình ứng dụng', 'Lập trình ứng dụng'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Kỹ năng tạo động lực', 'Kỹ năng tạo động lực'),
            ('Hiểu Biết Về Công Nghệ', 'Hiểu Biết Về Công Nghệ'),
            ('Thương Mại Điện Tử', 'Thương Mại Điện Tử'),
            ('Phát Triển Thương Hiệu', 'Phát Triển Thương Hiệu'),
            ('Quản Lý Thương Hiệu', 'Quản Lý Thương Hiệu'),
            ('Marketing', 'Marketing'),
            ('Adobe Photoshop', 'Adobe Photoshop'),
            ('Thuyết phục và đàm phán', 'Thuyết phục và đàm phán'),
            ('Ecommerce Vendor', 'Ecommerce Vendor'),
            ('Ecommerce Platfrom', 'Ecommerce Platfrom'),
            ('Digital Marketing', 'Digital Marketing'),
            ('Tiếng Anh', 'Tiếng Anh'),
            ('Microsoft Office', 'Microsoft Office'),
            ('Marketing Online', 'Marketing Online'),
            ('Phát Triển Thị Trường', 'Phát Triển Thị Trường'),
            ('Quảng Cáo', 'Quảng Cáo'),
            ('Quản lý nhóm', 'Quản lý nhóm'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
            # ('Tiếng Anh', 'Tiếng Anh'),
        ],
        default='',)
    # cap_do = models.CharField(
    #     max_length=1,
    #     choices=[
    #         ('1', '1'),
    #         ('2', '2'),
    #         ('3', '3'),
    #         ('4', '4'),
    #         ('5', '5'),
    #         ],
    #         default='',)

    def __str__(self):
        return self.ten_ky_nang_job
    def get_absolute_url(self):
        return reverse("skilljob-detail", kwargs={"pk": self.pk})

class JobSkill(models.Model):
    ma_viec_lam_skill = models.CharField(max_length=255,null=True,blank=True)
    ten_viec_lam_skill = models.CharField(max_length=255,null=True,blank=True)
    ten_ky_nang = models.ForeignKey(SkillJob, null=True, on_delete=models.CASCADE)
    # cap_do = models.CharField(
    #         max_length=1,
    #         choices=[
    #             ('1', '1'),
    #             ('2', '2'),
    #             ('3', '3'),
    #             ('4', '4'),
    #             ('5', '5'),
    #             ],
    #             default='',)
    def __str__(self):
        return self.ten_viec_lam_skill
    def get_absolute_url(self):
        return reverse("job-detail", kwargs={"pk": self.pk})
