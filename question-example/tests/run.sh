#!/bin/bash
mkdir -p /grade/results
mkdir -p /grade/student
cd /grade/tests
python3 grade.py > /grade/results/results.json