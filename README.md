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

Using `.env`:
```
cat <<'EOF' > .env
HETZNER_DNS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PMDD_ZONE_ID=xxxxxxxxxxxxxxxxxxxxxx
PMDD_NAME=home
EOF
```

Overriding the URL to get ip v4:
```
export PMDD_IP_URL=https://ip.hetzner.com
```


# Bash Completion
```
d=${XDG_DATA_HOME:-$HOME/.local/share}/bash-completion
f=$d/pmdd-complete.bash
echo $f
mkdir -p $d
_PMDD_COMPLETE=bash_source pmdd > $f
source $f
```

See
https://click.palletsprojects.com/en/8.1.x/shell-completion/#enabling-completion
for more shells.


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
