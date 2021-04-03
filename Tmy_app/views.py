from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import City, Post, Profile
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    cities = City.objects.all()
    return render(request, 'Tmy_app/home.html', {'cities': cities})


# It searches for the Cities from database

class SearchView(TemplateView):
    template_name = "Tmy_app/city.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        search_value = self.request.GET.get('search', None)
        if search_value:
            context['data'] = City.objects.filter(city_name__icontains=search_value).values('city_name', 'created')
        else:
            context['data'] = City.objects.all().values('city_name', 'created', 'id')
        return context


def city_search(request):
    print("request" + str(request))

    queryset = City.objects.all()
    search = request.POST.get('search')
    context = {
        "object_list": queryset,
        "search": search,

    }
    return render(request, 'Tmy_app/city.html', context)


# .............City Detail Page...........
def detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    cities = City.objects.all()
    return render(request, 'Tmy_app/detail.html', {'cities': cities, 'city': city})


# ............NavBar Items....................................
def contacts(request):
    return render(request, 'Tmy_app/contacts.html')


def about_us(request):
    return render(request, 'Tmy_app/about_us.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'Tmy_app/users/register.html', {'form': form})


@login_required
def feedback_page(request):
    posts = Post.objects.all()
    return render(request, 'Tmy_app/users/feedback_page.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'Tmy_app/users/feedback_page.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


@login_required
def profile(request):
    return render(request, 'Tmy_app/users/profile.html')


