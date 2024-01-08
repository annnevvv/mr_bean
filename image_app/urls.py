from django.urls import path
from django.conf.urls.static import static

from mr_bean import settings

from .views import HomeView, ImageFormView, SuccessView, GenerateExpiringLinkView, generate_thumbnail, ImageDetailView, ImageUpdateView, ImageDeleteView


app_name = 'image_app'

urlpatterns = [

    # CRUD
    path('form_upload_img', ImageFormView.as_view(), name='form-upload-img'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(),
         name='image_update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(),
         name='image_delete'),


    # DETAIL
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),

    # THUMBNAIL GENERATE
    path('generate-thumbnail', generate_thumbnail, name='generate-thumbnail'),
    path('generate_expiring_link/<int:image_id>/<int:th_time>',
         GenerateExpiringLinkView.as_view()),

    # OTHER

    path('success', SuccessView.as_view(),
         name='success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
