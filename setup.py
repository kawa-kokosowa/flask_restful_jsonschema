from setuptools import setup


exec(open('flask_restful_jsonschema/__init__.py').read())
setup(name='flask_restful_jsonschema',
      packages=['flask_restful_jsonschema'],
      version=__version__,
      description='Provides a wrapper which provides valid json to Resource methods.',
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      author='Lily Seabreeze',
      author_email='lillian.gardenia.seabreeze@gmail.com',
      license='MIT',
    )

