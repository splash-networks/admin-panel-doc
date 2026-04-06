To set up a portal for Cisco WLC first you need to [create a template](../defining-templates.md).

## Add a Portal

To create a portal go to the Portals tab and click on the New portal button. Enter a name for the portal and specify the business and venue. In Hardware select `Cisco WLC`. Then, enter a Site ID based on which the path of the portal URL will be defined.

![Create Portal](../assets/images/portals/cisco/portal.png)

The `Guest Portal URL` will be created based on the URL of the Splash Air application followed by the path given by Site ID. Note this URL as it will be required later.

Select the template and click on the Create button.

## Portal Settings

You can go to Portals to view the settings for the portal(s) just added.

Clicking on a portal takes you to the details for that portal. It lets you specify additional settings:

```
Business Name: name of the venue which will be displayed on top of the portal
Redirect URL: the URL a user is redirected to after successful portal authorization
Expiry: the time in days after which a repeat user will have to enter their data again on the portal
Duration (seconds) after email verification: when using "Link" type Flow it is the "Session-Timeout" a user will receive via RADIUS after successful email verification 
```

You can click on the Edit button against each entry to modify it if needed.

## Cisco WLC (AireOS) Settings

Access Cisco WLC using web interface and click on **Advanced**. Go to Security > AAA > RADIUS > Authentication and add a new RADIUS server. The IP address and RADIUS secret shared by Splash Networks' support team will be entered here.

![RADIUS](../assets/images/portals/cisco/radius.png)

Click on Apply to save the settings. Then go to Security > Access Control Lists > Access Control Lists (or FlexConnect ACLs if you're using FlexConnect) and create a new ACL. Click on the ACL name and add a new rule to it. Configure these settings:

```
Sequence: 1
Source: Any
Destination: IP Address
Protocol: Any
DSCP: Any
Action: Permit
```

In IP address enter the IP address of Splash Air server with Netmask `255.255.255.255`.

![ACL](../assets/images/portals/cisco/acl.png)

Similarly, add a new rule with Source equal to Splash Air IP address and Destination Any:

![ACL Summary](../assets/images/portals/cisco/acl-2.png)

Go to Security > Web Auth > Web Login Page. In **Web Authentication Type** select `External (Redirect to external server)`. In **Redirect URL after login** enter a redirect URL (optional). In **External Webauth URL** enter the Guest Portal URL copied earlier. Click on Apply to save settings.

![Web Auth](../assets/images/portals/cisco/web-login.png)

Next, go to WLANs and select the WLAN on which to apply guest portal. In Security > Layer 3 set **Layer 3 Security** to be `Web Policy`. Below it select the **Authentication** option. In **Preauthentication ACL** select the ACL created previously. Check **Over-ride Global Config** option. In Web Auth type select **External(Re-direct to external server)** and in URL enter the Guest Portal URL.

![Layer 3](../assets/images/portals/cisco/layer-3.png)

Then go to Security > AAA Servers and in Authentication servers check the **Enabled** button. In Server 1 add the RADIUS server created previously:

![AAA](../assets/images/portals/cisco/aaa.png)

Scroll down to **Authentication priority order for web-auth user**. Use the arrows to ensure only **RADIUS** is in the `Order Used for Authentication` section:

![RADIUS Order](../assets/images/portals/cisco/radius-order.png)

Click on Apply to save the settings.

Finally, go to Management > HTTP-HTTPS and configure these settings:

```
HTTP Access: Enabled
HTTPS Access: Enabled
WebAuth SecureWeb: Disabled
HTTPS Redirection: Disabled
```

![Management](../assets/images/portals/cisco/mgmt.png)

Click on Apply to save settings. WLC may need to be rebooted for these settings to take effect.

## Cisco C9800 (IOS-XE) Settings

Access Cisco WLC using web interface and go to Configuration > Security > Web Auth. In global profile Virtual IPv4 Address should be `192.0.2.2`.

![Webauth](../assets/images/portals/cisco/c9800-webauth.png)

Click on Add to create a new profile called **Splash** with these parameters:

 - **Maximum HTTP connections**: 200
 - **Init-State Timeout**: 3600
 - **Type**: `webauth`

Click on the Splash profile and in General tab use these settings:

 - **Banner Type**: None
 - **Turn-on Consent with Email**: Disabled
 - **Captive Bypass Portal**: Disabled
 - **Disable Success Window**: Enabled
 - **Disable Logout Window**: Enabled
 - **Sleeping Client Status**: Enabled
 - **Sleeping Client Timeout**: 720

In Advanced tab use these settings:

 - **Redirect URL for login**: Guest Portal URL created earlier
 - **Redirect On-Success**: redirect URL after successful portal authorization
 - **Redirect On-Failure**: Guest Portal URL created earlier
 - **Redirect Append for AP MAC Address**: `ap_mac`
 - **Redirect Append for Client MAC Address**: `client_mac`
 - **Portal IPV4 Address**: IP address of your Splash Air server

![Webauth](../assets/images/portals/cisco/c9800-webauth-2.png)

After that go to Configuration > Security > AAA > Servers/Groups and add a new RADIUS server. The IP address and RADIUS secret shared by Splash Networks' support team will be entered here.

Then, go to Server Groups tab and create a new Server group. The AAA server added earlier should be added to this group by moving it from Available Servers to Assigned Servers.

Then, go to AAA Method List and click on the default list. Move your server group from Available Server Groups to Assigned Server Groups.

Go to Configuration > Tags & Profiles > WLANs and create a new WLAN (or edit an existing WLAN). In Security > Layer 2 select **None**. In Security > Layer 3 use these settings:

 - **Web Policy**: Enabled
 - **Web Auth Parameter Map**: `Splash`
 - **Authentication List**: default
 - **On Mac Filter Failure**: Disabled
 - **Splash Web Redirect**: Disabled

Go to Configuration > Security > URL Filters and add a new filter:

 - **List Name**: walledGarden
 - **Type**: PRE_AUTH
 - **Action**: PERMIT
 - **URLs**: your Splash Air domain

![Walled Garden](../assets/images/portals/cisco/c9800-walled-garden.png)

Then, go to Configuration > Tags & Profiles > Policy and add a new policy. On general tab, enter a name for it. **Status** should be `Enabled`. On the Access Policies tab:

 - **URL Filters**: walledGarden

On Advanced tab:

 - **Allow AAA Override**: checked

After that go to Configuration > Tags & Profiles > Tags and add a new entry. Enter a name for it, and in WLAN-POLICY add a mapping for the WLAN Profile and Policy Profile created earlier:

![Tag](../assets/images/portals/cisco/c9800-tag.png)

Finally, go to Administration > Management > HTTP/HTTPS/Netconf/VTY and ensure these settings:

 - **HTTP Access**: Enabled
 - **HTTPS Access**: Enabled

### Credits

[Cloudi-Fi Cisco WLC 9800 Guide](https://help.cloudi-fi.com/hc/en-us/articles/9651117910941-How-to-enable-Cloudi-Fi-with-Cisco-WLC-9800-in-Local-Mode)

## Troubleshooting

To troubleshoot problems it is important to understand the components involved in the captive portal user authorization process and the interactions between them.

### Traffic Flow

Here is the traffic flow in the case of Cisco WLC:

![Traffic Flow](../assets/images/portals/cisco/traffic-flow.png)
