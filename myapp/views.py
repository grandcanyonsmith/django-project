from django.shortcuts import render
from .forms import AudioUrlForm
import requests
import json

def submit_audio_url(request):
    if request.method == 'POST':
        form = AudioUrlForm(request.POST)
        if form.is_valid():
            audio_url = form.cleaned_data['audio_url']
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({'audio_url': audio_url})
            response = requests.post('https://kuwvhekcm6.execute-api.us-east-1.amazonaws.com/dev/transcribe', headers=headers, data=data)
            return render(request, 'myapp/response.html', {'response': response.text})
    else:
        form = AudioUrlForm()

    return render(request, 'myapp/submit_audio_url.html', {'form': form})
