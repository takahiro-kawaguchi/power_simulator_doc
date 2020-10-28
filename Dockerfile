FROM squidfunk/mkdocs-material
RUN echo "now building..."
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install python-markdown-math