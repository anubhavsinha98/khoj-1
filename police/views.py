from django.shortcuts import render
from guardian.models import *
from core import stats
import json
# Create your views here.
def get_analysis(request):
    lost_stats = stats.lost_stats()
    found_stats = stats.found_stats()
    lost_and_found_relation =  stats.lost_and_found_relation()
    # import pdb;pdb.set_trace()
    data = {'lost_stats': lost_stats,'found_stats' : found_stats,'lost_and_found_relation' : lost_and_found_relation}
    data = json.dumps(data)
    return render(request, 'analyze.html', {'json_string': data})