from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    time = datetime.datetime.now()
    #names_list = ['Sunny','Katrina','Kareena','Deepika','Mallika','Alia']
    names_list = ['Pawan Kalyan','Prabhas','Sampu','Snow Anna','Jr. Ntr','Allu Arjun']
    msg_list = [
    'The golden days a head',
    'Better to sleep more time in class',
    'Tomorrow is the perfect day to propose ur GF',
    'Very soon you will get job',
    'Very soon U will get Marriage....'
    ]
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Good Morning'
    elif h<16:
        s = 'Good Afternoon'
    elif h<21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)
