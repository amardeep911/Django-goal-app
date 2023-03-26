from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Eat no coke",
    "march": None,
    "april": "Eat no beer",
    "may": "Eat no biscuit",
    "june": "Eat no pancake",
    "july": "Eat no pepsi",
    "september": "Eat no brain",
    "august": "Eat no oil",
    "october": "Eat no pastry",
    "november": "Eat no icecream",
    "december": "Eat no me",
}
def index(request):
    print("hlw")
    listItems = ""
    months = list(monthly_challenges.keys()) 

    return render(request, 'challenges/index.html', {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys());
    if month > len(months):
        return HttpResponseNotFound("Not found")
    redirect_month = months[month-1]
    redirect_path = reverse(monthly_challenge, args=[redirect_month]);  # Used for making url paths much flexible
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    