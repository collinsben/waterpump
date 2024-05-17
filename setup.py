import setuptools

setuptools.setup(
  name='python_template',
  version='0.0.0',
  author='Ben Collins',
  license='MIT',
  packages=setuptools.find_namespace_packages(),
  entry_points={
  },
  install_requires=[
    "adafruit-circuitpython-motorkit",
    "fastapi",
    "uvicorn[standard]",
    "rpi.gpio",
  ]
)