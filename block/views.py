from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from models import Block
from usercenter.models import ActivateCode

# Create your views here.

def block_list(request):
    blocks=Block.objects.all().order_by("-id")
    return render_to_response("block_list.html", {"blocks":blocks},context_instance=RequestContext(request))
    return redirect(reverse("login"))
