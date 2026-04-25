from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hospital import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from whitenoise.middleware import WhiteNoiseMiddleware


admin.site.site_header = "MediCare"

class AdminSite(admin.AdminSite):
    def login(self, request, extra_context=None):
        if request.user.is_authenticated and not request.user.is_staff:
            return redirect('admin_login')
        return super().login(request, extra_context)

admin.site.__class__ = AdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('', include('hospital.urls')),
    path('doctor/', include('doctor.urls')),
    path('api/', include('api.urls')),
    path('hospital_admin/', include('hospital_admin.urls')),
    path('chat/', include('ChatApp.urls')),
    path('sslcommerz/', include('sslcommerz.urls')),
    path('pharmacy/', include('pharmacy.urls')),

    # Password reset flow
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset-password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
]

# Serve media files in both dev and production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]