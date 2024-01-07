
from io import BytesIO
from django import forms
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .serializers import ImageModelSerializer, ImageCommentModelSerializer
from rest_framework.viewsets import ModelViewSet

from .forms import ImageForm, ExpiringLinkForm
from .models import Image, ImageComment, ExpiringLink
from users_app.models import UserAccountTier, UserProfile


from datetime import timedelta, timezone

# Create your views here.


class HomeView(ListView):
    model = Image
    template_name = 'image_app/index.html'
    context_object_name = 'image_list'
    ordering = ['-uploaded_at']


class ImageFormView(LoginRequiredMixin, FormView):
    template_name = 'image_app/form_upload_img.html'
    form_class = ImageForm
    success_url = reverse_lazy('image_app:success')

    def form_valid(self, form):
        sended_image = form.save(commit=False)
        sended_image.user = self.request.user
        sended_image.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'success.html'


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image_app/image_detail.html'
    context_object_name = 'image_instance'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_comments = ImageComment.objects.filter(img=self.object)
        tiers = UserAccountTier.objects.all()
        user_profile = UserProfile.objects.get(user=self.request.user.id)

        context['image_comments'] = image_comments
        context['tiers'] = tiers
        context['user_profile'] = user_profile
        return context


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'image_app/image_update.html'
    form_class = ImageUpdateForm
    success_url = reverse_lazy('image_app:success')

    # def get_success_url(self):
    #     return reverse_lazy('success')

    # def get_success_url(self):
    #     return reverse_lazy('image_detail', kwargs={'pk': self.object.pk})


class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'image_app/image_delete.html'
    success_url = reverse_lazy('image_app:success')


# class ImageMixin:
#     model = Image
#     template_name = 'image_app/image_update_delete.html'
#     form_class = ImageUpdateForm

#     def get_success_url(self):
#         return reverse_lazy('image_detail', kwargs={'pk': self.object.pk})


class GenerateExpiringLinkView(LoginRequiredMixin, View):
    template_name = 'image_app/generate_exp_link.html'

    def get(self, request, image_id, th_time=310):
        image = Image.objects.get(pk=image_id)
        form = ExpiringLinkForm()

        try:
            link = ExpiringLink.objects.get(img=image)
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': link})
        except ExpiringLink.DoesNotExist:
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': False})

    def post(self, request, image_id, th_time=310):
        image = Image.objects.get(pk=image_id)
        form = ExpiringLinkForm(
            request.POST)

        if 'create_link' in request.POST:

            if form.is_valid():
                link = form.save(commit=False)
                link.img = image
                link.save()

                try:
                    link = ExpiringLink.objects.get(img=image)
                    return render(request, self.template_name,
                                  {'image': image, 'form': form,
                                   'links': link})
                except ExpiringLink.DoesNotExist:
                    return render(request, self.template_name,
                                  {'image': image, 'form': form,
                                   'links': False})
            else:
                print('Error in form', form.errors)

            return render(request, self.template_name,
                          {'image': image, 'form': form})

        elif 'delete_links' in request.POST:
            form = ExpiringLinkForm()

            try:
                lin = request.POST.get('delete_links')
                link = ExpiringLink.objects.get(name=lin)
                link.delete()

                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})
            except ExpiringLink.DoesNotExist:
                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})


@login_required
def generate_thumbnail(request, image_id, th_width, th_height):
    image = Image.objects.get(pk=image_id)

    if image.image_file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        img = Image.open(image.image_file.path)
        img = img.convert('RGB')

        width, height = img.width, img.height
        aspect_ratio = th_width / th_height
        img_aspect_ratio = width / height

        if img_aspect_ratio < aspect_ratio:
            new_height = int(width / aspect_ratio)
            top = (height - new_height) // 2
            bottom = top + new_height
            img = img.crop((0, top, width, bottom))
        else:
            new_width = int(height * aspect_ratio)
            left = (width - new_width) // 2
            right = left + new_width
            img = img.crop((left, 0, right, height))

        img.thumbnail((th_width, th_height))
        thumbnail_io = BytesIO()
        img.save(thumbnail_io, 'JPEG')
        response = HttpResponse(content_type='image/jpeg')
        response.write(thumbnail_io.getvalue())

        return response
    else:
        raise Http404(
            "Unsupported image format. Thumbnails can be created from jpg jpeg png formats.")


class GenerateExpiringLinkView(LoginRequiredMixin, View):
    template_name = 'image_app/generate-exp-link.html'

    def get(self, request, image_id, th_time=310):
        image = Image.objects.get(pk=image_id)
        form = ExpiringLinkForm()

        try:
            link = ExpiringLink.objects.get(img=image)
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': link})
        except ExpiringLink.DoesNotExist:
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': False})

    def post(self, request, image_id, th_time=310):
        image = Image.objects.get(pk=image_id)
        form = ExpiringLinkForm(
            request.POST)  # request.POSt - for make work form in adding links

        if 'create_link' in request.POST:

            if form.is_valid():
                link = form.save(commit=False)
                link.img = image
                link.save()

                try:
                    link = ExpiringLink.objects.get(img=image)
                    return render(request, self.template_name,
                                  {'image': image, 'form': form,
                                   'links': link})
                except ExpiringLink.DoesNotExist:
                    return render(request, self.template_name,
                                  {'image': image, 'form': form,
                                   'links': False})
            else:
                print('Error in form', form.errors)

            return render(request, self.template_name,
                          {'image': image, 'form': form})

        elif 'delete_links' in request.POST:
            form = ExpiringLinkForm()

            try:
                lin = request.POST.get('delete_links')
                link = ExpiringLink.objects.get(name=lin)
                link.delete()

                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})
            except ExpiringLink.DoesNotExist:
                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})


def show_generate_thumbnail(request, image_id, link_name):
    image = Image.objects.get(pk=image_id)
    link = ExpiringLink.objects.get(name=link_name)

    current_time = timezone.now()
    creation_time = link.creation_time
    exp = link.expiration
    expiration = timedelta(seconds=exp)
    expiration_time = creation_time + expiration

    context = {'image': image,
               'link': link,
               'exp': expiration_time,
               'current_time': current_time, }

    return render(request, 'image_app/show-link.html', context)
# API ViewSets


class ImageModelViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer


class ImageCommenModelViewSet(ModelViewSet):
    queryset = ImageComment.objects.all()
    serializer_class = ImageCommentModelSerializer
