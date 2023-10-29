from django.contrib import admin

from . models import (
    Service, ServiceRequest, Category, Advantage, Image, Unit, FAQ, Member, Social, CompanyDetails, HeadDetails, AboutUsText, ServicesText, ContactNowText, ContactText
)


class ImageInline(admin.TabularInline):
    model = Image


class SocialInline(admin.TabularInline):
    model = Social


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


class MemberAdmin(admin.ModelAdmin):
    inlines = [SocialInline, ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register((ServiceRequest, Category, Advantage, Unit, Social, FAQ,
                     CompanyDetails, HeadDetails, AboutUsText, ServicesText, ContactNowText, ContactText))
