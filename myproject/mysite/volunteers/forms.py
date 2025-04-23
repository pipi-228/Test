from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Volunteer, Partner, Bonus

class VolunteerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=100)
    inn = forms.CharField(max_length=12)
    phone = forms.CharField(max_length=15)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    achievements = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.save()
        Volunteer.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            inn=self.cleaned_data['inn'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
            birth_date=self.cleaned_data['birth_date'],
            achievements=self.cleaned_data['achievements'],
            category=1,  # По умолчанию
            unique_code=f"VOL-{user.id}-{self.cleaned_data['inn'][-4:]}"
        )
        return user

class PartnerSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    contact_person = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_partner = True
        user.save()
        Partner.objects.create(
            user=user,
            company_name=self.cleaned_data['company_name'],
            contact_person=self.cleaned_data['contact_person'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email']
        )
        return user

class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = ['name', 'description', 'category_available', 'valid_from', 'valid_to']
