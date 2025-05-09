from django import forms

CHART_CHOICES = (
        ("#1","Bar chart"),
        ("#2","Pie chart"),
        ("#3","Line chart"),
        )
RESULT_CHOICES = (
        ("#1","transaction"),
        ("#2","sale date"),
        )

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    result_by = forms.ChoiceField(choices=RESULT_CHOICES)

