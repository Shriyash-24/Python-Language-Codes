# In index.html, and we shifted in posts.html
'''

<section>
        <h2>Featured Posts</h2>
        <ul>
            {% for blog in blogs %}
                {% include 'blogs/includes/posts/html'}
            {% endfor %}
        </ul>
'''