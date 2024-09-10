from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gpt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "A robust GPT interface with multiple providers, automatic cycling, "
        "and error handling for reliable AI-powered text generation."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/gpt",
)
