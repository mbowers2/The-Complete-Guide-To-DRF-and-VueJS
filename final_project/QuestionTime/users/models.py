from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''
    This user class inherits the django AbstractUser, which includes a number
    of built-in fields like username, email, etc. We are using this custom 
    class in case we'd want to add something more later.
    '''
    pass
