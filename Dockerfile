FROM python:3.7.4
WORKDIR /app
ADD . /app

# Install any necessary dependencies
RUN pip3 install --upgrade setuptools pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Open port 5000 for serving the web page
EXPOSE 5000
# These two properties for ENVIRONMENT selection to automatically pass through CI
ARG NAME
ENV ENV=${NAME:-NOT_DEFINED}
# Run app.py Flask app, when the container launches
CMD ["python3", "app.py", "${ENV}"]