from cProfile import label
from tkinter.ttk import LabeledScale
from xml.dom import ValidationErr
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "gpa")
        labels = {
            "name": "Full Name",
        }

    def clean_gpa(self):
        gpa =  self.cleaned_data["gpa"]
        if gpa<=0:
            raise ValidationErr("Gpa must be greater than zero!")
        if gpa>100:
            raise ValidationErr("Gpa must be less than 100")
        return  gpa
   
