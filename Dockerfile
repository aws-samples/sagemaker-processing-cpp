FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y install build-essential libatlas-dev git wget curl nginx jq libatlas3-base

RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -bfp /miniconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda3/bin:${PATH}

RUN conda update -y conda && \
    conda install -c conda-forge pyarrow=0.14.1 && \
    conda install -c mlio -c conda-forge mlio-py=0.1 && \
    conda install -c anaconda scipy

# Python won’t try to write .pyc or .pyo files on the import of source modules
# Force stdin, stdout and stderr to be totally unbuffered. Good for logging
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN pip install --no-cache -I scikit-learn==0.20.0 pandas==1.0.3 boto3 sagemaker retrying
ADD process_script.py /
ADD a.out /
