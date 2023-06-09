from django.http import JsonResponse
from django.shortcuts import render
from .models import Settings, NewsLatter
from property.models import Property,Place,Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_email_tasks
from blog.models import Post
from property.models import PropertyBook

# Create your views here.


def Home(request):
    place = Place.objects.all().annotate(property_count = Count('property_place'))
    categories = Category.objects.all()
    resturant_list = Property.objects.filter(Category__name = 'Resturant')[:5]
    hotel_list = Property.objects.filter(Category__name = 'Hotels')[:4]
    places_list = Property.objects.filter(Category__name = 'Places')[:4]
    recent_posts = Post.objects.all()


    user_count = User.objects.all().count()
    hotel_count = Property.objects.filter(Category__name = 'Hotels').count()
    places_count = Property.objects.filter(Category__name = 'Places').count()
    resturant_count = Property.objects.filter(Category__name = 'Resturant').count()

    return render(request, 'settings/home.html',{
        'places':place,
        'category':categories,
        'resturant_list': resturant_list,
        'hotel_list':hotel_list,
        'places_list':places_list,
        'recent_posts':recent_posts,
        'user_count':user_count,
        'hotel_count':hotel_count,
        'places_count':places_count,
        'resturant_count':resturant_count,


                    })



def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    property_list = Property.objects.filter(
        Q(name__icontains = name) &
        Q(place__name__icontains=place)

    )
    return render(request, 'settings/home_search.html', {'property_list':property_list})


def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(Category=category)
    return render(request, 'settings/home_search.html', {'property_list':property_list})



def contact_us(request):
    site_info = Settings.objects.last()

    if request.method == 'POST':
        subject = request.POST['subject']
        site_name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_email_tasks.delay(subject,site_name,email,message)
        # send_mail(
        #     subject,
        #     f'message from {name} \n email : {email} \n Message : {message}',
        #     email,
        #     [settings.EMAIL_HOST_USER],
        #     fail_silently=False,
        # )

    return render(request,'settings/contact.html',{'site_info': site_info})


def dashboard(request):
    user_count = User.objects.all().count()
    hotel_count = Property.objects.filter(Category__name = 'Hotels').count()
    places_count = Property.objects.filter(Category__name = 'Places').count()
    resturant_count = Property.objects.filter(Category__name = 'Resturant').count()
    booking_count = PropertyBook.objects.all().count()
    posts_count = Post.objects.all().count()
    return render(request, 'settings/dashboard.html',{
 
        'user_count':user_count,
        'hotel_count':hotel_count,
        'places_count':places_count,
        'resturant_count':resturant_count,
        'booking_count':booking_count,
        'posts_count':posts_count


                    })





def news_letter(request):
    email = request.POST.get("emailInput")
    news_letter = NewsLatter.objects.create(email=email)

    return JsonResponse({'done':'done'})
