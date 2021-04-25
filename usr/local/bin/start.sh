#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/Downloads/my-key.json"
chmod 777 /usr/local/bin/share/captures
python3 usr/local/bin/pytest.py