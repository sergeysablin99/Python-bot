from setuptools import setup

requirements = [
    # TODO: put package requirements here
    'requests',
    'datetime'
]

test_requirements = [
    # TODO: put package test requirements here
    'requests',
    'datetime'
]

setup(
    name='Python-bot',
    version='0.1.0',
    description='Bot to notify you about plans via VK',
    long_description="readme + '\n\n' + history",
    author="Sergey Sablin",
    author_email='serewkasablin@outlook.com',
    url='https://github.com/notification-bot/Python-bot',
    packages=[
        'Python-bot',
    ],
    package_dir={'Python-bot':
                 'Python-bot'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Python-bot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
