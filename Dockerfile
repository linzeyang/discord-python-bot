# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10.7-slim-bullseye

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -U pip && python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "bot.py"]
