from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group

@permission_required('auth.add_user', login_url='users:list')
def create(request):
	return render(request, 'users_create.html', {
		'groups': Group.objects.all(),
	})
