from setuptools import setup, find_packages

with open('README.rst', 'r') as file:
    readme = file.read()
    
setup(
    name='discake',
    author='Carlos',
    url='https://github.com/lollipop-69/discake',
    version='0.0.1',
    license='MIT',
    description='A discord py support library containing utilities.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    install_requires=[
        'discord.py'
    ],
    project_urls={
        "Homepage": "https://github.com/lollipop-69/discake/"
    },
    packages=find_packages(),
    python_requires='>=3.8.0',
    keywords=['discord py', 'discord paginator', 'paginator', 'button paginator'],
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
