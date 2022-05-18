from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from statistics import mean, median, stdev

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

def find_mean(request):
    mean = None
    
    if request.method == "POST":
        num = request.POST.get("numbers")
        numbers = list(map(int, num.split(",")))
        mean = round((sum(numbers)/len(numbers)), 2)
        # return redirect("home")
        
    context = {
        "section":"mean",
        "mean" : mean
    }
    
    return render(request, "mean.html", context)




def median_value(request):
    med = None
    
    if request.method == "POST":
        num = request.POST.get("numbers")
        numbers = list(map(int, num.split(",")))
        med = median(numbers)
        
    context = {
        "section":"median",
        "median" : med
    }
    
    return render(request, "median.html", context)
    

def standard_deviation(request):
    std_dev = None
    
    if request.method == "POST":
        num = request.POST.get("numbers")
        numbers = list(map(int, num.split(",")))
        std_dev = round(stdev(numbers), 3)
        
    context = {
        "section":"std_dev",
        "std_dev" : std_dev
    }
    
    return render(request, "std.html", context)


def skewness(request):
    skw = None
    
    if request.method == "POST":
        num = request.POST.get("numbers")
        numbers = list(map(int, num.split(",")))
        mean_ = mean(numbers)
        standard_dev = stdev(numbers)
        n = len(numbers)
        numerator = sum([(x-mean_)**3 for x in numbers])
        denominator = (n-1) * (standard_dev**3)
        skw =  numerator/denominator

    context = {
        "section":"skewness",
        "skewness" : skw
    }
    
    return render(request, "skewness.html", context)