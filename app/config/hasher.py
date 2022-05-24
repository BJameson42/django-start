from os import environ

from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


class MyBcryptHasher(BCryptSHA256PasswordHasher):

    rounds = int(environ.get("HASHER_SALT_ROUNDS", default=12))
