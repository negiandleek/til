# !/bin/bash
directory="/home/pi/workspace/my-first-shell/itunes"
mkdir -p $directory
date=`date +'%Y%m%d%H%M'`
filename="${directory}/${date}.xml"
curl -s -o $filename https://itunes.apple.com/jp/rss/topsongs/limit=10/xml
