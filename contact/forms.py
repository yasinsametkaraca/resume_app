from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):  # Model içerisindeki alanlar database e kayıt için geçerli validasyonlar. Buradaki alanlar ise form alanları için geçerli validasyonlar. Yani formun gönderim aşamasındaki validasyonlar. Yani database e gitmeden hata göstericez.
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=250, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))

    # def send_mail(self):  # kullanıcıya mail göndermek için kullanıcaz. (Mesajınız alındı gibi)
    #     if self.is_valid():
    #         name = self.cleaned_data.get('name')
    #         email = self.cleaned_data.get('email')
    #         subject = self.cleaned_data.get('subject')
    #         message = self.cleaned_data.get('message')
    #
    #         message_context = 'Message received.\n\n' \
    #                           'Name: %s\n' \
    #                           'Subject: %s\n' \
    #                           'Email: %s\n' \
    #                           'Message: %s' % (name, subject, email, message)
    #
    #         email_message = EmailMessage(
    #             subject=subject,
    #             body=message_context,
    #             to=[settings.DEFAULT_FROM_EMAIL],  # Buraya mail adresi yazılır. Buraya yazılan mail adresine mail gönderilir.
    #             reply_to=[email],
    #         )
    #         email_message.send()
