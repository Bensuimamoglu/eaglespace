from django import forms
from .models import Post, Comment, UserProfile

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'class': 'form-control'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PostForm(forms.ModelForm):
    image = MultipleFileField(required=False, label='Upload Images')
    video = MultipleFileField(required=False, label='Upload Videos')

    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...',
            'class': 'form-control'
            }))

    def save(self, commit=True):
        result = super().save(commit=commit)
        if commit:
            for image in self.cleaned_data.get('image', []):
                Image(post=result, image=image).save()
            for video in self.cleaned_data.get('video', []):
                Video(post=result, video=video).save()
        return result

    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    class Meta:
        model = Comment
        fields = ['comment']

class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'birth_date', 'location', 'picture', 'cover_photo']