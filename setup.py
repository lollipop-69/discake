from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    readme = file.read()
    
setup(
    name='dpy-utils',
    author='Carlos',
    url='https://github.com/lollipop-69/dpy-utils',
    version='0.0.1,
    license='MIT',
    description='A discord py extension containing utitlities.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    install_requires=[
        'discord.py'
    ],
    project_urls={
        "Homepage": "https://github.com/lollipop-69/dpy-utils/"
    },
    packages=find_packages()
    python_requires='>=3.8.0',
    keywords=['discord py', 'discord paginator', 'paginator', 'button paginator']
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)
