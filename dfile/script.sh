#!/bin/bash

python -u ./LogCreator.py &

python -u  ./producer.py &

python  ./consumer.py 


