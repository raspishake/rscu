import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="rscu",
    version="0.0.1",
    author="David Fowler",
    author_email="dfshake@highriskadventures.com",
    license='GPLv3',
    description="Simplifying charting of Raspberry Shake seismograph data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raspishake/rscu",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['obspy'],
    entry_points = {
        'console_scripts': [
            'rscu=rscu.rscu:vp_start_gui',
            ],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Framework :: Matplotlib",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
    ],
)