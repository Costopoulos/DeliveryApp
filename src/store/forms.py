from driver.models import order
from django import forms



class OrderForm(forms.ModelForm):
    time_to_pickup       = forms.CharField(label='', 
                    widget=forms.DateTimeInput(attrs={"placeholder": "Time to deliver"}))
    adress_to = forms.CharField(
                        required=True, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )    
    class Meta:
        model = order
        fields = [
            "time_to_pickup",
            'adress_to'
        ]