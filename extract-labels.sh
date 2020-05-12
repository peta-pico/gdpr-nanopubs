#!/usr/bin/env bash

TPRED='<http://data.europa.eu/eli/ontology#title_alternative>'
LPRED='<http://www.w3.org/2000/01/rdf-schema#label>'

rapper -i turtle -o ntriples data/gdpr.ttl \
  | grep " $TPRED " \
  | sed "s| $TPRED | $LPRED |" \
  | less
#  > gdpr-labels.nt
