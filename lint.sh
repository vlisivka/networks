#!/bin/bash
set -ue

panic() {
  echo "ERROR: $*" >&2
  exit 1
}

[ -x $(which panache) ] || panic "Install panache using command \"cargo install panache\"."

exec panache --flavor pandoc lint src
