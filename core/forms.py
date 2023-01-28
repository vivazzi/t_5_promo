from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваше ФИО*', 'class': 'small-text'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш email*', 'class': 'small-text'})
    )

    phone = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон*', 'class': 'small-text'})
    )

    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение*', 'class': 'small-text', 'rows': 3})
    )

    agreement = forms.BooleanField(required=True)
