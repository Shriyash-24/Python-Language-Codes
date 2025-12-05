# Segregating into pages is known as Pagination.
"""
Settings.py addition -->

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}
"""
"""
“Whenever you return a list of objects,
don’t give everything at once.
Use the Limit-Offset style pagination by default.”
PAGE SIZE = 5.
"""
