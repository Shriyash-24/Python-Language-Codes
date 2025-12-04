# HTML files that contain HTML and can also hold dynamic content.

'''
BEFORE -
def home_page(request):
    return HttpResponse("<h1>Home Page Of Our Blogs</h1>")
'''
'''
from django.template.loader import render_to_string
def home_page(request):
    res_data = render_to_string("blogs/index.html")
    return HttpResponse(res_data)
'''

# It won't load because django won't load the HTML file, so you need to make changes in settings.py.
# In templates section,
# DIRS:
#   BASE_DIR / "blogs" / "templates"