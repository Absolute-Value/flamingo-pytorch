from setuptools import setup, find_packages

setup(
  name = 'flamingo-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.8',
  license='MIT',
  description = 'Flamingo - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/flamingo-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'visual question answering'
  ],
  install_requires=[
    'einops>=0.4',
    'einops-exts',
    'torch>=1.6',
    'vit-pytorch'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
