from django import forms
from .models import Tweet


class PictureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control form-group", "placeholder": "Your Name"}
        )
        self.fields["body"].widget.attrs.update(
            {
                "class": "form-control form-group form-label",
                "for": "exampleFormControlTextarea1",
                "placeholder": "What's going on?",
            }
        )
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control form-group",
                "placeholder": "Image",
            }
        )

    class Meta:
        model = Tweet
        fields = ["name", "body", "image"]
