from django import forms

class AudioUrlForm(forms.Form):
    audio_url = forms.URLField(label='Audio URL', required=True)
