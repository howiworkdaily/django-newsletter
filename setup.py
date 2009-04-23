from setuptools import setup, find_packages
 
setup(
    name='django-newsletter',
    version='0.3.0',
    description='A basic, reusable newsletter subscription (opt-in/out) application.',
    author='Kevin Fricovsky',
    author_email='kfricovsky@gmail.com',
    url='http://github.com/howiworkdaily/django-newsletter/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

