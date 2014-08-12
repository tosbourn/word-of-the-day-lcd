# Dependencies

This uses pifacecad for speaking to the Pi's LCD display, so we need:

`sudo apt-get install python{,3}-pifacecad`

It also uses the wordnik API so we need to install it:

`easy_install wordnik`

Because of the wordnik integration we need an API key, for this version you just need to run an export with your key;

```
  export wordnik_api_key=YOUR_API_KEY
  python3 wotd.py

```
