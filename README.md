# pipe-config-logging

Simple example of using great looking rich logging in an application's console, as well as in the log files itself.

## Usage

### Docker

On Linux, assuming you have Docker installed and configured properly, you can do the following in a Terminal:

```bash
# Change working directory to within the repo, if you haven't already
cd pipe-config-logging/

# Make the Bash scripts for building the Docker image and deploying the Docker container executable
chmod u+x build.sh
chmod u+x deploy.sh

# Build the Docker container
bash build.sh

# Deploy/run the Docker container
bash deploy.sh
```

The Docker container will run and produce a log into the `app/logs` directory, and a JSON output into the `app/dump` directory.

### Without Docker

If you just want to run the code, without using the Docker container, you can do the following:

```bash
# Change working directory to the app/ directory in the repo
cd pipe-config-logging/app

# Run the code
python endpoint.py
```

> Ensure you have the required packages installed (`requirements.txt`), otherwise the code will not run and throw an error.