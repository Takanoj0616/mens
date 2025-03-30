from django import forms
from review.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['girl', 'customer_name', 'visit_date', 'comment']
        widgets = {
            'girl': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'visit_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }