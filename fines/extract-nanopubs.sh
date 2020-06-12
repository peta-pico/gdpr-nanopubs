#!/usr/bin/env bash

np op build -c http://c1.nl -c http://c2.nl -d http://d.nl prefixes.ttl -o nanopubs.trig GDPRfines_clean_mod.jsonld
np mktrusty nanopubs.trig
np check trusty.nanopubs.trig
