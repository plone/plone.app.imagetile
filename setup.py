from setuptools import setup, find_packages
import os

version = '1.0dev'

tests_require = [
    'interlude',
    'plone.app.testing',
    'plone.app.dexterity',
]

setup(name='plone.app.imagetile',
      version=version,
      description="A tile which displays an image.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Thomas Buchberger',
      author_email='t.buchberger@4teamwork.ch',
      url='https://github.com/plone/plone.app.imagetile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'plone.app.tiles',
          'plone.app.mediarepository',
          'plone.formwidget.querystring',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
