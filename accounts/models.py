from django.contrib.auth.models import User
from django.db import models
from  django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.


TYPE_PERSON = (
    ("M", "MALE"),
    ("F", "FEMALE")
)
class Profile(models.Model):
    DOCTOR_IN ={
        ("مخ واعصاب","مخ واعصاب"),
        ("جراحة","جراحة"),
        ("ولادة","ولادة"),
        ("قلب","قلب"),
        ("عيون","عيون"),
        ("عظام","عظام"),
        ("جلدية","جلدية"),
        ("اشعة","اشعة"),
    }
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الاسم : "), max_length=50)
    surname = models.CharField(_("اللقب  "), max_length=50)
    sub_title = models.CharField(_("نبذة : "), max_length=50)
    address = models.CharField(_("العنوان:"), max_length=50)
    address_detail = models.CharField(_("العنوان بالتفصيل"), max_length=50)
    phone = models.CharField(_("ر:قم الهاتف"), max_length=50)
    working_hours = models.CharField(_("ساعات العمل:"), max_length=50)
    waitting_time = models.IntegerField(_("وقت الانتظار : "), blank=True, null=True)
    who_i = models.TextField(_("من أنا : "),max_length=250, blank=True, null=True)
    price = models.IntegerField(_("سعر الكشف : "), blank=True, null=True)
    join_now = models.DateTimeField(_("وقت الانضمام :"), auto_now_add=True)
    type_person = models.CharField(_("النوع"), choices= TYPE_PERSON , max_length=50)
    image = models.ImageField(_("الصورة الشخصية"), upload_to='profile', blank=True, null=True)
    specialist_doctor = models.CharField(_(" التخصص:"), max_length=50, blank=True, null=True)
    doctor = models.CharField(_(" دكتور ؟:"), choices= DOCTOR_IN , max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(_("slug"), blank=True, null=True)
  
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profile")


    def __str__(self):
        return '%s' %(self.user.username)

        
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender = User)

    
