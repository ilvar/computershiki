from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from badges.forms import UserBadgeForm
from badges.models import Badge


class HomeView(ListView):
    template_name = 'home.html'
    model = Badge

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data.update({
            'form': UserBadgeForm(),
        })
        return data

    def post(self, request, *args, **kwargs):
        f = UserBadgeForm(request.POST)

        if f.is_valid():
            f.save(user=request.user)

        return redirect('.')

home = HomeView.as_view()