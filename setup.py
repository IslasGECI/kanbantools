from setuptools import setup, find_packages

setup(
    name="kanban_tools",
    version="0.1.0",
    packages=["kanban_tools"],
    author="Ciencia de Datos • GECI",
    install_requires=[
        "numpy",
        "pandas",
    ],
    python_requires=">=3",
)
