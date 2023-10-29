from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Unit(BaseModel):
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.unit


class Advantage(BaseModel):
    advantage = models.CharField(max_length=200)

    def __str__(self):
        return self.advantage


class Service(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='services')
    price = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    advantages = models.ManyToManyField(Advantage)

    def __str__(self):
        return self.title


class Image(BaseModel):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.alt_text} {self.is_head_image}'


class ServiceRequest(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='service_request', blank=True, null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.service} - {self.phone_number}'


class Member(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Social(BaseModel):
    choices = (
        ('facebook', 'ri-facebook-fill'),
        ('twitter', 'ri-twitter-fill'),
        ('instagram', 'ri-instagram-fill'),
        ('linkedin', 'ri-linkedin-box-fill'),
    )
    name = models.CharField(max_length=100)
    icon_class = models.CharField(choices=choices, max_length=100)
    link = models.CharField(max_length=500)
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='socials')

    def __str__(self):
        return self.name


class FAQ(BaseModel):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class CompanyDetails(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=300)
    email = models.EmailField()
    twitter_link = models.CharField(max_length=200,default="#")
    facebook_link = models.CharField(max_length=200,default="#")
    instagram_link = models.CharField(max_length=200,default="#")
    linkedin_link = models.CharField(max_length=200,default="#")
    map_link = models.CharField(max_length=500,default="#")
    
    def __str__(self):
        return "Company Details"


class HeadDetails(models.Model):
    text = models.CharField(max_length=100)
    video_link = models.CharField(max_length=500,default="#")
    
    def __str_(self):
        return "Heading Details"


class AboutUsText(models.Model):
    text = models.TextField()
    def __str_(self):
        return "Aboutus section text"

class ServicesText(models.Model):
    text = models.TextField()
    def __str_(self):
        return "Services section text"


class ContactNowText(models.Model):
    text = models.TextField()
    def __str_(self):
        return "Contactnow  section text"


class ContactText(models.Model):
    text = models.TextField()
    
    def __str_(self):
        return "contact section text"
