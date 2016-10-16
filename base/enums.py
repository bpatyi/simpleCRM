from base.exceptions import NotFoundOptionExcpetion


class Enum(object):

    _CHOICES = {}

    @classmethod
    def get_options(cls):
        return {
            value: value
            for name, value in vars(cls).items()
            if not name.startswith('_')
        }

    @classmethod
    def is_option(cls, option):
        return option in cls.get_options().keys()

    @classmethod
    def get_choices(cls):
        return cls._CHOICES

    @classmethod
    def option_to_string(cls, option):
        translation = cls.get_choices().get(option)

        if not translation:
            raise NotFoundOptionExcpetion

        return translation
