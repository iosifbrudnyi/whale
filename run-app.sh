#!/bin/bash

set -e

exec poetry run yoyo apply migrations &
exec poetry run start