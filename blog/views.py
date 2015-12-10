from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, '/Users/alexanderjohanneser/djangoman/blog/templates/post_list.html', {})