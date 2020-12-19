from setuptools import setup

setup(
    name='python-amazon-sp-api',
    version='0.0.1',
    install_requires=[
        "requests",
        "six~=1.15.0",
        "boto3~=1.16.39",
        "cachetools~=4.2.0",
        "pycryptodome"
    ],
    packages=['tests', 'tests.api', 'tests.api.orders', 'tests.api.sellers', 'tests.api.finances',
              'tests.api.product_fees', 'tests.api.notifications', 'tests.client', 'sp_api', 'sp_api.api',
              'sp_api.api.orders', 'sp_api.api.orders.models', 'sp_api.api.sellers', 'sp_api.api.sellers.models',
              'sp_api.api.finances', 'sp_api.api.finances.models', 'sp_api.api.product_fees',
              'sp_api.api.notifications', 'sp_api.api.notifications.models', 'sp_api.auth', 'sp_api.base'],
    url='',
    license='mit',
    author='Michael Primke',
    author_email='info@saleweaver.com',
    description='python wrapper for amazon selling partner api'
)