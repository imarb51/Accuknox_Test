from django.http import HttpResponse
from .models import ThreadModel
import threading

def thread_view(request):
    current_thread = threading.current_thread()
    print(f"Thread view running in thread: {current_thread.name}")
    
    ThreadModel.objects.create(name="Thread Test Object")
    
    return HttpResponse("Thread test completed. Check console for thread information.")