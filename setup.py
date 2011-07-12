from setuptools import setup, find_packages

setup(
    name='pial',
    version='1.0',
    description='Image manipulations for a variety of Python imaging libraries.',
    long_description=open('README.rst').read(),
    author='Gregory Taylor and Mikko Hellsing',
    author_email='gtaylor@duointeractive.com',
    license='BSD',
    url='https://github.com/duointeractive/pial',
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        ],
    )

