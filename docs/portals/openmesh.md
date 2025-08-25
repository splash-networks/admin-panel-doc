To set up a portal for Open Mesh first you need to [create a template](../defining-templates.md).

## Add a Portal

To create a portal go to the Portal tab and click on the New portal button. Enter a name for the portal and specify the business and venue. In Hardware select `Coova Chilli`. Enter a secret which will be used to secure communication between the router/AP and Splash Air server. Then, enter a Site ID based on which the path of the portal URL will be defined.

![Coova Portal](../assets/images/portals/coova/coova-portal-url.png)

The `Guest Portal URL` will be created based on the URL of the Splash Air application followed by the path given by Site ID. Note this URL as it will be required later.

Select the template and click on the Create button.

## Portal Settings

You can go to Portals to view the settings for the portal(s) just added.

Clicking on a portal takes you to the details for that portal. It lets you specify additional settings:

```
Business Name: name of the venue which will be displayed on top of the portal
Expiry: the time in days after which a repeat user will have to enter their data again on the portal
Redirect URL: the URL a user is redirected to after successful portal authorization
Duration (seconds) after email verification: when using "Link" type Flow it is the "Session-Timeout" a user will receive via RADIUS after successful email verification 
```

You can click on the Edit button against each entry to modify it if needed.

## Open Mesh Settings

Access CloudTrax web portal and select the SSID on which captive portal needs to be enabled in Configure > SSID #.

In **SSID name** set an SSID. Turn on the **Enable** option. Turn off **Authentication**. Under Captive Portal turn on **Splash page**.

![SSID](../assets/images/portals/openmesh/ssid.png)

In **Splash page type** select `Hosted remotely`. In **Splash page URL** enter the `Guest Portal URL` copied earlier. In **Splash page secret** enter the secret created earlier. In **Splash page authentication type** select `RADIUS`. In **Server address 1** and **Server secret** enter the IP address and secret of your RADIUS server (will be provided by Splash Networks' team).

![Splash Page settings](../assets/images/portals/openmesh/splash-page.png)

Keep the **Use MAC addr for password** option off. In **Client force timeout** select a session timeout value. Keep the remaining settings at their default values: **Block LAN access** and **Client isolation** should be on.

## Troubleshooting

To troubleshoot problems it is important to understand the components involved in the captive portal user authorization process and the interactions between them.

### Traffic Flow

For traffic flow refer to the traffic flow section of Coova Chilli [here](coova-chilli.md/#traffic-flow).

### Pre Auth

Open Mesh devices perform a pre-auth process when a user comes online. It sends a RADIUS Access-Request with that user's MAC address as User-Name and empty User-Password (can be changed to MAC address by using the **Use MAC addr for password** toggle in Cloudtrax settings). If RADIUS accepts that request the user won't see the captive portal at all and would have internet directly. If you are using the RADIUS settings given [here](../radius.md) then add the following line at the top of `/etc/freeradius/3.0/users` file:

```text { .copy }
DEFAULT User-Password == "", Auth-Type := Reject
```

This will ensure that the portal always pops up for the client.

### SSH Access

To access Open Mesh AP via SSH go to Configure > Advanced and set a password in **Root password** field. Then AP can be accessed using username `root` and your configured password.

Open Mesh devices use a daemon called `udsplash` for captive portal. Here are some helpful commands:

Check online users

```text { .copy }
udsplash -l
```

Logout connected user

```text { .copy }
udsplash -n <ssid> -A <MAC address>
```

For example: `udsplash -n ssid4 -A 5A:0B:F7:02:A3:6E`