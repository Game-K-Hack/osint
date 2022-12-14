<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/osint/main/logo.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.2" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=stable&color=green" alt="Version - stable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
  <a href="https://www.paypal.com/paypalme/gamekdonate">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate" />
  </a>
</div>

<h4 align="center">Information retrieval program by pseudo</h4>

<p align="center">
  <a href="#definition">Definition</a> •
  <a href="#site">Site</a> •
  <a href="#command">Command</a>
</p>

<br>
<br>

## Definition

Open source intelligence is the collection and analysis of information obtained from public information sources. It is mainly used for activities related to national security, law enforcement and economic intelligence in the private sector. The heterogeneous set of these investigative practices comes from "the plurality of definitions of the Osint investigation, according to its practice by journalists, magistrates, researchers or activists".

OSINT sources can be divided into six different categories of information flow:

* The media, printed newspapers, magazines, radios, television channels in the different countries;
* Internet, online publications, blogs, discussion groups, citizen media, YouTube and other social networks;
* Government data, reports, budgets, hearings, directories, press conferences, official websites and speeches. This information comes from official sources, but is publicly accessible and can be used freely and free of charge;
* Professional and academic publications, from academic journals, conferences, publications and theses;
* Commercial data, satellite imagery, financial and industrial assessments and databases;
* Gray literature, technical reports, preprints, patents, working papers, trade documents, unpublished works and newsletters.

Open source intelligence is different from research because it applies the process associated with the intelligence cycle for the purpose of seeking information to respond to specific tasks or in support of decision-making, and not acquisition. of knowledge.

## Site

For the moment, the script looks for the nickname only on `linktr.ee`. But other bookstores will arrive...

## Command

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
