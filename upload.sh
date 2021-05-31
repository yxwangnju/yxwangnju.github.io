#!/bin/bash

pelican content

git add -u 
git commit -m "."
git push origin notebook_source:notebook_source

ghp-import -m "Generate Pelican site" --no-jekyll -b main output -c audreyw.top

git push origin main:main

