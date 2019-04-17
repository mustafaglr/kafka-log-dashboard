#!/bin/bash

python -u ./LogCreator.py &

python ./producer.py &

python ./consumer.py
