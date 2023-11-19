from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ImageForm, ExpiringLinkForm
from .models import ImageModel, ExpiringLinkModel


class ImageFormView(LoginRequiredMixin, FormView):
    template_name = 'imageapp/form_upload_img.html'
    form_class = ImageForm
    success_url = 'form_send_img_success'

    def form_valid(self, form):
        sended_image = form.save(commit=False)
        sended_image.user = self.request.user
        sended_image.save()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'templates/success.html'


class GenerateExpiringLinkView(LoginRequiredMixin, View):
    template_name = 'imageapp/generate_exp_link.html'

    def get(self, request, image_id, th_time=310):
        image = ImageModel.objects.get(pk=image_id)
        form = ExpiringLinkForm()

        try:
            link = ExpiringLinkModel.objects.get(img=image)
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': link})
        except ExpiringLinkModel.DoesNotExist:
            return render(request, self.template_name,
                          {'image': image, 'form': form, 'links': False})

    def post(self, request, image_id, th_time=310):
        image = ImageModel.objects.get(pk=image_id)
        form = ExpiringLinkForm(
            request.POST)

        if 'create_link' in request.POST:

            if form.is_valid():
                link = form.save(commit=False)
                link.img = image
                link.save()

                try:
                    link = ExpiringLinkModel.objects.get(img=image)
                    return render(request, self.template_name,
                                  {'image': image, 'form': form,
                                   'links': link})
                except ExpiringLinkModel.DoesNotExist:
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
                link = ExpiringLinkModel.objects.get(name=lin)
                link.delete()

                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})
            except ExpiringLinkModel.DoesNotExist:
                return render(request, self.template_name,
                              {'image': image, 'form': form, 'links': False})
