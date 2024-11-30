# Luotettava UDP-kommunikointi virtuaalisoketilla
Tässä projektissa toteutetaan luotettavan tiedonsiirron menetelmiä UDP-protokollan päällä käyttäen virtuaalisokettia. Virtuaalisoketti toimii välikerroksena sovelluksen ja UDP-soketin välillä, mahdollistaen virheiden simuloinnin sekä mukautetut luotettavuusprotokollat. Projekti sisältää asiakas- ja palvelinsovellukset sekä erilaisia luotettavuusprotokollan versioita, jotka käsittelevät pakettien häviämisen, viiveen ja yksittäiset bittivirheet.
## Yleiskuvaus
### Asiakaspuoli (client.py)
Toiminnot:
Lähettää viestin palvelimelle.
Odottaa kuittausta (ACK/NACK) palvelimelta.
Käyttää aikakatkaisua havaittujen pakettihäiriöiden käsittelyyn ja uudelleenlähetyksiin.
Tukee yksinkertaista virheentunnistusta pariteetilla.
Erikoisominaisuudet:
Tukee satunnaisia pakettihäviöitä ja viiveitä palvelimen simuloimien virheiden vuoksi.
### Palvelinpuoli (server.py)
Toiminnot:
Vastaanottaa asiakkaan lähettämän viestin.
Tarkistaa viestin eheyden (pariteetti tai muu menetelmä).
Lähettää kuittauksen:
ACK: Jos viesti on vastaanotettu oikein.
NACK: Jos viestissä havaitaan virhe.
Tukee satunnaisten bittivirheiden simulointia.

