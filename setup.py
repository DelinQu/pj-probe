from setuptools import setup, find_packages
import os

requirements = [
    'colorama',
]

init_fn = os.path.join(os.path.dirname(__file__), 'pjprobe', '__init__.py')
with open(init_fn) as f:
    for l in f.readlines():
        if '__version__' in l:
            exec(l)
            break

setup(
    name='pjprobe',
    version=__version__,
    install_requires=requirements,
    python_requires='>=3.7',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pjprobe = pjprobe.pjprobe:main',
        ]
    },
)