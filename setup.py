from setuptools import setup, find_packages

setup(
    name="rosmaster_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pyserial"],
    author="Daojie PENG",
    description="A library for Rosmaster control",
    url="https://github.com/DaojiePENG/rosmaster_lib",  # 可选
)