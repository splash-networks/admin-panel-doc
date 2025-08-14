To set up a portal for Huawei first you need to [create a template](../defining-templates.md).

## Add a Portal

To create a portal go to the Portals tab and click on the New portal button. Enter a name for the portal, and in Hardware select `Huawei`. Then, enter a Site ID based on which the path of the portal URL will be defined.

![Huawei Portal](../assets/images/portals/huawei/portal.png)

The `Guest Portal URL` will be created based on the URL of the Splash Air application followed by the path given by Site ID. Note this URL as it will be required later.

Select the venue and template and click on the Create button.

## Portal Settings

You can go to Portals to view the settings for the portal(s) just added.

Clicking on a portal takes you to the details for that portal. It lets you specify additional settings:

```
Business Name: name of the venue which will be displayed on top of the portal
Expiry (days): the time in days after which a repeat user will have to enter their data again on the portal
Redirect URL: the URL a user is redirected to after successful portal authorization
Duration (seconds) after email verification: when using "Link" type Flow it is the "Session-Timeout" a user will receive via RADIUS after successful email verification 
```

You can click on the Edit button against each entry to modify it if needed.

## Huawei FAT AP Settings

**Note:** _There are 2 captive portal modes supported on Huawei: **HTTP** and **HTTPS**. HTTP is simpler to set up but is less secure and will not work on iOS devices. The use of HTTPS is recommended as it is more secure and supported by all devices. The setup for HTTPS mode requires a few more steps so the procedure for setting it up is given at the end._

### HTTP Setup

Login to your Huawei FAT AP using its web interface. Go to Configuration > Internet Configuration and make sure Internet access mode is `Gateway` and NAT is On.

![Huawei Portal](../assets/images/portals/huawei/gateway.png)

Similarly, ensure that the LAN interface on which you want to enable portal is using DHCP from the AP.

Go to Advanced > Security > ACL > User ACL Settings. Create a new ACL and give it a number such as `6000` and a name such as `splash`. This ACL will be used for pre-authentication access, also known as walled garden. Enter a new rule in it to permit traffic for UDP destination port `53` to allow access to DNS servers.

![Huawei Walled Garden](../assets/images/portals/huawei/firewall-1.png)

Similarly, add another rule to permit access to the AP from LAN. In this example the AP LAN interface has the IP of `192.168.50.1`.

![Huawei Walled Garden](../assets/images/portals/huawei/firewall-3.png)

Then go to Advanced > Security > AAA and in Portal Server Global Configuration switch to External Portal tab. Check the **HTTP Protocol** option and in **HTTP interoperation mode** select `HTTP-based`. In **Local gateway address** select `All addresses`. Click Apply to save the settings.

![External Portal](../assets/images/portals/huawei/external-portal.png)

In **Portal Authentication Server List** click on the Create button. In **Server name** enter a name for the server. In Server IP enter the IP of Splash Air server and click on the `+` button to add it. In **Protocol type** select `HTTP/HTTPS`. In **URL** enter the `Guest Portal URL` obtained earlier.

![Portal Server](../assets/images/portals/huawei/portal-server.png)

Navigate down to URL Option Settings and set up the following options:

 - User IP address keyword: `userip`
 - User MAC keyword: `usermac`
 - Login URL keyword/Login URL: `url`. The value of the URL will be based on your LAN gateway IP. For gateway IP of `192.168.50.1` the value will be `http://192.168.50.1:8000`

![URL Options](../assets/images/portals/huawei/url-options.png)

(Optional) To set a redirect URL to which the user is redirected after successful portal login expand Parameter Parsing Configuration section. In **Login success response** select `Redirect to the specified URL`. Then, enter a URL to which the user should be redirected:

![Parameter Parsing](../assets/images/portals/huawei/parameter-parsing.png)

Click OK to save the settings.

