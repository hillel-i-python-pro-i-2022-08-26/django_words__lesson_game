from django import forms
from django.core.exceptions import ValidationError

from game.models import Word, User


class UserName(forms.ModelForm):
    name = forms.TextInput()

    class Meta:
        model = User
        fields = ('name', )


class InputWord(forms.ModelForm):
    input_word = forms.TextInput()

    class Meta:
        model = Word
        fields = ("word",)

    def clean_word(self):
        word = self.cleaned_data["word"]
        if len(word.split()) > 1:
            raise ValidationError('Should be one word!')
        elif not word.isalpha():
            raise ValidationError('Should not consist of numbers and signs')
        
        return word
