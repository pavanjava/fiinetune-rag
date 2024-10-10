from setuptools import setup, find_packages

setup(
    name='finetune-rag',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'flask',  # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'finetune-rag=finetunerag.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
