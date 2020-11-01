PORT = 3306

# name -> secret (32 hex chars)
USERS = {
    "tg":  "893d8335eb98014543fdaba68a56cb5c"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www-cdn.whatsapp.net"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "df6fff91c50a321843ed1d43c0e6ded7"
330
