# We create a base template and other for other templates.
# It should be create in a main project folder so we can use for other apps.
# {% block %} --> We can use it to inject the content. We need to use a name as wel..

# Look at base.html file.
# {% block page_title %}My blog{% endblock %}

# In allposts.html, at the top - {% extends "../../../templates/base.html "%} this is a relative path.
# Giving relative path is messy so we go in settings.py, in templates variable and in BASE_DIR, we write.. BASE_DIR / templates.

# allposts.html file now,
'''
{% extends "base.html" %}

{% block page_title %}
All Posts
{% endblock %}

{% block body_content %}
    <ul>
        {% for blog in blogs %}
            <li><a href="{% url 'blog-post' blog %}">{{ blog|capfirst}}</a></li>
<!--                            {% url 'blog-post' blog=blog %}-->
        {% endfor %}
    </ul>
{% endblock %}
'''