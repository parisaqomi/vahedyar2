from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

COURSE_TYPE_CHOISES=[(1,u'درس اصلی') ,
     (2,u'درس تخصصی') ,
      (3,u'درس عمومی'),
      (4,u'درس اختیاری')]

DEGREE_TYPE_CHOISES=[(1,u'کاردانی') ,
     (2,u'کارشناسی') ,
      (3,u'کارشناسی ارشد'),
      (4,u'دکتری')]

class University(models.Model):
    name = models.CharField(verbose_name="نام دانشگاه", max_length = 40)
    has_associates_degree = models.NullBooleanField(verbose_name="مقطع کاردانی")
    has_bachelors_degree = models.NullBooleanField(verbose_name="مقطع کارشناسی")
    has_masters_degree = models.NullBooleanField(verbose_name="مقطع کارشناسی ارشد")
    has_doctorate_degree = models.NullBooleanField(verbose_name="مقطع دکتری")
    class Meta:
        verbose_name=u' دانشگاه'
        verbose_name_plural=u'دانشگاه‌ها '  
    def __str__(self):
        return f"{self.name}" 

class Faculty(models.Model):
    name = models.CharField(verbose_name="نام دانشکده" , max_length = 40)
    universiy = models.ForeignKey(
        'University', 
        on_delete=models.CASCADE,
        verbose_name="نام دانشگاه"
    )    
    class Meta:
        verbose_name=u'دانشکده '
        verbose_name_plural=u'دانشکده‌ها ' 
    def __str__(self):
        return f"{self.name} {self.universiy.name}" 

 
class Chart(models.Model):
    title = models.CharField(verbose_name="عنوان چارت" ,max_length = 40)
    is_active = models.BooleanField(verbose_name="فعال بودن")
    degree = models.CharField(verbose_name="مقطع" , max_length = 20)
    acceptance_date = models.DateField(verbose_name="تاریخ تصویب")
    course = models.ManyToManyField("Course" , null=True , blank=True)
    faculty = models.ForeignKey(
        'Faculty', 
        on_delete=models.CASCADE,
        verbose_name="دانشکده"
    ) 
    class Meta:
        verbose_name=u'چارت تحصیلی '
        verbose_name_plural=u'چارت‌های تحصیلی'  
    def __str__(self):
        return f"چارت {self.title} دانشکده {self.faculty}" 

class Study(models.Model):
    degree = models.IntegerField(choices=DEGREE_TYPE_CHOISES, verbose_name="مقطع تحصیلی")
    entrance_year = models.DateField(verbose_name="سال ورود")
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="دانشجو"
    )
    chart = models.ForeignKey(
        'Chart', 
        on_delete=models.CASCADE,
        verbose_name="چارت"
    )
    class Meta:
        verbose_name=u'مقطع تحصیلی '
        verbose_name_plural=u'مقاطع تحصیلی '  
    def __str__(self):
        return f"{self.get_degree_display()} {self.chart.title}" 

class Scores(models.Model):
    score = models.FloatField(verbose_name="نمره")
    study = models.ForeignKey(
        'Study', 
        on_delete=models.CASCADE,
        verbose_name="تحصیل"
    )
    course = models.ForeignKey(
        'Course', 
        on_delete=models.CASCADE,
        verbose_name="درس"
    )
    class Meta:
        verbose_name=u'نمره '
        verbose_name_plural=u'نمره‌ها '  
    def __str__(self):
        return f"{self.name}" 

class Course(models.Model):
    title = models.CharField(verbose_name="عنوان",max_length = 20)
    course_type = models.IntegerField(choices=COURSE_TYPE_CHOISES, verbose_name="نوع درس")
    vahed_nazari = models.IntegerField(verbose_name="تعداد واحد نظری")
    vahed_amali = models.IntegerField(verbose_name="تعداد واحد عملی")
    corequisite_courses = models.ManyToManyField( #همنیاز
        'self', 
        verbose_name="هم‌نیاز",
        related_name="corequisites",
        blank=True
    )
    prerequisite_courses = models.ManyToManyField(
        'self', 
        verbose_name="پیش‌نیاز",
        related_name="prerequisites",
        blank=True
    )
    class Meta:
        verbose_name=u'درس '
        verbose_name_plural=u'درس‌ها '  
    def __str__(self):
        return f"{self.title}" 