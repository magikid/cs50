from django.shortcuts import render
import markdown2

from . import util


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
