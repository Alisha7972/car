from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .forms import UserForm
from .models import User


def index(request):
    form = UserForm()
    members = User.objects.all().order_by('-created_at')
    # initial full page render (includes the list partial)
    return render(request, 'members/index.html', {'form': form, 'members': members})


def members_list_partial(request):
    members = User.objects.all().order_by('-created_at')
    html = render_to_string('members/_list.html', {'members': members}, request=request)
    return HttpResponse(html)


def create_member(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            members = User.objects.all().order_by('-created_at')
            html = render_to_string('members/_list.html', {'members': members}, request=request)
            return HttpResponse(html, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'POST required'}, status=405)


def member_json(request, pk):
    m = get_object_or_404(User, pk=pk)
    data = {
        'id': m.id,
        'name': m.name,
        'email': m.email or '',
        'age': m.age if m.age is not None else '',
        'notes': m.notes or '',
    }
    return JsonResponse(data)


def update_member(request, pk):
    m = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=m)
        if form.is_valid():
            form.save()
            members = User.objects.all().order_by('-created_at')
            html = render_to_string('members/_list.html', {'members': members}, request=request)
            return HttpResponse(html)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'POST required'}, status=405)


def delete_member(request, pk):
    m = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        m.delete()
        members = User.objects.all().order_by('-created_at')
        html = render_to_string('members/_list.html', {'members': members}, request=request)
        return HttpResponse(html)
    return JsonResponse({'error': 'POST required'}, status=405)
