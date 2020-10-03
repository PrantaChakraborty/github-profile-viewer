from django.shortcuts import render
import requests
import json
# Create your views here.


def profile(request):
    outputList = []
    if request.method == 'POST':
        username = request.POST.get('user')
        jsonList = []
        req = requests.get('https://api.github.com/users/' + username)
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        outputList.append(userData)
    return render(request, 'user/home.html', {'outputList': outputList})
