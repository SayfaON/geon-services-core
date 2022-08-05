import setuptools

desc = """\
=================
Geon Services Core
=================
Shared modules for QWC services.
"""

setuptools.setup(
    name="geon-services-core",
    version="1.0",
    author="Sourcepole AG",
    author_email="info@sourcepole.ch",
    description="Shared modules for QWC services",
    long_description=desc,
    long_description_content_type="text/x-rst",
    url="https://github.com/SayfaON/geon-services-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
