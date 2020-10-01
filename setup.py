
import setuptools

setuptools.setup(
    name='APS-Games',
    version='0.0.1',
    description='Jogo de aventura simples baseado em texto',
    package=['APS-Games'],
    package_dir={'APS-Games': 'src'},
    package_data={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
