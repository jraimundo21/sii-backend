from django.shortcuts import redirect

from django.contrib.auth import logout


# _______Login

def logoutUser(request):
    print('------------OKEYY---------')
    logout(request)
    print('---------------------')
    return redirect('index')
