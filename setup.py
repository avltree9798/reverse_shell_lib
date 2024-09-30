from setuptools import setup, find_packages

setup(
    name='reverse_shell_lib',  # The name of the package
    version='0.1',  # Initial version
    packages=find_packages(),  # Automatically find packages in this directory
    description='A reverse shell library',  # Short description
    long_description=open('README.md').read(),  # README file for detailed description
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/avltree9798/reverse_shell_lib',  # URL of the project (if hosted)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],  # Add dependencies if any
)
