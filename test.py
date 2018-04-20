import os

SOME_ENV = os.getenv('SOME_ENV', None)
# SOME_ENV = process.env.SOME_ENV
print(SOME_ENV)
