PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "32b920dffb51643028e2f6b878d4eac1"
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
TLS_DOMAIN = "w1.web.whatsapp.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "aa6a74ce1e3b2acef42c6fe975cd13d9"
330
