from django.urls import path
from .views import RegisterView, AssignUserRoleList, UserSettings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('<int:user_id>/roles', AssignUserRoleList.as_view(), name='assign-role-to-user-list'),
    path('<int:user_id>/settings', UserSettings.as_view(), name='user-settings'),
]