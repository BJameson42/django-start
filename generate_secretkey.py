from django.core.management.utils import get_random_secret_key

new_key: str = get_random_secret_key()
print(new_key)