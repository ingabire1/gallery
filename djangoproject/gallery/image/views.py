from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Gallery Correction')

def image_of_day(request):
    date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    # return HttpResponse(html)
    return render(request, 'all-images/today-image.html', {"date": date,})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

def past_days_images(request,past_date):
    # Converts data from the string Url
    # View Function to present news from past days
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)

    #     news = Article.days_news(date)
    # return render(request, 'all-news/past-news.html',{"date": date,"news":news})

    return render(request, 'all-images/past-images.html', {"date": date})

def welcome(request):
    return render(request, 'welcome.html')

def news_today(request):
    date = dt.date.today()
    images = Image.todays_image()
    return render(request, 'all-images/today-images.html', {"date": date,"images":images})

def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html", {"image":image})