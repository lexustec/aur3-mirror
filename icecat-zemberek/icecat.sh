#!/bin/bash
  
  [ "${ICECATDIR}" = "" ] && export ICECATDIR="/usr/lib/icecat-3.0.1-g1"
# export LD_LIBRARY_PATH=${ICECATDIR}:${LD_LIBRARY_PATH}
  export MOZILLA_FIVE_HOME=${ICECATDIR}
# export MOZ_PLUGIN_PATH=${ICECATDIR}/plugins/:${MOZ_PLUGIN_PATH}
  export PATH=${PATH}:${ICECATDIR}
