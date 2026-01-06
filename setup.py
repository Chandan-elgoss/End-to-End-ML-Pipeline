from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Package metadata
PACKAGE_NAME = "End-to-End-ML-Pipeline"
VERSION = "0.1.0"
AUTHOR = "Chandan-elgoss"
AUTHOR_EMAIL = "chandan.kumar@elgoss.com"
DESCRIPTION = "A comprehensive end-to-end machine learning pipeline"
URL = f"https://github.com/{AUTHOR}/{PACKAGE_NAME}"
SRC_REPO = "mlProject"


PYTHON_REQUIRES = ">=3.8"

# Dependencies
INSTALL_REQUIRES = [
    "pandas>=1.3.0",
    "numpy>=1.21.0",
    "scikit-learn>=1.0.0",
    "matplotlib>=3.4.0",
    "seaborn>=0.11.0",
]

EXTRAS_REQUIRE = {
    "dev": ["pytest>=6.0", "black>=21.0"],
}

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name=SRC_REPO,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    projects_urls={
        "Bug Tracker": URL/"issues",
        },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=CLASSIFIERS,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)