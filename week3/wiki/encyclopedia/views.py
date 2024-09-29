import random

import markdown2
from django.shortcuts import redirect, render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def get_entry(request, title):
    raw_entry = util.get_entry(title)

    if raw_entry is None:
        return render(request, "encyclopedia/error.html", {"title": title})

    markdown = markdown2.markdown(raw_entry)

    return render(
        request,
        "encyclopedia/entry.html",
        {
            "title": title,
            "content": markdown,
        },
    )


def get_search_result(request):
    search_request = request.GET.get("q", None)
    entries = util.list_entries()
    if search_request in entries:
        return redirect("get_entry", search_request)

    matching_entries = [
        entry for entry in entries if search_request in util.get_entry(entry)
    ]

    return render(
        request,
        "encyclopedia/search_list.html",
        {"search_request": search_request, "entries": matching_entries},
    )


def new_entry(request):
    error_message = None
    if request.method == "POST":
        title = request.POST.get("title")
        if title not in util.list_entries():
            util.save_entry(title, request.POST.get("content"))
            return redirect("get_entry", title)
        error_message = f"A page titled {title} already exists."
    return render(
        request, "encyclopedia/new_entry.html", {"error_message": error_message}
    )


def random_entry(request):
    choice = random.choice(util.list_entries())
    return redirect("get_entry", choice)


def edit_entry(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        return render(
            request,
            "encyclopedia/edit_entry.html",
            {"title": title, "content": content},
        )

    util.save_entry(title, request.POST.get("content"))
    return redirect("get_entry", title)
