from django.db import models

class UpperCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.is_uppercase = kwargs.pop('uppercase', False)
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper() if self.is_uppercase else value
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCharField, self).pre_save(model_instance, add)