# CORS_ORIGIN_WHITELIST = (
#     'localhost:3000',
#     '127.0.0.1:3000',
#     'http://localhost:3000',
#     '*',
# )

# CORS_ORIGIN_WHITELIST = (
#     '*',
# )

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_HEADERS = (
#     '*',
# )
# CORS_URLS_REGEX = r'^/api/.*$'
#
# CORS_ALLOW_METHODS = (
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# )

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-origin',
)
