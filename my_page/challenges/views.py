import challenges
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'jan': 'January ok',
    'feb': 'February ok',
    'mar': 'March ok',
    'apr': 'April ok',
    'may': 'May ok',
    'jun': 'June ok',
    'jul': 'July ok',
    'aug': 'August ok',
    'sep': None,
    'oct': None,
    'nov': None,
    'dec': None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })


def numb_challenges(request, month):
    month_list = list(monthly_challenges.keys())
    if month > len(month_list):
        return HttpResponseNotFound(str(month)+" not found")
    redirect_month = month_list[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/jan
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()
        return render(request, "404.html")
        #return HttpResponseNotFound(f"<h1>{month} not found</h1>")
