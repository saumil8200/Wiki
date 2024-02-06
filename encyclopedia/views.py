from django.shortcuts import render
import random

from django.shortcuts import redirect
from django import forms
from django.http import HttpResponse

from . import util


class NewWikiForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, name):
    return render(request, "encyclopedia/wiki.html", {
        "entry": util.get_entry(name)
    })

def search(request):
    query = request.GET.get('q')
    if query:
        entries = util.list_entries()
        found_entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {"found_entries": found_entries, "query": query})
    else:
        return render(request, "encyclopedia/search.html")

def new(request):
    entries = util.list_entries()

    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            lowercase_entries = [entry.lower() for entry in entries]
            lowercase_title = title.lower()

            if lowercase_title not in lowercase_entries:
                util.save_entry(title, content)
                return redirect("wiki", name=title)
            else:
                return HttpResponse("Wiki already exists.")
    else:
        form = NewWikiForm()

    return render(request, "encyclopedia/new.html", {
        "form": form,
        "entries": entries
    })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect("wiki", name=random_entry)

