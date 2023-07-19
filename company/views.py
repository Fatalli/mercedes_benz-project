from django.shortcuts import render, get_object_or_404
from .models import Company

def about_company(request):
    companys = Company.objects.order_by('-date')
    return render(request, 'company/about_company.html', {'companys':companys})


def detail_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'company/detail_company.html',{'company':company})

