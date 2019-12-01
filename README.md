# IlmoBot
Discord botti Digit Ry:lle

IlmoBot on laitettu ulkoiselle serverille, jotta se olisi päällä vuorokauden ympäri.
IlmoBotin käyttöönotto Digit ry:n discord serverillä on vielä työn alla.

# Komennot

Kirjoittamalla ">ilmo" Discordserverin tekstikanavalle, IlmoBot hakee kaikki avoimet tapahtumat suoraan discordiisi. Komento kertoo tapahtuman nimen, viimeisen ilmoittautusmis ajan, sekä osallistujamäärät.

![ilmo](https://github.com/Akatixxc/IlmoBot/blob/master/images/Ilmo_ilmo.JPG)


Kirjoittamalla ">help" IlmoBot lähettää sinulle direct maililla tiedot kaikista komennoista, tekijän discordin, sekä Github linkin tähän repositoryyn.

![help](https://github.com/Akatixxc/IlmoBot/blob/master/images/Ilmo_help.JPG)

# Toiminta

IlmoBot pohjautuu discord.py pakettiin, jossa on kaikki discord botin tarvittavat ominaisuudet.
Tämän lisäksi botti käyttää apunaan seleniumia ja chromedriveriä, joiden avulla se voi avata JavaScript nettisivuja. Ilmo komennolla botti menee url:iin https://digit.fi/ilmo, ja katsoo onko avoimia tapahtumia. Botti klikkaa kaikkia tapahtumia, ja kerää talteen osallistujamäärän, sekä ajan, milloin ilmoittautuminen päättyy.
