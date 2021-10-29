import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='okkular_ml',
    version='0.0.1',
    author='Okkular',
    author_email='vahuja@okkular.io',
    description="A package to host all code pertaining to okkular's machine learning/deep learning pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://www.okkular.io/',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues",
        "Company URL": "https://www.okkular.io/"
    },
    license='MIT',
    packages=['okkular_ml'],
    install_requires=[	"setuptools>=42","wheel","boto3","fastai==2.5.1"],
)