# Usage
```
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

