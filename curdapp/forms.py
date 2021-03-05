from django import forms

class InsertForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Your Product_id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product_id'
            }
        )
    )

    product_Name = forms.CharField(
        label="Enter Your Product_Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_Name'
            }
        )
    )

    product_class = forms.CharField(
        label="Enter Your Product_class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_class'
            }
        )
    )

    product_color = forms.CharField(
        label="Enter Your Product_color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_color'
            }
        )
    )

    product_weight = forms.IntegerField(
        label="Enter Your Product_weight",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_weight'
            }
        )
    )

    product_cost = forms.IntegerField(
        label="Enter Your Product_cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_cost'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product_id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product_cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_cost'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product_id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product_id'
            }
        )
    )
