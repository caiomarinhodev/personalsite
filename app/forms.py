from django import forms
from django.forms import ModelForm, inlineformset_factory
from app.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone phone'
            if field_name == 'cep' or field_name == 'postalcode':
                field.widget.attrs['class'] = 'form-control cep'


class ContactForm(BaseForm, ModelForm):
    class Meta:
        model = models.Contact
        fields = ("id", "name", "email", "subject", "message")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Contact)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


class ContactFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Contact
        fields = ("id", "name", "email", "subject")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Contact)

    def __init__(self, *args, **kwargs):
        super(ContactFormToInline, self).__init__(*args, **kwargs)



class CategoryForm(BaseForm, ModelForm):
    class Meta:
        model = models.Category
        fields = ("id", "name")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Category)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)


class CategoryFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Category
        fields = ("id", "name")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Category)

    def __init__(self, *args, **kwargs):
        super(CategoryFormToInline, self).__init__(*args, **kwargs)



class ProjectForm(BaseForm, ModelForm):
    class Meta:
        model = models.Project
        fields = ("id", "title", "description", "category", "project_date", "project_url")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Project)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)


class ProjectFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Project
        fields = ("id", "title", "category", "project_date", "project_url")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Project)

    def __init__(self, *args, **kwargs):
        super(ProjectFormToInline, self).__init__(*args, **kwargs)


ProjectCategoryFormSet = inlineformset_factory(models.Category, models.Project, form=ProjectFormToInline, extra=1)


class ProjectImageForm(BaseForm, ModelForm):
    class Meta:
        model = models.ProjectImage
        fields = ("id", "project", "image", "file_url", "is_poster")
        widgets = generate_bootstrap_widgets_for_all_fields(models.ProjectImage)

    def __init__(self, *args, **kwargs):
        super(ProjectImageForm, self).__init__(*args, **kwargs)


class ProjectImageFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.ProjectImage
        fields = ("id", "project", "file_url", "is_poster")
        widgets = generate_bootstrap_widgets_for_all_fields(models.ProjectImage)

    def __init__(self, *args, **kwargs):
        super(ProjectImageFormToInline, self).__init__(*args, **kwargs)


ProjectImageProjectFormSet = inlineformset_factory(models.Project, models.ProjectImage, form=ProjectImageFormToInline, extra=1)
