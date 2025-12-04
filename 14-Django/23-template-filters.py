'''
Just for eg, we have removed title() from here and want to work it with template.
def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list).title()
'''

# We should template filters instead.. {{ value|title}}  <-- Template filter.
