from .forms import ReserveForm, LogForm, UpdateLogForm
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Log, Reserve
from django.urls import reverse
from django.http import HttpResponse, request


class AllListView(ListView):
    template_name = 'reserving/alllist.html'
    context_object_name = 'reserve_list'
    queryset = Reserve.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Reserve.objects.all()
        else:
            return Reserve.objects.filter(customer_name=current_user.username)

"""
関数ベース
def index(request):
    reserving_list = Reserve.objects.all()
    return render(request, 'reserving/index.html', {'reserving_list': reserving_list})
"""


class ReserveDetailView(DetailView):
    model = Reserve
    template_name = 'reserving/detail.html'


class RegisterReserveView(CreateView):
    model = Reserve
    form_class = ReserveForm
    template_name = 'reserving/register.html'
    
    def get_success_url(self):
        return reverse('reserving:reserve_detail', kwargs={'pk': self.object.pk })



def registerreserve(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.customuser = request.user
            d.save()
            return redirect('reserving::reserve_detail')
    
    else:
        form = ReserveForm()
    return render(request, 'reserving/register.html', {'form': form})


class UpdateReserveView(UpdateView):
    model = Reserve
    form_class = ReserveForm
    template_name = "reserving/alllist"


class WritingLogView(CreateView):
    model = Log
    form_class = LogForm
    template_name = "reserving/writinglog.html"
    def get_success_url(self):
        return reverse('reserving:reserve_detail', kwargs={'pk': self.object.reserve.pk})

    
class UpdateLogView(UpdateView):
    model = Log
    form_class = UpdateLogForm
    template_name = 'reserving/writinglog.html'
    def get_success_url(self):
        return reverse('reserving:reserve_detail', kwargs={'pk': self.object.reserve.pk})


class DeleteLogView(DeleteView):
    model = Log
    def get_success_url(self):
        return reverse('reserving:reserve_detail', kwargs={'pk': self.object.reserve.pk })

"""
def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    reserve_id = obj.reserve.pk
    if request.method == "POST":
        obj.delete()
        return redirect('reserving:reserve_detail', pk=reserve_id)
    context = {'obj': obj}
    return render(request, "reserving/delete.html", context)
"""


class DeleteReserveView(DeleteView):
    model = Reserve
    def get_success_url(self):
        return reverse('reserving:alllist')

"""
def deletereserve(request, pk):
    obj = get_object_or_404(Reserve, id=pk)
    if request.mehtod == "POST":
        obj.delete()
        return redirect('reserving:index')
    context = {'obj': obj}
    return render(request, "reserving/delete.html", context)
"""


def writingthisresrvelog(request, pk):
    obj = get_object_or_404(Reserve, id=pk)
    form = LogForm({'reserve':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('reserving:reserve_detail', pk=l.reserve.pk)
    else:
        return render(request, 'reserving/register.html', {'form': form})

"""
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render ( request, 'create.html', {'form': form})
    

class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valied():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form})
"""

