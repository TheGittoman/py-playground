from setuptools import setup

setup(
    name="Playground-project",
    version="1.0.0",
    packages=["src"],
    install_requires=[
        "numpy>=1.18.1",
        "pandas>=1.0.3",
    ],
    entry_points={
        'console_scripts': ['galai-generate=src.main:main']
    },
    author="Tomi Vartiainen",
    author_email="your_name@example.com",
    description="Playground for practising python programming",
    license="MIT",
)
