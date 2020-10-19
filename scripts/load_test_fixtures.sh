#!/usr/bin/env bash
# Load a set of test fixture praise lists and praise

$(dirname "$0")/run_django_command.sh loaddata \
data_models/fixtures/beta_fixtures.json
  
