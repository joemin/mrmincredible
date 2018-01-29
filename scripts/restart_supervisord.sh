#!/bin/sh

sudo /home/ec2-user/mrmincredible/venv/bin/supervisorctl reread
sudo /home/ec2-user/mrmincredible/venv/bin/supervisorctl update
sudo /home/ec2-user/mrmincredible/venv/bin/supervisorctl restart mrmincredible_flask_app