Next, go to Advanced > Security > AAA > RADIUS tab and create a new RADIUS Server Profile. Enter the IP address and Secret (will be provided by Splash Networks' team) and check the **Authentication** option.

![RADIUS 1](../assets/images/portals/huawei/radius-1.png)

In **Profile default shared key** input the same RADIUS secret added earlier.

![RADIUS 2](../assets/images/portals/huawei/radius-2.png)

Click OK to save RADIUS profile. Then go to Advanced > HTTP Access tab. In **Access mode** select `HTTP` and in **Local gateway address** select `Any address`.

![Advanced](../assets/images/portals/huawei/advanced.png)

Click on Apply to save the settings.

Finally, go to Configuration > WLAN Configuration and create a new SSID (or select an existing SSID) to enable captive portal on it. In Step 1 enter a SSID and select the interface VLAN of LAN side (which should have DHCP configured).

<figure markdown="span">
  ![WLAN 1](../assets/images/portals/huawei/wlan-1.png){ width="80%" }
</figure>


Click Next to go to the second step. In **Security settings** select `Portal`. In **Portal server** select `External Portal server`. Uncheck **MAC address-prioritized** option. In External Portal Server Configuration select the server template that you created earlier. Similarly, in External RADIUS Server Configuration select the RADIUS template that you created earlier.

![WLAN 2](../assets/images/portals/huawei/wlan-2.png)

In Authentication-free Rule select Control mode `ACL`. In **ACL number** select the ACL that you created earlier.

<figure markdown="span">
  ![WLAN 2 ACL](../assets/images/portals/huawei/wlan-2-acl.png){ width="70%" }
</figure>

Click Next to go to the last step. In Step 3 keep the default settings and click Finish to save the settings.

### HTTPS Setup

To set up HTTPS you first need 2 things:

1. TLS certificate
2. DNS record pointing to your Huawei AP

#### TLS Certificate

In this example we have used Let's Encrypt to obtain a TLS certificate for free. The domain in our case is `huawei.splashnetworks.co` which is configured to point to the WAN IP of Huawei AP.

```
certbot certonly --manual --preferred-challenges dns --key-type rsa --rsa-key-size 2048 -d huawei.splashnetworks.co
```

It will generate a DNS challenge to verify domain ownership. After completing that it will produce 4 files:

1. `privkey.pem`
2. `cert.pem`
3. `chain.pem`
4. `fullchain.pem`

Huawei requires the private key to be password protected which it is currently not. Here's how to password protect it:

```
openssl rsa -aes256 -in privkey.pem -out privkey_encrypted.pem
```

It will ask for a password and then output `privkey_encrypted.pem` file.

Before uploading the certificate to AP we need to combine the private key and certificate in a single file. Create a consolidated file `combined.pem` like this:

```
cat privkey_encrypted.pem fullchain.pem > combined.pem
```

On Huawei AP go to Advanced > Security > Certificate Management and click on Upload Certificate. Enter a name for it, and in **Certificate type** select `Local+CA+Private key`. In **Certificate format** select `PEM`. Upload the `combined.pem` in **Certificate file** and provide its password.

<figure markdown="span">
  ![Upload Cert](../assets/images/portals/huawei/upload-cert.png){ width="70%" }
</figure>

Click OK to save. Then go to Advanced > Security > SSL and create a new SSL policy. In **SSL policy name** input a name for the policy. In **SSL policy type** select `Server`. In **Certificate name** select the certificate created in the previous step. Keep the remaining values at their default and click OK to save.

![SSL Policy](../assets/images/portals/huawei/ssl-policy.png)

Now you can apply this SSL policy to the AP so it doesn't show a certificate warning on web login. Access the AP using SSH and deploy the SSL policy created in the previous step using command-line:

```
[huawei-AP] http secure-server ssl-policy splash
```

#### HTTPS Configurations

Assuming HTTP configurations described above are already in place, a few modifications are required to switch from HTTP to HTTPS mode.

Go to Advanced > AAA > Portal Server Global Configuration and switch to External Portal tab. In HTTP Protocol section switch to `HTTPS-based` in **HTTP interoperation mode**. Select the SSL policy created above and in **Local gateway address** select `All addresses`. Port number will be `8443`. Click Apply to save the settings.

![External Portal HTTPS](../assets/images/portals/huawei/external-portal-https.png)

In Portal Authentication Server List click on the existing server to access its details. Expand **URL Option Settings** and update the `Login URL` based on your Huawei AP's hostname. If your AP has a hostname of `huawei.splashnetworks.co` then enter this URL:

```
https://huawei.splashnetworks.co:8443
```

It should appear like this:

![URL Options HTTPS](../assets/images/portals/huawei/url-options-https.png)

Click on OK to save the changes. Then go to Advanced > Security > ACL > Domain Name Configuration. Click on Create to add a domain which we will later reference in our ACL. Enter an ID and your domain like this:

<figure markdown="span">
  ![Domain Name](../assets/images/portals/huawei/domain-name.png){ width="70%" }
</figure>

Then go to User ACL Settings tab and add a new rule to your existing ACL to permit the domain created in the last step by adding it in **Dest domain name**:

![ACL Domain](../assets/images/portals/huawei/acl-domain.png)

HTTPS configuration is now complete. No change is required on Splash Air to support HTTPS mode.

## Troubleshooting

To troubleshoot problems it is important to understand the components involved in the captive portal user authorization process and the interactions between them.

### Traffic Flow

Here is the traffic flow in the case of Huawei:

![Huawei Traffic Flow](../assets/images/portals/huawei/traffic-flow.png)

### iOS Error

When using HTTP captive portal mode iOS devices will produce an error like this:

<figure markdown="span">
  ![iOS Error](../assets/images/portals/huawei/ios-error.png){ width="70%" }
</figure>

This is because HTTP mode is less secure and is therefore blocked on iOS. The solution is to switch to HTTPS mode.