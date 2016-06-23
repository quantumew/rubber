try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Utility for wrapping requests in proxy protocol.',
    'author': 'Andy Gertjejansen',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'andygertjejansen@outlook.com',
    'version': '0.1',
    'install_requires': [],
    'packages': [],
    'scripts': [
        "rubber",
    ],
    'name': 'rubber',
}

setup(**config)
