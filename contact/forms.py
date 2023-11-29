from django import forms


class ContactForm(forms.Form):  # Model içerisindeki alanlar database e kayıt için geçerli validasyonlar. Buradaki alanlar ise form alanları için geçerli validasyonlar. Yani formun gönderim aşamasındaki validasyonlar. Yani database e gitmeden hata göstericez.
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=250, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
