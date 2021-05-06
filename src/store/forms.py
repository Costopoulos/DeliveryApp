from driver.models import order
from django import forms
from datetimewidget.widgets import DateTimeWidget


class OrderForm(forms.ModelForm):
    time_to_pickup = forms.CharField(label='Ημερομηνία και ώρα παράδοσης', 
                                    widget=forms.DateTimeInput(
                                                attrs={
                                                    "placeholder": "YΥΥΥ-ΜΜ-DD HH:MM",
                                                    "cols": 20,
                                                    "rows": 20
                                                }),
                                    required=True)
    adress_to = forms.CharField(
                        required=True, 
                        label='Διεύθυνση παράδοσης',
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Βάλτε διεύθυνση και σχόλια παραγγελίας",
                                    # "class": "new-class-name two",
                                    # "id": "my-id-for-textarea",
                                    #"rows": 5,
                                    'cols': 120
                                }
                        )
                )    
    price = forms.DecimalField(
                        required=True, 
                        label='Σύνολο',
                        widget=forms.NumberInput(
                                attrs={
                                    "placeholder": "Σε μορφή Ευρώ.Cents",
                                }
                        )
            )  
    isPaid = forms.BooleanField(
                        required=False, 
                        label='Έχει προπληρωθεί',
                        # widget=forms.NumberInput(
                        #         attrs={
                        #             "placeholder": "Σε μορφή Ευρώ.Cents",
                        #         }
                        # )
            ) 
    class Meta:
        model = order
        fields = [
            'time_to_pickup',
            'adress_to',
            'price',
            'isPaid'
        ]
        # widgets = {
        # 'datetime':DateTimeWidget(attrs={'id':""}, usel10n=True, bootstrap_version=3)
        # }