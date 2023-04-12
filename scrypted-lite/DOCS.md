# Scrypted Lite Add-on for Home Assistant

For more information on Scrypted, please check out the [the Scrypted website](https://scrypted.app) or [the Scrypted GitHub page](https://github.com/koush/scrypted).

# Advanced: Environment variables
Environment variables may be set using the add-on configuration screen and are loaded as the add-on starts. Valid variables must begin with `SCRYPTED_`, for example:

```
- name: "SCRYPTED_DISABLE_AUTHENTICATION"
  value: "false"
- name: "SCRYPTED_ADMIN_TOKEN"
  value: "secret"
- name: "SCRYPTED_ADMIN_USERNAME"
  value: "hassioingress"
```

If set, `SCRYPTED_ADMIN_TOKEN` can be used by `ingress.conf` to automatically authenticate all requests that originate from Home Assistant. 