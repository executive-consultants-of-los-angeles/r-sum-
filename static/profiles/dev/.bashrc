#!/bin/bash
alias gp='git push origin $(git rev-parse --abbrev-ref HEAD); git push heroku $(git rev-parse --abbrev-ref HEAD):master'
