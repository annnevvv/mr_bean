

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework.viewsets import ModelViewSet

from image_app.models import ImageModel

from .models import UserAccountTier, UserProfile
from .forms import UserForm, UserProfileForm

from .serializers import UserAccountTierSerializer, UserProfileModelSerializer

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
    template_name = 'users_app/dashboard.html'
    paginate_by = 24

    def get(self, request):
        tiers = UserAccountTier.objects.all()
        user = request.user
        user_profile = UserProfile.objects.get(user=user)

        print(f"user_profile: {user_profile}")

        img_sended_by_user = ImageModel.objects.filter(
            user=user.id).order_by('-uploaded_at')

        print(f"user_profile_mini: {img_sended_by_user}")

        context = {
            'tiers': tiers,
            'user': user,
            'user_profile': user_profile,
            'img_sended_by_user': img_sended_by_user[0:3],
        }
        return render(request, self.template_name, context)


class UserGallery(LoginRequiredMixin, View):
    template_name = 'users_app/user_gallery.html'
    paginate_by = 24

    def get(self, request):
        tiers = UserAccountTier.objects.all()
        user = request.user
        user_profile = UserProfile.objects.get(user=user)

        print(f"user_profile: {user_profile}")

        img_sended_by_user = ImageModel.objects.filter(
            user=user.id).order_by('-uploaded_at')

        print(f"user_profile_mini: {img_sended_by_user}")

        context = {
            'tiers': tiers,
            'user': user,
            'user_profile': user_profile,
            'img_sended_by_user': img_sended_by_user,
        }
        return render(request, self.template_name, context)


class UserProfileDetailView(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'users_app/user_profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context['user_profile'] = user_profile

        form = UserForm()
        context['form'] = form

        return context

    def post(self, request):
        form = UserForm(request.POST)
        profile = UserProfile.objects.get(pk=self.request.user_id)

        return render(request, self.template_name,
                      {'form': form, })


# API ViewSets

class UserAccountTierViewSet(ModelViewSet):
    queryset = UserAccountTier.objects.all()
    serializer_class = UserAccountTierSerializer


class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer
