from django.shortcuts import render, get_object_or_404
from .models import Member

# Create your views here.
def team(request):
	page_title = "Knowledge | Équipe"

	members = Member.objects.all().order_by('level')
	context = {
		'page_title': page_title,
		'members': members,
	}
	
	return render(request, "team/team.html", context)

def team_member(request, id):
	member = get_object_or_404(Member, id=id)

	page_title = "Knowledge | {}".format(member.get_fullname())

	context = {
		'page_title': page_title,
		'member': member,
	}
	
	return render(request, "team/team-member.html", context)

