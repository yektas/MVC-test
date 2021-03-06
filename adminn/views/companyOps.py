import datetime
import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render

from adminn.models.companyModels import CompanyEventClass
from utility.decorators import is_admin

logging.basicConfig(filename='debug.log', level=logging.DEBUG)


@is_admin
def create_company(request):
    """Utkucan """
    """Create company function"""
    """Object Create"""
    instance = CompanyEventClass(request)
    if request.method == "POST":
        """Get company name from form"""
        name = request.POST.get('cname', ' ')
        """If create company"""
        if instance.create_company(name):
            logging.info('company created / {} '.format(datetime.datetime.now()))
            return redirect("adminn:index")

    return render(request, "company.html")


@is_admin
def list_company(request):
    instance = CompanyEventClass(request)
    company = instance.list_company()
    """Use the paginator from django"""
    page = request.GET.get('page', 1)
    """All companies split into 5 pieces"""
    paginator = Paginator(company, 5)
    try:
        companys = paginator.page(page)
        """If page not an integer return page 1"""
    except PageNotAnInteger:
        companys = paginator.page(1)
    except EmptyPage:
        companys = paginator.page(paginator.num_pages)
    return render(request, "companylist.html", {"companys": companys})


@is_admin
def delete_company(request):
    instance = CompanyEventClass(request)
    if request.method == "POST":
        name = request.POST.getlist('name', '')
        for i in range(len(name)):
            instance.delete_company(name[i])

        logging.info('company deleted / {}'.format(datetime.datetime.now()))
        return redirect("adminn:list_company")
    else:
        return redirect("adminn:list_company")
