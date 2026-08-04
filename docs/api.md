## API Key Creation

To access customer data via API the first step is to create an API Key.

Go to Admin > Generate API Key and press the Generate button.

![Generate API Key](assets/images/customer-data/api/api-key-generate.png)

Copy the generated API Key as it will only be displayed once.

You can use the same page to delete an existing key and create a new one if needed.

## API Docs

<style>
  :root {
    --scalar-custom-header-height: 60px; /* match Material's actual header height */
  }
</style>
<script id="api-reference"
  data-url="/files/api.json"
  data-configuration='{
    "layout": "modern",
    "showSidebar": true,
    "hideModels": false,
    "hideDownloadButton": true,
    "hideSearch": true,
    "hideDarkModeToggle": false,
    "darkMode": false,
    "authentication": {
      "preferredSecurityScheme": "ApiKeyAuth",
      "securitySchemes": {
        "ApiKeyAuth": {
          "name": "X-API-Key",
          "in": "header",
          "value": ""
        }
      }
    },
    "hiddenClients": "true",
    "agent": {
      "disabled": true
    },
    "customCss": ".scalar-app { --scalar-color-accent: #2563eb; }"
  }'>
</script>
<script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>