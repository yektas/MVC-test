from django.shortcuts import render, render_to_response, redirect

from utility.decorators import language_assigned


def language_detector(request):
    if request.method == 'GET':
        try:
            response = render_to_response("{}/index.html".format(request.GET.get('language', ' ')))
            response.set_cookie('language', '{}'.format(request.GET.get('language', ' ')))
            return response
        except:
            response = render_to_response("tr/index.html")
            try:
                response.set_cookie('language', '{}'.format(request.session['language']))
            except:
                response.set_cookie('language', 'tr')
            return response
    else:
        return redirect("home:index")


@language_assigned
def index(request):
    return render(request, "{}/index.html".format(request.COOKIES['language']))