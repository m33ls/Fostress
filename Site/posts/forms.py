from django import forms
from .models import Post
 
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('post_title', 'image', 'post_text', 'post_author')
        exclude = ('post_author',)
    def __init__(self, *args, **kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['post_title'].widget.attrs.update({'class':'form-control','placeholder':'Enter title (60 characters max)'})
        self.fields['image'].widget.attrs.update({'class':'form-control','placeholder':'Upload image'})
        self.fields['post_text'].widget.attrs.update({'class':'form-control','placeholder':'Write your post...'})