from setuptools import setup, find_packages
from pathlib import Path
from setuptools.command.install import install
from configparser import ConfigParser
import os



class PostInstallCommand(install):
    def run(self):
        install.run(self)
        config = ConfigParser()
        config.read("setup.cfg")
        
        config_dir = Path(os.path.expanduser(config.get("layman_terminal", "config_dir")))
        config_file = config_dir / config.get("layman_terminal", "config_file")
        
        # Create directory if needed
        config_dir.mkdir(mode=0o700, exist_ok=True)

        if not config_file.exists():
            default_config = ConfigParser()
            default_config["DEFAULT"] = {
                "api_key": "your_default_key_here",
                "llm":"gemini"
            }
            with open(config_file, "w") as f:
                default_config.write(f)
            config_file.chmod(0o600)  # Secure file permissions
            print(f"Created default config file: {config_file}")


setup(
    name="layman_terminal",
    version="0.1.0b1",
    packages=find_packages(),
    cmdclass={"install": PostInstallCommand},
    install_requires=[
        "python-dotenv",
        "pyyaml",
        "google-genai"
    ],
    entry_points={
        "console_scripts": [
            "lt=src.cli:main"
        ]
    },
    include_package_data=True,
    python_requires=">=3.9",
    author="Prashant Gavit",
    author_email="prashantgavit115@gmail.com",
    description="AI-powered terminal assistant",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prashantgavit/layman-terminal",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9+",
    ],
    keywords="ai terminal cli assistant",
    project_urls={
        "Bug Tracker": "https://github.com/prashantgavit/layman-terminal/issues",
    },


)