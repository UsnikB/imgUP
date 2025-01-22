from django.views import generic
from . import forms
from django.urls import reverse_lazy

class CreatePhotoPostView(generic.CreateView):
    template_name = 'create_post_photo.html'
    form_class = forms.PostFormPicture
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.post_type = 'photo'
        return super().form_valid(form)

class CreateTextPostView(generic.CreateView):
    template_name = 'create_text_post.html'
    form_class = forms.PostFormText
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.post_type = 'text'
        return super().form_valid(form)
    
    