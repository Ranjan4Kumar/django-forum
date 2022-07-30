from http.client import HTTPResponse
from traceback import format_exception_only
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import App
from .forms import PostForm

def index(request):

 # if the method is post
    if request.method == 'POST':
        form = PostForm(request.POST)


   
        # if the form is valid
        if form.is_valid():
            # yes, save 
            form.save()
            #it and redirect it to home
            return HttpResponseRedirect('/')


            
        else:
             # No, It will project an error
             return HttpResponseRedirect(form.errors.as_json())





     #get all the post limit= 20
    app_1 = App.objects.all()[:20]

    return render(request, 'app.html',
    {'app_1':app_1})
   


def delete(request, post_id):
    # Find post
    post = App.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    output = 'POST ID IS' +str(post_id)
    return HttpResponse(output)


def edit(request, post_id):
    app_1 = App.objects.get(id = post_id)


    if request.method == 'POST':

        form = PostForm(request.POST,instance=post_id)


        if form .is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("not valid")
   




