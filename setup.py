from setuptools import find_packages, setup

setup(
        name='fib-prusty',
        version="0.0.1",
        author="sshu2017",
        author_email="sshu2017@yahoo.com",
        description="Calculates a Fibonacci number",
        long_description="blah blah blah blah",
        long_description_content_type="text/markdown",
        url="https://github.com/sshu2017/fib-prusty.git",
        install_requires=[],
        packages=find_packages(exclude=("tests",)),
        classifiers=[
            "Development Status::4-Beta",
            "Programming Language::Python::3",
            "Operating System::OS Independent",
            ],
        python_requires=">=3",
        tests_requires=["pytest"],
        )

