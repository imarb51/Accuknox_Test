from django.http import HttpResponse
from .models import SyncModel
import time

def sync_view(request):
    start_time = time.time()
    print(f"Sync view started at {start_time}")
    
    SyncModel.objects.create(name="Sync Test Object")
    
    end_time = time.time()
    print(f"Sync view finished at {end_time}")
    
    return HttpResponse(f"Sync view execution time: {end_time - start_time} seconds")
