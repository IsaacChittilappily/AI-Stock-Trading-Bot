from setuptools import setup, find_packages

setup(
    name="ai_stock_trading_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'scikit-learn',
        'pandas',
        'requests',
        'python-dotenv',
        'alpaca-trade-api',
        'flask'
    ],
    author="Isaac Chittilappily",
    author_email="chittilappilyisaac@gmail.com",
    description="An AI-powered stock trading bot using neural networks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IsaacChittilappily/ai_stock_trading_bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
