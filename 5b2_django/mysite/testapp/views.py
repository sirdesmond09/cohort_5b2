from django.shortcuts import redirect, render
from django.http.response import HttpResponse


def test_view(request):
    return HttpResponse("""<h1>This is a response</h1>
<p> I am just testing this view out<p>""")
    
def about_us(request):
    data = {
        "section":"about"
    }
    return render(request, "about.html", data)

def html_home_page(request):
    context = {
        "section":"home"
    }
    return render(request, "home.html", context)

def contact_us(request):
    mean = None
    
    if request.method == "POST":
        num = request.POST.get("numbers")
        numbers = list(map(int, num.split(",")))
        mean = round((sum(numbers)/len(numbers)), 2)
        # return redirect("home")
        
    context = {
        "section":"contact",
        "mean" : mean
    }
    
    return render(request, "contact.html", context)