import setuptools

setuptools.setup(
    name='git42',
    version='2021.1.31',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/git42']
)
