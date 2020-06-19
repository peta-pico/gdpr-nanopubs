#!/usr/bin/env bash

np op build -c https://orcid.org/0000-0001-6882-6480 -c http://orcid.org/0000-0002-1267-0234 -d https://www.enforcementtracker.com/ prefixes.ttl -o nanopubs.trig data/GDPRfines_clean_mod.jsonld
np mktrusty nanopubs.trig
np check trusty.nanopubs.trig
