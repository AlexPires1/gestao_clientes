from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = "Nome"
        self.fields["last_name"].label = "Sobrenome"
        self.fields["age"].label = "Idade"
        self.fields["salary"].label = "Salário"
        self.fields["bio"].label = "Bio"
        self.fields["photo"].label = "Foto"


class EditPersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    def __init__(self, *args, **kwargs):
        super(EditPersonForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = "Nome"
        self.fields["last_name"].label = "Sobrenome"
        self.fields["age"].label = "Idade"
        self.fields["salary"].label = "Salário"
        self.fields["bio"].label = "Bio"
        self.fields["photo"].label = "Foto"