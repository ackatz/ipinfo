#!/bin/bash

# Run the uvicorn server and crontab
uvicorn app.main:app --host 0.0.0.0 --port 8080