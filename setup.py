import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='GettMore',
      version='0.0.1',
      description='Improving simple language models and turning them to GPT',
      author='Shauray Singh',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['to be defined'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['numpy', 'requests', 'pillow'],
      python_requires='>=3.8',
      extras_require={
        'cuda': ["pycuda"],
        'testing': [
            "pytest",
            "torch~=1.11.0",
            "tqdm",
            "pre-commit",
        ],
      },
      include_package_data=True)
