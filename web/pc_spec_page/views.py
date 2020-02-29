from django.shortcuts import render
from .models import PcSpecs


def spec_list(request):
    pcs = PcSpecs.objects.all()
    return render(request, 'pc_spec_page/index.html', {'pcs': pcs})
