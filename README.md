# Install
```
pip install git+https://github.com/felixhummel/poor-mans-dyndns.git@main
```


# Usage
First, [get a Hetzner DNS API access token][api-access-token].

[api-access-token]: https://docs.hetzner.com/dns-console/dns/general/api-access-token/
```
export HETZNER_DNS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
pmdd zones
pmdd set a-record --zone-id xxxxxxxxxxxxxxxxxxxxxx --name home
```

Using environment variables:
```
export PMDD_ZONE_ID=xxxxxxxxxxxxxxxxxxxxxx
export PMDD_NAME=home
pmdd set a-record
```


# cron
```
PMDD_ZONE_ID=xxxxxxxxxxxxxxxxxxxxxx PMDD_NAME=home pmdd update
```


# Alternatives
- https://pypi.org/project/hetzner-dns-tools/
- https://github.com/filiparag/hetzner_ddns



# Felix' Cheatsheet
```
export HETZNER_DNS_TOKEN=$(pass felix/hetzner/dns-token)
export PMDD_ZONE_ID=$(pass hacks/pmdd/test/zone-id)
export PMDD_NAME=$(pass hacks/pmdd/test/name)
make
```
