"""
Flask-Elastic-DSL
-------------
Easily serve your static files from aliyun oss.
"""
from setuptools import setup

__version__ = "0.1"

setup(
    name='flask-elastic-dsl',
    version=__version__,
    url='https://github.com/edison7500/flask-oss',
    license='MIT',
    author='jiaxin',
    author_email='edison7500@gmail.com',
    description='Flask-Elasticsearch-dsl',
    long_description=__doc__,
    py_modules=['flask_elastic_dsl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch-dsl>=5.3.0',
    ],
    tests_require=['nose', 'mock'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite = 'nose.collector'
)