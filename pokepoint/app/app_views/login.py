from django.shortcuts import redirect

from django.contrib.auth import logout


# _______Login

def logoutUser(request):
    logout(request)
    return redirect('login')
