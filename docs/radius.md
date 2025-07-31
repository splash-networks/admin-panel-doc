Some vendors require the use of RADIUS in their captive portal authorization flows (e.g. HPE/Aruba Instant On). These instructions can be used to set up a RADIUS server using FreeRADIUS.

### FreeRADIUS Setup

Install FreeRADIUS:

```
apt-get install freeradius freeradius-mysql freeradius-utils
```

Allow all NAS clients to connect to it:

```
nano /etc/freeradius/3.0/clients.conf
```

Add the following lines at the end (replace `testing123` with a more secure secret):

```
client all {
       ipaddr          = 0.0.0.0/0
       secret          = testing123
}
```

Authenticate all users without checking username/password:

```
nano /etc/freeradius/3.0/users
```

Add the following on top:

```
DEFAULT Auth-Type := Accept
```

Restart FreeRADIUS service:

```
systemctl restart freeradius.service
```

