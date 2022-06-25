#!/bin/bash

docker build . -t yspeech/bierbot-rasa-actions

docker-compose up -d
