# raspi-newstext

Newsticker for Teletext on Raspberry Pi. Uses RSS-Feed to load newsticker from [heise online](https://heise.de).

## Getting started

* Install [VBit2 by peterkvt](https://github.com/peterkvt80/vbit2)

Run following commands to start virtualenv and load news:

```plaintext
git clone https://github.com/jamct/raspi-newstext
python3 -m venv ~/raspi-newstext
source ~/raspi-newstext/bin/activate
pip install -r requirements.txt
python getheise.py
```

This script will generate Index File P100.tti in /home/pi/teletext. Run vbit2 to watch it in action.

## Documentation

This project is part of an article from c't magazine: [Teleticker](https://ct.de/yw46)