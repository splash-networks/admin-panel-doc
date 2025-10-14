To allow access to various services before captive portal authorization is complete you need to add these walled garden entries:

### Stripe

Stripe is a payment gateway used in `Payment` Flow type. White-list these domains for Stripe access:

```
api.stripe.com
checkout.stripe.com
files.stripe.com
js.stripe.com
m.stripe.com
m.stripe.network
q.stripe.com
```