from setuptools import setup

setup(
    name="Playground-project",
    version="1.0.0",
    packages=["src"],
    install_requires=[
        "numpy>=1.18.1",
        "pandas>=1.0.3",
        "opencv>=4.6.0",
    ],
    entry_points={
        'console_scripts': ['my-command=src.main:main']
    },
    author="Tomi Vartiainen",
    author_email="your_name@example.com",
    description="Playground for practising python programming",
    license="MIT",
)
