import setuptools



setuptools.setup(
    name="tituemg",
    version="0.0.1.3",
    author="Tomas Tubino",
    author_email="titubino@miuandes.cl.com",
    description="Heramioentas utiles para el proceso de EMG",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tistu37/tituemg",
    install_requires=['scipy', 'numpy'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
