#!/bin/bash

# DİKKAT bu script ./ssi-turkiye-docs/docker/new-node dizininden cagirilmali

set -e

echo "initialising new node"

. "./.env"

NEW_NODE_SEED="29292929292929292929292929292929"
LEDGER_VOLUME="publicnet_newnode_node_data"

docker build -f ../Dockerfile.von -t ssi-turkiye/von .

sudo mkdir -p /opt/ssi-turkiye/publicnet
sudo mkdir -p /var/tmp/ssi-turkiye
sudo chown -R "$USER":"$USER" /opt/ssi-turkiye
sudo chown -R "$USER":"$USER" /var/tmp/ssi-turkiye

docker volume create $LEDGER_VOLUME

docker run --rm -it \
    -v "$PWD":/new-node \
    -v "$LEDGER_VOLUME":"/home/indy/ledger" \
    -v "/opt/ssi-turkiye/publicnet":"/opt/ssi-turkiye/publicnet" \
    --user=root \
    ssi-turkiye/von \
    bash -c "
    init_indy_keys --seed $NEW_NODE_SEED --name $NODE_NAME | tee /opt/ssi-turkiye/publicnet/newnode_node_keys.txt;

    cp /new-node/domain_transactions_genesis /home/indy/ledger/ssi-turkiye-publicnet;
    cp /new-node/pool_transactions_genesis /home/indy/ledger/ssi-turkiye-publicnet;
    "

