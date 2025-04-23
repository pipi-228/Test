INSTALLED_APPS = [
    ...
    'volunteers',
]

AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/profile/'
