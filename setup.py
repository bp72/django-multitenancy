from setuptools import setup


setup(
    name='django-multitenancy-plus',
    version='0.1.0',
    packages=['django_multitenancy', 'django_multitenancy/middleware'],
    url='',
    license='MIT',
    author='Pavel Bityukov',
    author_email='pavleg.bityukov@gmail.com',
    maintainer='Pavel Bityukov',
    maintainer_email='pavleg.bityukov@gmail.com',
    description='',
    python_requires='>=3.8',
    install_requires=['django>=4,<4.3'],
)
