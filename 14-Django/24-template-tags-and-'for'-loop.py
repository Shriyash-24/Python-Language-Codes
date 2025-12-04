# Tags - DTL built-in feature.
# 'for' tag - Used for loops.
# The logic should be in a template.
''' BEFORE -->
def blogposts(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    for b in blog_list:
        blog_path = reverse("blog-post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)
'''

'''
AFTER -->
def blogposts(request):
    list_items = ""
    blog_list = list(blog_names.keys())
    return render(request, "blogs/allposts.html", {"blogs":blog_list})
HTML File Changes -
<body>
    <ul>
        {% for blog in blogs %}
            <li><a href="">{{ blog|capfirst}}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
'''