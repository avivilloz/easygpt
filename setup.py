from setuptools import setup, find_packages

setup(
    name="g4f_wrapper",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "retry",
        "g4f",
        "curl_cffi",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "A robust GPT interface with multiple providers, automatic cycling, "
        "and error handling for reliable AI-powered text generation."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/g4f_wrapper",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
