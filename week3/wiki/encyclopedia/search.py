from . import util
from django.shortcuts import redirect, render
from django.http import HttpResponse

class Search:
    def find(request, search_request):
        entries = util.list_entries()
        if search_request in entries:
            return redirect("get_entry", search_request)

        matching_entries = [ entry for entry in entries if search_request in util.get_entry(entry) ]

        return render(request, "encyclopedia/search_list.html", {'search_request': search_request, 'entries': matching_entries})
