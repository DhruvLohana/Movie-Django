from django.urls import path
from .views import EditProfile, Signup
from django.contrib.auth import views as auth_views
from user.views import UserProfile,LandingView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', next_page='landing'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('profile/<username>/', UserProfile, name='profile'),
    path('profile/edit', EditProfile, name='edit-profile'),
    path('signup/', Signup, name='register'),
    # Ensure you have a landing page URL pattern
    path('landing/', LandingView, name='landing'),  # Example landing page view
]
