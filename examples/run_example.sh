#!/bin/bash

pushd ../docker/new-node
docker build -f Dockerfile.von -t ssi-turkiye/von .
popd

docker run --rm -it -v "$PWD":/examples ssi-turkiye/von  python3 /examples/query_ledger.py