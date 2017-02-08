from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p><img src="{url}"/></p>'.format(url=photo.image.url),
    )

    return HttpResponse('\n'.join(messages))

@login_required
def create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect(obj)
    else:
        form = PhotoForm()
    return render(request, 'edit.html', {'form':form})