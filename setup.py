from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "PythonDemoPackage"
USER_NAME = "entbappy"
USER_EMAIL = "entbappy73@gmail.com"

setup(
    name=f"{PROJECT_NAME}",
    version="0.0.6",
    author="Bappy Ahmed",
    author_email=USER_EMAIL,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages= find_packages(where="src"),
    python_requires=">=3.7",

    install_requires=[
        "pandas",
        "PyYAML"
    ]
)