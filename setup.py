from setuptools import setup, find_packages

if "__main__" == __name__:
    try:
        setup(
            name="pyrust",
            packages=find_packages(),
            install_requires=['maturin'],
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
