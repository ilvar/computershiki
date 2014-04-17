from crispy_forms.bootstrap import InlineField
from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.layout import Div, HTML, Field, Submit, Row
from crispy_forms.helper import FormHelper, Layout

from badges.models import UserBadge, Badge


class UserBadgeForm(forms.ModelForm):
    badge = forms.CharField(label=_(u'Bagde'))

    class Meta:
        model = UserBadge
        fields = ['badge', 'year', 'description']

    def __init__(self, *args, **kwargs):
        super(UserBadgeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            Row(
                Div(
                    HTML(_(u'I have used')),
                    InlineField('badge', css_class='input-sm'),
                    HTML(_(u'in the year')),
                    InlineField('year', css_class='input-sm', min=1940, max=2014, value=2014),
                    HTML(_(u',')),
                    Submit('submit', _(u'really!'), css_class='input-sm'),
                    css_class='col-sm-12',
                )
            ),
            Row(
                Div(
                    Field('description'),
                    css_class='col-sm-12',
                ),
            )
        )

    def clean_badge(self):
        badge, _created = Badge.objects.get_or_create(title=self.cleaned_data['badge'])
        return badge

    def save(self, user=None, commit=True):
        if not UserBadge.objects.filter(badge=self.cleaned_data['badge'], user=user).exists():
            obj = super(UserBadgeForm, self).save(commit=False)
            obj.user = user
            if commit:
                obj.save()
            return obj
        else:
            return