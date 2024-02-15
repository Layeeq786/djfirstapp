import datetime
from django.shortcuts import render

# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg = 'Hello Sir Very Very Good '
    h = int(date.strftime('%H'))
    if h<12:
        msg += 'Morning'
    elif h<16:
        msg += 'Afternoon'
    elif h<21:
        msg += 'Evening'
    else:
        msg += 'Night'

    p1 = 'Good to get job very easily'
    p2 = 'Learning is also is very easy'
    p3 = 'You can claim 3 to 4 years of exp.'
    p4 = 'It is very helpful for freshers...'

    batch = 'Current Batch Students Are:'

    my_dict = {'insert_date':date,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'insert_msg':msg,'batch':batch}
    return render(request,'myapp/index.html',my_dict)
