from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'msg' : '코딩좋아',
    }
    return render(request, 'sample/index.html', context)