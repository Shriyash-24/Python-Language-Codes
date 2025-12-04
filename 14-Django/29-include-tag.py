## The idea is to not use entire html file as the base template but having a small html snippet.
# Eg - Navigation bar.

# We can outsource this in base.html but it could lead to issues.
# So now what to do? We use include tag.
# So we created includes folder in blogs folder. We named it header.html.
# {% include "blogs/includes/header.html" %}