Some vendors require the use of RADIUS in their captive portal authorization flows (e.g. HPE/Aruba Instant On). These instructions can be used to set up a RADIUS server using FreeRADIUS.

### FreeRADIUS Setup

Install FreeRADIUS:

```bash { .copy }
apt-get install freeradius freeradius-mysql freeradius-utils
```

Allow all NAS clients to connect to it:

```bash { .copy }
nano /etc/freeradius/3.0/clients.conf
```

Add the following lines at the end (replace `testing123` with a more secure secret):

```bash { .copy }
client all {
       ipaddr          = 0.0.0.0/0
       secret          = testing123
}
```

Authenticate all users without checking username/password:

```bash { .copy }
nano /etc/freeradius/3.0/users
```

Add the following on top:

```bash { .copy }
DEFAULT Auth-Type := Accept
```

Restart FreeRADIUS service:

```bash { .copy }
systemctl restart freeradius.service
```

