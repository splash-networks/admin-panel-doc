To set up a portal for Unifi first you need to [create a template](../defining-templates.md). Then you have to add the Unifi controller which will be using that portal. A single template can be applied to multiple sites.

## Add a Unifi Controller

To add a Unifi Controller you will click on the New unifi controller button in the Unifi Controllers tab. An interactive wizard will launch. You need to enter the name, URL and username password for the Unifi Controller. It needs to be a local user without 2FA. The controller should be reachable directly over the internet using the provided hostname, not via ui.com portal.

![Unifi Wizard 1](../assets/images/portals/unifi/unifi-wizard-1.png)

In the 2nd step the connection with the Unifi controller will be tested. If the connection is successful, you will get an option to assign sites on the Unifi controller to corresponding venues and templates on Splash Air. You can use the `+` button at the bottom to add multiple sites.

![Unifi Wizard 2](../assets/images/portals/unifi/unifi-wizard-2.png)

The 3rd and final step applies the settings for captive portal to the respective site on the Unifi controller. Click on the Create button to complete the process.

![Unifi Wizard 3](../assets/images/portals/unifi/unifi-wizard-3.png)

Completing this process sets up the captive portal for the selected site(s) on Splash Air.

The controller will start showing on the Unifi Controllers page:

![Controller Added](../assets/images/portals/unifi/controller-added.png)

You should check the site in the Unifi Controller to double-check the captive portal settings. In Hotspot > Authentication `External Portal Server` should be selected. 

![Unifi External Portal Server](../assets/images/portals/unifi/unifi-external-portal-server.png)

By clicking on Edit you can view the IP address: it should show the IP address of the Splash Air server.

![Unifi Portal Server IP](../assets/images/portals/unifi/unifi-portal-server-ip.png)

In the Settings tab the Landing Page Settings should be like this:

![Unifi Landing Page Settings](../assets/images/portals/unifi/unifi-landing-page.png)

```
Show Landing Page: checked
HTTPs Redirection Support: unchecked
Encrypted URL: unchecked
Secure Portal: checked
Domain: checked

Domain: <Splash Air Domain>
```

If using `Payment` Flow you need to add [walled garden](walled-garden.md) entries for your payment gateway such as Stripe in Pre-Authorization Allowances section.

<figure markdown="1">
![Unifi Portals](../assets/images/portals/unifi/walled-garden.png)
</figure>

## Portals

You can go to Portals to view the settings for the portal(s) just added.

![Unifi Portals](../assets/images/portals/unifi/unifi-portals.png)

Clicking on a portal takes you to the details for that portal. It lets you specify additional settings:

```
Redirect URL: the URL a user is redirected to after successful portal authorization
Business Name: name of the venue which will be displayed on top of the portal
Duration: the time in minutes for which a user is authorized on the network
Expiry: the time in days after which a repeat user will have to enter their data again on the portal
```

You can click on the Edit button against each entry to modify it if needed.

![Unifi Portal Details](../assets/images/portals/unifi/unifi-portal-details.png)

## Troubleshooting

To troubleshoot problems it is important to understand the components involved in the captive portal user authorization process and the interactions between them.

### Traffic Flow

Here is the traffic flow in the case of Ubiquiti Unifi:

![Unifi Traffic Flow](../assets/images/portals/unifi/unifi-traffic-flow.png)

### Client Isolation

The client isolation setting on Unifi controller has been known to lead to this error when trying to access the captive portal:

```
Hotspot login cannot open the page because the network connection was lost
```

<figure markdown="1">
![Unifi Traffic Flow](../assets/images/portals/unifi/unifi-client-isolation.png)
</figure>

To prevent it disable client device isolation in WiFi settings.

![Unifi Traffic Flow](../assets/images/portals/unifi/unifi-client-isolation-2.png)