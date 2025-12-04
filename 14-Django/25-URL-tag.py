## URL Tag
# Returns an absolute path reference matching a given view and optional parameters.

# <body>
#     <ul>
#         {% for blog in blogs %}
#             <li><a href="{% url 'blog-post' blog %}">{{ blog|capfirst}}</a></li>
# <!--                            {% url 'blog-post' blog=blog %}-->
#         {% endfor %}
#     </ul>
# </body>