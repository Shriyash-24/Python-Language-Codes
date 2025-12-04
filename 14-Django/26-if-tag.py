# If blog is  in process like "tkinter": None
# We need to use 'if' tag.
# {% if %}
'''
<body>
    <h1>{{ blog_name|title }} Blog Post</h1>
    {% if blog_text %}
        <h2>{{ blog_text }}</h2>
    {% else %}
        <h2>"Blog is in progress...</h2>
    {% endif %}
</body>
'''
# Here {% endif %} is necessary at the end.