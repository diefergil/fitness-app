# Django
from crispy_forms.bootstrap import FormActions
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
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django.contrib.auth.models import User


class TrainerFormRecaptcha(forms.ModelForm):
    phone = forms.CharField(
        label=_('Phone'),
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    owner = forms.CharField(
        label=_('Owner'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    zip_code = forms.CharField(
        label=_('ZIP Code'),
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    city = forms.CharField(
        label=_('City'),
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    street = forms.CharField(
        label=_('Street'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'data-theme': 'light',
                'data-size': 'invisible',
                'data-badge': 'bottomright',
            }
        ),
        label='',
    )

    class Meta:
        model = User
        fields = ['email', 'phone', 'owner', 'zip_code', 'city', 'street']

    def __init__(self, *args, **kwargs):
        super(TrainerFormRecaptcha, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'email',
            'phone',
            'owner',
            'zip_code',
            'city',
            'street',
            'captcha',
            FormActions(
                Submit('save', _('Update'), css_class='btn-primary'),
                css_class='text-right',
            ),
        )


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
