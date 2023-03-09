from distutils.core import setup

setup(
    name='opcua-sampleproject',
    version='1.0.0',
    description='A sample opcua project',
    url='https://github.com/Kefaku/opcua-example',
    install_requires=['opcua', 'jupyter', 'numpy', 'matplotlib', 'pyOpenSSL'],
)