# Why have we created blogs folder.. and directly put index.html in templates.
# But it's not good practice.
# Django won't be able to differentiate between apps.
# We can also improve the rendering part.
'''
def home_page(request):
    res_data = render_to_string("blogs/index.html")
    return HttpResponse(res_data)
'''

'''
def home_page(request):
    return render(request, "blogs/index.html")
'''