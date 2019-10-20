from django import forms


class ContactForm(forms.Form):
	from_email = forms.EmailField(
		required=True, widget=forms.EmailInput(
			attrs={
			'class' : 'col s12 m8 l8 xl6'
			}
			)
		)

	subject = forms.CharField(
		required=True, widget=forms.EmailInput(
			attrs={
			'class' : 'col s12 m8 l8 xl6'
			}
			)
		)
	message = forms.CharField(required=True, widget=forms.EmailInput(
			attrs={
			'class' : 'col s12 m8 l8 xl6'
			}
			)
	)