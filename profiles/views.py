from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    photos = user.photo_set.order_by('-created_at', '-pk')
    return render(request, 'profiles/profile.html', {'user':user, 'photos':photos,})
