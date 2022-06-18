#!/usr/bin/env bash

# get dest from env files
WEBPROP="env/web.prop"
if test -f "$WEBPROP"; then
  DEST=$(grep "^DEST" $WEBPROP | cut -d "=" -f2 | sed 's/"//g')
else
  echo "${WEBPROP} does not exist; run setup.sh ?"
fi

# move files
# compile typescript to js
WEBAPP=webapp
cp ${WEBAPP}/index.py $DEST
chmod 755 $DEST/*.py
tsc ${WEBAPP}/app.ts --outFile apps/app.js
cp ${WEBAPP}/app.js $DEST

TEAMSNAPPROP="env/teamsnap.prop"
if test -f "$TEAMSNAPPROP"; then
  cp $TEAMSNAPPROP $DEST
else
  echo "${TEAMSNAPPROP} does not exist; run setup.sh ?"
fi
