# rscu - Raspberry Shake Charting Utility

written and contributed by David Fowler

## About

rscu (pronounced "rascue") is a GUI-based charting utility built to make custom plotting of [Raspberry Shake](https://raspberryshake.org) data easier.

## Installation

### via Anaconda/Miniconda (recommended)

Download and install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
1. In a Terminal (Mac OS or Linux) or Anaconda Prompt (Windows), tell conda to update itself:

    ```
    conda update conda -y
    ```

1. Next, tell conda to create an environment with the proper requirements, and activate it:

    ```
    conda create --name rscu obspy
    conda activate rscu
    ```

1. Now, install rscu directly from github (you may need [git](https://git-scm.com/) for this):

    ```
    pip install git+https://github.com/raspishake/rscu
    ```

1. You're ready to run rscu!

    ```
    rscu
    ```

### on Debian Linux without Anaconda

1. Install requirements via apt and pip

    ```
    sudo apt install python3-numpy python3-lxml python3-pip
    pip install obspy
    ```

1. Now, install rscu directly from github (you may need [git](https://git-scm.com/) for this):

    ```
    pip install git+https://github.com/raspishake/rscu
    ```

1. You're ready to run rscu!

    ```
    rscu
    ```
