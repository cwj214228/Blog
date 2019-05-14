from django import forms


class WorkExperienceForm(forms.Form):
    start_time = forms.CharField(max_length=20)
    end_time = forms.CharField(max_length=20)
    position = forms.CharField(max_length=50)
    work_one = forms.CharField(max_length=200)
    work_two = forms.CharField(max_length=200)
    work_three = forms.CharField(max_length=200)
    work_four = forms.CharField(max_length=200)
    work_five = forms.CharField(max_length=200)
    work_skill_one = forms.CharField(max_length=200)
    work_skill_two = forms.CharField(max_length=200)
    work_skill_three = forms.CharField(max_length=200)
    work_skill_four = forms.CharField(max_length=200)
    work_skill_five = forms.CharField(max_length=200)