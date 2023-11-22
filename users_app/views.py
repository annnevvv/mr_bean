from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from image_app.models import ImageModel

from .models import UserAccountTier, UserProfileModel


# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserDasboard(LoginRequiredMixin, View):
    template_name = 'users/dashboard.html'
    paginate_by = 24

    def get(self, request):
        tiers = UserAccountTier.objects.all()
        user = request.user
        profile = UserProfileModel.objects.get(user=user)
        img_sended_by_user = ImageModel.objects.filter(
            user=user.id).order_by('-uploaded_at')

        context = {
            'tiers': tiers,
            'user': user,
            'profile': profile,
            'img_sended_by_user': img_sended_by_user,
        }
        return render(request, self.template_name, context)
