from django import forms
from django.core.exceptions import ValidationError

from game.models import Word, User


class UserName(forms.ModelForm):
    name = forms.TextInput()

    class Meta:
        model = User
        fields = ('name',)


class InputWord(forms.ModelForm):
    input_word = forms.TextInput()

    class Meta:
        model = Word
        fields = ('word',)

    def word__clean(self):
        word = self.cleaned_data["word"]
        if len(word.split()) > 1:
            raise ValidationError('Should be one word!')
        return word
