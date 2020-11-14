"""Setup script."""
import os

import glob
import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


def get_requirements(filename):
    with open(filename) as f:
        requirements = f.readlines()
    return requirements


requirements = get_requirements(os.path.join(this_directory, 'requirements.txt'))

setuptools.setup(name='ds-distcal',
                 version='1.0.0',
                 description='project_description',
                 long_description=long_description,
                 classifiers=[
                     "Development Status :: 2 - Pre-Alpha",
                     "Programming Language :: Python :: 3 :: Only",
                     "Programming Language :: Python :: 3.6"
                 ],
                 keywords='keywords',
                 url='http://bitbucket.org/odigeoteam/ds-distcal',
                 # author='eDreams ODIGEO',
                 author_email='mail',
                 license='COPYRIGHT',
                 packages=setuptools.find_packages('src'),
                 package_dir={'': 'src'},
                 py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')],
                 include_package_data=True,
                 install_requires=requirements,
                 entry_points={'console_scripts':
                                   ['distcal_get_data=distcal.get_data:main'
                                    ]}
                 )
