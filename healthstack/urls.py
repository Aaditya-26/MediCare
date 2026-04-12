from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hospital import views
from django.contrib.auth import views as auth_views

admin.site.site_header = "MediCare"

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Fix: debug toolbar was unconditionally loaded in urls — must only be active in DEBUG mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
