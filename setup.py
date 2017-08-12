from setuptools import setup, find_packages


version = __import__('autoreloader').__version__

setup(
    name='django-autoreloader',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Autoreload files in browser for Django development',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-autoreloader',
    download_url='https://github.com/synw/django-autoreloader/releases/tag/' + version,
    keywords=['django', 'development'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        "websocket-server",
        "pyinotify"
    ],
    zip_safe=False
)
