from django.shortcuts import render


from .forms import ImageForm
# Create your views here.


class ImageFormView(LoginRequiredMixin, FormView):
    template_name = 'imageapp/form-send-img.html'
    form_class = ImageForm
    success_url = 'form_send_img_success'

    def form_valid(self, form):
        sended_image = form.save(commit=False)
        sended_image.user = self.request.user
        # sended_image = sended_image.zi
        sended_image.save()
        return super().form_valid(form)
