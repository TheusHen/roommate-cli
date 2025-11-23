from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="roommate-cli",
    version="1.0.0",
    author="I'm Matheus",
    author_email="theushen@example.com",
    description="Your Personal AI Roommate - A beautiful CLI for chatting with your AI companion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheusHen/roommate-cli",
    project_urls={
        "Bug Tracker": "https://github.com/TheusHen/roommate-cli/issues",
        "Source Code": "https://github.com/TheusHen/roommate-cli",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    py_modules=["main"],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "roommate=main:main",
        ],
    },
    keywords="ai chat cli terminal roommate chatbot assistant",
)
