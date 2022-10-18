from django import forms
from game.models import Word, User


class UserName(forms.Form):
    name = forms.TextInput()

    class Meta:
        model = User
        fields = ('name',)


class InputWord(forms.Form):
    input_word = forms.TextInput()

    class Meta:
        model = Word
        fields = ('word',)

    def word__clean(self):
        word = self.cleaned_data["word"]
        if len(word.split()) > 1:
            raise ValidationError('Should be one word!')
        return word
