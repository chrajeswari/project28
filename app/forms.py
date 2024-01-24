from django import forms

from app.models import *

class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
    
class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        exclude=['url']
        labels={'topic_name':'tn','name':'NAME'}
        widgets={'topic_name':forms.PasswordInput}




class AccessRecordform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'