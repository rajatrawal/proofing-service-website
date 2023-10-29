from typing import Any, Dict
from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.contrib import messages
from . forms import ServiceRequsetForm

from django.http import HttpResponse


from . models import (
    Service,
    Image,
    Category,
    FAQ,
    Member,
    HeadDetails,
    CompanyDetails,
    AboutUsText,
    ServicesText,
    ContactNowText,
    ContactText

)
# Create your views here.

# home page


def index(request):

    services = Service.objects.all()[:3]
    faqs = FAQ.objects.all()
    members = Member.objects.all()

    context = {
     
        'services': services,
        'faqs': faqs,
        'members': members,
        'head_details': HeadDetails.objects.last(),
        "company_details": CompanyDetails.objects.last(),
        'about_us_text': AboutUsText.objects.last(),
        "services_text": ServicesText.objects.last(),
        "contact_now_text": ContactNowText.objects.last(),
        'contact_text': ContactText.objects.last()
    }

    return render(request, 'home/index.html', context)


def get_service(request, pk):
    service = Service.objects.filter(id=pk)
    if not service.exists():
        messages.error(request, '404 introuvables !')
        return redirect('index')
    form = ServiceRequsetForm
    if request.method == 'POST':
        form = ServiceRequsetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Demande soumise avec succès')
    return render(request, 'home/service_detail.html', {'service': service[0], 'form': form, "company_details": CompanyDetails.objects.last()})


class ServiceList(ListView):
    model = Category
    template_name = 'home/services.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        cat = self.request.GET.get('category', None)
        if cat is not None:
            queryset = queryset.filter(category__icontains=cat)
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['company_details'] = CompanyDetails.objects.last()
        return data


def contact_form(request):
    if request.method == "POST":
        form = ServiceRequsetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
        return HttpResponse('None')
