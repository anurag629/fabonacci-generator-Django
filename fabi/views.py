from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from fabi.models import Fabonacci


# This function Returns true if
# s is a number else false
def isNumber(s):

    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False

    return True


def index(request):
    return render(request, 'fabi/index.html')


def fibo_post(request):
    if request.method == 'GET':
        value = request.GET['value']

        n1, n2 = 0, 1
        count = 0
        series = []
        if isNumber(value):
            if int(value) == 1:
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
            return redirect(fibo_archive)

        else:
            if(isNumber(value[1:])):
                return render(request, 'fabi/index.html', {'message': "Negative value entered.... Enter a positive number."})
            else:
                return render(request, 'fabi/index.html', {'message': "Text entered.... Enter a positive number."})

    else:
        return redirect(index)


def fibo_archive(request):
    all_series = Fabonacci.objects.all()[::-1]
    print(all_series)
    context = {
        'all_series': all_series
    }
    return render(request, 'fabi/index.html', context)
