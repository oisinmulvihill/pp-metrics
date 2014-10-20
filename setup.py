# -*- coding: utf-8 -*-
"""
"""
from setuptools import setup, find_packages

Name = "pp-metrics"
ProjectUrl = ""
Version = "1.0.0"
Author = 'Oisin Mulvihill'
AuthorEmail = 'oisin mulvihill at gmail'
Maintainer = ''
Summary = 'Scales metrics integration helper for pp-web-base apps.'
License = ''
Description = Summary
ShortDescription = Summary


needed = [
    "scales",
]

test_needed = [
    "pytest-cov",
]

test_suite = ''

EagerResources = [
    'pp',
]

ProjectScripts = [
]

PackageData = {
    '': ['*.*'],
}


# [console] ??
#     testing = pp.testing.scripts.app:main
EntryPoints = """
"""

setup(
    url=ProjectUrl,
    name=Name,
    zip_safe=False,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    classifiers=[
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
    ],
    keywords='python',
    license=License,
    scripts=ProjectScripts,
    install_requires=needed,
    tests_require=test_needed,
    test_suite=test_suite,
    include_package_data=True,
    packages=find_packages(),
    package_data=PackageData,
    eager_resources=EagerResources,
    entry_points=EntryPoints,
    namespace_packages=['pp'],
)
