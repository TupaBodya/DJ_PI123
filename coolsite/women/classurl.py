from django.views.generic import RedirectView


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value

class CharConverter:
    regex = "[A-Za-z]"

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)

