from setuptools import setup, find_packages
import pyrabbit

# To update version number, edit:
# pyrabbit/__init__.py
version = ".".join(str(x) for x in pyrabbit.version)

setup(name='pyrabbit',
      version=version,
      description="A Pythonic interface to the RabbitMQ Management HTTP API", 

      long_description="""\

The main documentation lives at http://pyrabbit.readthedocs.org

There's no way to easily write programs against RabbitMQs management API
without resorting to some messy urllib boilerplate code involving HTTP 
Basic authentication and parsing the JSON responses, etc. Pyrabbit 
abstracts this away & provides an intuitive, easy way to work with the 
data that lives inside of RabbitMQ, and manipulate the resources there.""",

      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='python http amqp rabbit rabbitmq management',
      install_requires = ['httplib2'],
      author='Brian K. Jones',
      author_email='bkjones@gmail.com',
      url='http://www.github.com/bkjones/pyrabbit',
      download_url='http://www.github.com/bkjones/pyrabbit',
      license='MIT',
      packages=find_packages(exclude='tests'),
      include_package_data=False,
      zip_safe=False
      )
