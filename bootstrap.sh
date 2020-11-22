#!/bin/bash
HOST="0.0.0.0:8080"
ASGI="server.app:app"

exec uvicorn server.app:app --host 0.0.0.0
