# Django
# Third Party
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    ButtonHolder,
    Column,
    Fieldset,
    Layout,
    Row,
    Submit,
)
from django import forms
from django.utils.translation import gettext as _


class PaymentForm(forms.Form):
    credit_card_number = forms.CharField(
        label=_('Credit Card Number'),
        required=False,  # Required only if Credit Card is selected
        max_length=16,
        widget=forms.TextInput(attrs={'placeholder': _('1234 5678 9012 3456')}),
    )
    cvv = forms.CharField(
        label=_('CVV'),
        required=False,  # Required only if Credit Card is selected
        max_length=3,
        widget=forms.TextInput(attrs={'placeholder': '123'}),
    )
    expiration_date = forms.DateField(
        label=_('Expiration Date'),
        required=False,  # Required only if Credit Card is selected
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'wger-form'
        self.helper.layout = Layout(
            Fieldset(
                _('Payment Details'),
                'payment_method',
                Row(
                    Column('credit_card_number', css_class='col-6'),
                    Column('cvv', css_class='col-3'),
                    Column('expiration_date', css_class='col-3'),
                    css_class='form-row',
                ),
            ),
            ButtonHolder(Submit('submit', _('Submit'), css_class='btn-success btn-block')),
        )

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')
        credit_card_number = cleaned_data.get('credit_card_number')
        cvv = cleaned_data.get('cvv')
        expiration_date = cleaned_data.get('expiration_date')

        # Validate credit card fields only if the credit card option is selected
        if payment_method == 'credit_card' and not (credit_card_number and cvv and expiration_date):
            raise forms.ValidationError(_('Complete credit card information is required.'))

        return cleaned_data
