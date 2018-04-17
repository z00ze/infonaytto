# Infonäyttö
Infonäyttö palvelimella pyöritettäväksi. Sivu on jaettu kuuteen eri lohkoon ja jokainen niistä voi olla eri kehittäjän omalla palvelimella pyörivä sivusto. Lohkojen (blocks) päivitys rajapinnan ylitse helpottamaan ylläpitoa ja lohkojen vaihtoa.

<img src="Screenshot-1.png" width="600">

## Käyttäjä
Tietokannassa käyttäjä nimellä <b>admin</b> jonka salasana on <b>deleteME</b>

## Rajapinnat (JSON)

### POST /new
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "position": "1",
    "name": "google",
    "url": "http://www.google.com"
  }
```

### POST /update
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "position": "1",
    "name": "yahoo",
    "url": "http://www.yahoo.com"
  }
```
### POST /delete
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "uid": "93"
  }
```

### POST /newuser
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "name": "admin",
    "password": "deleteME"
  }
```

### POST /deleteuser
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "name": "admin",
  }
```

### POST /swap
Example request:
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  [0,1]
```
