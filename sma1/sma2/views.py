from django.shortcuts import render
from .models import Sensor, SystemChanges
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from .func_for_datchik import vvod_info_datchiki

# Create your views here.

class IndexView(View):
    def get(self, request):
        vvod_info_datchiki()
        return render(request, 'index.html')  # путь из templates


# class CreateFormView(View):
#     def get(self, request):
#         author_form = AuthorForm()
#         return render(request, 'create_form.html', context={"author_form": author_form, })
#
#     def post(self, request):
#         author_form = AuthorForm(request.POST)
#         if not author_form.is_valid():
#             return HttpResponseBadRequest("Bad Request")
#         data = author_form.cleaned_data
#         author = Author(**data)
#         author.save()
#         return HttpResponse(author.name)
#
#
# class CreateView(View):
#     def get(self, request):
#         return render(request, 'create.html')
#
#     def post(self, request):
#         data = request.POST
#         try:
#             author = Author(
#                 name=data["name"],
#                 sur_name=data["sur_name"],
#                 year=data["year"]
#             )
#             author.save()
#         except Exception:
#             return HttpResponseBadRequest("Bad Request")
#         return HttpResponse(author.name)
#
#
# class DelAuthorsView(View):
#     def get(self, request):
#         return render(request, 'delauthors.html')
#
#     def post(self, request):
#         try:
#             author = Author.objects.get(id=request.POST["id"])
#             print(author)
#             author.delete()
#         except Exception:
#             return HttpResponseBadRequest("Bad Request")
#         return HttpResponse(author.name)
#
# class ListAuthorsView(View):
#     def get(self, request):
#         authors = Author.objects.all()
#         return render(request, 'authors.html', context={"authors": authors})
