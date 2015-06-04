from setuptools import setup, find_packages

setup(
    name="SplitQsub",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    scripts=['scripts/submit_qsub.sh'],
    entry_points={
        "console_scripts": [
            "splitqsub = splitqsub.__main__:main"
        ]
    },
    namespace_packages=["splitqsub"]
    )
