from . import util
from django.shortcuts import redirect
from django.http import HttpResponse

class Search:
    def find(search_request):
        entries = util.list_entries()
        if search_request in entries:
            return redirect("get_entry", search_request)
        return HttpResponse(content='not found', status=404)
