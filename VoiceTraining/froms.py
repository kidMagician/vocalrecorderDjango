from django import forms
from .models import TrainingVoice


class TrainingVoiceForm(forms.ModelForm):

    class Meta:
        model = TrainingVoice
        fields = ('voice','savedDate',)