from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Tweet
from .forms import PictureForm
from django import forms

from cloudinary.forms import cl_init_js_callbacks

# Create views here.


def home(request):
    # fetch all objects
    tweets = Tweet.objects.order_by("created_at").reverse().all()
    form = PictureForm()

    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"tweets": tweets, "backend_form": form}
    return render(request, "home.html", context=context)


def upload(request):
    # add form dictionary to context
    context = dict(backend_form=PictureForm())

    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "upload.html", context)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Tweet, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


def edit(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Tweet, id=id)
    # obj = Tweet.objects.get(id=id)

    # pass the object as instance in form
    form = PictureForm(instance=obj)

    # save the data from the form and redirect to home
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=obj)
        # print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("home")

    # add form dictionary to context
    context = {"obj": obj, "form": form}
    return render(request, "edit.html", context)


def like_function(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Tweet, id=id)

    # Increase like count by 1
    obj.like_count += 1

    # save
    obj.save()

    return HttpResponseRedirect("/")


def dislike_function(request, id):
    obj = get_object_or_404(Tweet, id=id)

    # Increase like count by 1
    obj.like_count -= 1

    # save
    obj.save()

    return HttpResponseRedirect("/")


def hiden_fuctionality(request, id):
    obj = get_object_or_404(Tweet, id=id)

    # Hide the tweet
    obj.hidden = True

    # Save
    obj.save()

    return HttpResponseRedirect("/")
