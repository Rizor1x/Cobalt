from setuptools import setup, find_packages

setup(
    name="crest-lang",
    version="0.3.0",
    description="Crest Programming Language Compiler",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "crest=src.cli:main"
        ]
    },
    install_requires=[
        "lark>=1.1.0"
    ]
)