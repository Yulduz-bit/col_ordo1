from django.shortcuts import render
from store.models.product import History


def history(request):
    histories = History.objects.all()
    context = {
        "histories": histories
    }
    return render(request, 'history.html', context)