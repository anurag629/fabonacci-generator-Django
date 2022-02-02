from django.shortcuts import render, redirect

# Create your views here.
from fabi.models import Fabonacci


def index(request):
    return render(request, 'fabi/index.html')


def fibo_post(request):
    if request.method == 'GET':
        value = request.GET['value']

        n1, n2 = 0, 1
        count = 0
        series = []
        # check if the number of terms is valid
        if int(value) <= 0:
            print("Please enter a positive integer")
        # if there is only one term, return n1
        elif int(value) == 1:
            series.append(str(n1))
        # generate fibonacci sequence
        else:
            while count < int(value):
                series.append(str(n1))
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
                count += 1
        p = ' '.join(series)
        pp = Fabonacci(numstr=value, terms=p)
        pp.save()
        context = {
            'seriess': p
        }

        return render(request, 'fabi/index.html', context)
    else:
        return redirect(index)


def fibo_archive(request):
    all_series = Fabonacci.objects.all()

    context = {
        'all_series': all_series
    }
    return render(request, 'fabi/index.html', context)
