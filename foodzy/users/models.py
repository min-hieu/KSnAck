from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager


class MyStudentManager(BaseUserManager):
    def create_user(self, username, student_id, password=None):
        if not username:
            raise ValueError("Username is blank or invalid")
        if not student_id:
            raise ValueError("enter XX-YYY for student id")

        student = self.model(
            username = username,
            student_id = student_id,
        )

        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, username, student_id, password):
        student = self.create_user(
            username = username,
            student_id = student_id,
            password=password,
        )

        student.is_admin = True
        student.is_staff = True
        student.is_superuser = True
        student.save(using=self._db)
        return student


class Student(AbstractBaseUser):
    username                = models.CharField(max_length=100, unique=True)
    student_id              = models.CharField(max_length=6, unique=True)
    rank                    = models.CharField(max_length=100, default='Layman')
    happiness               = models.IntegerField(default=0)
    medals                  = models.TextField(default='')
    bio                     = models.TextField(default='')

    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['username',]

    objects = MyStudentManager()

    def __str__(self):
        return self.student_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



    

