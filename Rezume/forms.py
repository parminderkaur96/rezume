from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100,widget=forms.TextInput(attrs={'class': "form-control",'style':
                                                                                               'width:85%'}))
    email = forms.EmailField(label="Your email", max_length=100,widget=forms.TextInput(attrs={'class': "form-control",'style':
                                                                                               'width:85%'}))
    message = forms.CharField(label="Your message", max_length=100,widget=forms.TextInput(attrs={'class': "form-control",'style':
                                                                                               'width:85%'}))
    password = forms.CharField(label="Your password", max_length=100,widget=forms.TextInput(attrs={'class': "form-control",'style':
                                                                                               'width:85%'}))
    confirm_password = forms.CharField(label="Confirm password", max_length=100,widget=forms.TextInput(attrs={'class': "form-control",'style':
                                                                                               'width:85%'}))