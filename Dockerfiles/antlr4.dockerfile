# Use the official openjdk image as the base
FROM openjdk:11-jdk

# Define a build argument. We want this to fail if not specified
ARG ANTLR_VERSION=

# Install Python runtime and ANTLR4
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    pip install antlr4-python3-runtime && \
    curl -O https://www.antlr.org/download/antlr-$ANTLR_VERSION-complete.jar

# Set the environment variables
ENV CLASSPATH=".:/antlr-$ANTLR_VERSION-complete.jar:$CLASSPATH"
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:$PATH"

# Set the working directory
WORKDIR /app

# Start a shell by default
CMD ["/bin/bash"]
