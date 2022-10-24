<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/osint/main/logo.png" width=150 />
</p>

## Définition

Le renseignement d'origine sources ouvertes est le recueil et l'analyse d'information obtenue à partir de source d'information publique. Il est principalement utilisé dans le cadre d'activités liées à la sécurité nationale, l'application de la loi et l'intelligence économique dans le secteur privé. L'ensemble hétéroclite de ces pratiques d’investigation provient de « la pluralité des définitions de l’enquête Osint, en fonction de sa pratique par des journalistes, des magistrats, des chercheurs ou des activistes ».

Les sources de l'OSINT peuvent être divisées en six catégories différentes de flux d'informations :

* Les médias, journaux imprimés, magazines, radios, chaînes de télévision dans les différents pays ;
* Internet, les publications en ligne, les blogs, les groupes de discussion, les médias citoyens, YouTube et autres réseaux sociaux ;
* Les données gouvernementales, rapports, budgets, auditions, annuaires, conférences de presse, sites web officiels et discours. Ces informations proviennent de sources officielles, mais sont bien publiquement accessibles et peuvent être utilisées librement et gratuitement ;
* Les publications professionnelles et académiques, provenant de revues académiques, conférences, publications et thèses ;
* Les données commerciales, imagerie satellite, évaluations financières et industrielles et bases de données ;
* La littérature grise, rapports techniques, prépublications, brevets, documents de travail, documents commerciaux, travaux non publiés et lettres d'information.

Le renseignement d'origine sources ouvertes est différent de la recherche car il applique le processus associé au cycle du renseignement dans un but de recherche d'information pour répondre à des tâches spécifiques ou en support à la prise de décision, et non d'acquisition de connaissances.

## Site

Pour le moment, le script cherche le pseudo seulement sur `linktr.ee`. Mais d'autre librairie vont arriver...

## Commande

```
 ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██
███    ███   ███ Game K ███▌ ███   ███     ███   ▀
███    ███ ▀███████████ ███▌ ███   ███     ███
███    ███          ███ ███  ███   ███     ███
███    ███    ▄█    ███ ███  ███   ███     ███
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀


usage: osint.py [-h] [-s] [--linktr] name [name ...]

OSINT search v0.1 by Game K

positional arguments:
  name         Name of person

optional arguments:
  -h, --help   show this help message and exit
  -s, --spray  Take search on all similar name
  --linktr     Search on 'linktr.ee' website
```
