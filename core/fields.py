from django.db.models import CharField


class TitleField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 240
        super().__init__(*args, **kwargs)
