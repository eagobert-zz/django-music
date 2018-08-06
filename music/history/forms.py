from django import forms


class AlbumForm(forms.Form):
    """ Form model represents and album """
    title = forms.CharField(label='Album Title', max_length=100)
    label = forms.CharField(label='Album Label', max_length=100)