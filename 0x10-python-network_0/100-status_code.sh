#!/bin/bash
#Black hole
curl -so /dev/null -w "%{http_code}" "$1"
