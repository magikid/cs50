from django.shortcuts import render, redirect
import markdown2

from . import util
from .search import Search

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    raw_entry = util.get_entry(title)

    if raw_entry is None:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

    markdown = markdown2.markdown(raw_entry)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown,
    })

def get_search_result(request):
    search_request = request.GET.get('q', None)
    return Search.find(request, search_request)

def new_entry(request):
    error_message = None
    if request.method == "POST":
        title = request.POST.get('title')
        if title not in util.list_entries():
            util.save_entry(title, request.POST.get('content'))
            return redirect('get_entry', title)
        error_message = f"A page titled {title} already exists."
    return render(request, "encyclopedia/new_entry.html", {"error_message": error_message})
