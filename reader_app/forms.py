from django import forms

from reader_app.models import Channel


class ChannelFollowForm(forms.Form):
    channel = forms.ModelChoiceField(queryset=Channel.objects.all(), widget=forms.HiddenInput)
