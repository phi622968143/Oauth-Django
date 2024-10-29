pip install social_django
"social_django.middleware.SocialAuthExceptionMiddleware"

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/accounts/auth/login/google-oauth2/'  # Correct login URL for OAuth
LOGIN_REDIRECT_URL = '/home/'  # Where to redirect after login
LOGOUT_REDIRECT_URL = '/login/'  # Where to redirect after logout

path('accounts/', include('social_django.urls', namespace='social')), 

<a href="{% url 'social:begin' 'google-oauth2' %}">Login with Google</a>

http://localhost:8000/login/ to test

login_req to protect view
