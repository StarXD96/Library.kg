from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Films
from .forms import FilmForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cineboard:film_list')
    else:
        form = RegisterForm()
    return render(request, 'cineboard/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cineboard:film_list')
    else:
        form = AuthenticationForm()
    return render(request, 'cineboard/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('cineboard:film_list')


class FilmListView(ListView):
    model = Films
    template_name = 'cineboard/film_list.html'
    context_object_name = 'films'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('tags')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset


def film_detail(request, pk):
    film = get_object_or_404(Films, pk=pk)
    return render(request, 'cineboard/film_detail.html', {'film': film})


@login_required
def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cineboard:film_list')
    else:
        form = FilmForm()
    return render(request, 'cineboard/film_form.html', {'form': form, 'action': 'Добавить'})


@login_required
def film_edit(request, pk):
    film = get_object_or_404(Films, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('cineboard:film_detail', pk=film.pk)
    else:
        form = FilmForm(instance=film)
    return render(request, 'cineboard/film_form.html', {'form': form, 'action': 'Сохранить'})


@login_required
def film_delete(request, pk):
    film = get_object_or_404(Films, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('cineboard:film_list')
    return render(request, 'cineboard/film_confirm_delete.html', {'film': film})
