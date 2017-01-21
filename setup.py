from setuptools import setup, find_packages
from os import path

setup_requires = [ ]

install_requires = [
    'numpy==1.12.0'
]

here = path.abspath( path.dirname( __file__ ) )
with open( path.join( here, 'README.rst' ), 'r' ) as f :
    readme = f.read( )

dependency_links = [
]

setup(
        name='twistyRL',
        version='0.1.07',
        url='https://github.com/python-study-ko/twistyRL',
        license='MIT License',
        description='twisty cube game for ML',
        long_description=readme,
        author='wesky93',
        author_email='wesky93@gmail.com',
        packages=[ "twistyRL" ],
        include_package_data=True,
        install_requires=install_requires,
        setup_requires=setup_requires,
        dependency_links=dependency_links,
        keywords=[ 'cube', 'rubiks', 'twistycube', 'ML', 'RL' ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
        ]

)
