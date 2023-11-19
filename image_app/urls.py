from django.urls import path

from .views import ImageFormView, ImageFormSuccessView, GenerateExpiringLinkView

app_name = 'image_app'

urlpatterns = [
    path('form_upload_img', ImageFormView.as_view(), name='form-upload-img'),
    path('success', ImageFormSuccessView.as_view(),
         name='success'),
    path('generate_expiring_link/<int:image_id>/<int:th_time>',
         GenerateExpiringLinkView.as_view()),
]
