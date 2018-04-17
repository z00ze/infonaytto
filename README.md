# Infonäyttö
Infonäyttö palvelimella pyöritettäväksi. Sivu on jaettu kuuteen eri lohkoon ja jokainen niistä voi olla eri kehittäjän omalla palvelimella pyörivä sivusto. Lohkojen (blocks) päivitys rajapinnan ylitse helpottamaan ylläpitoa ja lohkojen vaihtoa.

<img src="Screenshot-1.png" width="600">

## Asennus ja käyttö
Asenna:
Tarvittavat riippuvuudet.
Käyttö:
python infonaytto.py

## Käyttäjä
Tietokannassa käyttäjä nimellä <b>admin</b> jonka salasana on <b>deleteME</b>

## Rajapinnat (JSON)

### POST /new
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
Luo uuden lohkon, korvaa siinä paikassa olleen lohkon.

### POST /update
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
Päivittää kyseisessä paikassa olevan lohkon uusilla tiedoilla.

### POST /delete
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "uid": "93"
  }
```
Poistaa lohkon uniikin id:n mukaan.

### POST /newuser
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
Luo uuden käyttäjän.

### POST /deleteuser
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  {
    "name": "admin",
  }
```
Poistaa käyttäjän nimen perusteella.

### POST /swap
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json

Body
  [0,1]
```
Vaihtaa kahden lohkon paikkoja.

### POST /getAll
```
Headers
   Authorization: Basic YWRtaW46ZGVsZXRlTUU=
   Content-Type: application/json
```
RETURNS users and blocks tables from database. `[ [blocks], [users] ]`

## RESPONSES
SUCCESFULL
```
{
	"post": "successfull"
}
```
FAILED
```
{
	"post": "failed"
}
```
