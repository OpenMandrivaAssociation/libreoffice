#!/bin/sh
curl -s -L https://dev-builds.libreoffice.org/pre-releases/src/ 2>/dev/null |grep -E 'libreoffice-[0-9]' |cut -d'>' -f3- |cut -d_ -f2- |sed -e 's,.*libreoffice-,,;s,\.tar.*,,' |grep -v -- '<' |sort -V |tail -n1
