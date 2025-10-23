# This base image is chosen because it has all of the basic requirements preinstalled, 
# such as python, CUDA, CUDnn and should be GPU enabled by default.
# Several tensorflow/tensorflow images are broken by default and either require significant rework to become functional, 
# or are incompatible with Windows.

# ARG VARIANT=2.16.1-gpu

# FROM tensorflow/tensorflow:${VARIANT}
FROM tensorflow/tensorflow:2.16.1-gpu

# Filter out informational log messages from TensorFlow
# ENV TF_CPP_MIN_LOG_LEVEL=0
ENV TF_CPP_MIN_LOG_LEVEL=1

# Update environment variable
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:${LD_LIBRARY_PATH}"

RUN \
    --mount=type=cache,target=/var/cache/apt \
    # Now, run the update and install packages.
    apt-get update && apt-get install -y --no-install-recommends \
        # For monitoring system resources
        htop \              
        # For downloading files
        wget \              
        # For secure communications
        ca-certificates \   
        # Add sudo for user privilege escalation if needed inside the container
        # For privilege escalation
        sudo \              
        # For managing keys
        curl \              
        # For version control and collaboration
        git \               
        # For extracting zip files
        unzip \             
        # For file editing
        vim \
        # 
        gnupg2 \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY \
    .devcontainer/requirements.txt \
    /tmp/requirements.txt

RUN \
    python3 -m pip install --upgrade pip setuptools \
    && \
    python3 -m pip install -v \
        --no-cache-dir -r /tmp/requirements.txt \
    && \
    rm /tmp/requirements.txt

# Install gcloud CLI (example for Debian/Ubuntu)
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates gnupg curl sudo \
    && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt-get update && apt-get install -y google-cloud-cli \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a non-root user and switch to it
# RUN \
#     useradd -m -s /bin/bash -u 1000 user \
#     && \
#     echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the new user.
# USER user

# Change the working directory to /home/user.
# WORKDIR /home/user

# Define the entry point for the container.
# ENTRYPOINT ["/bin/bash"]