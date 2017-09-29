
from app.exceptions import ValidatorException, NotImplementedException

class CommonValidator(object):

    @classmethod
    def validate(self):
        raise NotImplementedException("{}: does not have a validate method.".format(type(self)))

    @classmethod
    def is_valid(self, *args, **kwargs):
        try:
            self.validate(*args, **kwargs)
            return True
        except ValidatorException as e:
            return False
