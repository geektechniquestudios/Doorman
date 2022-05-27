# **WIP**

###### please excuse the state of this readme, I've had to pick and choose my prioritiies lately, so this is on my backburner.

---

---

# Doorman

### This is a personal Raspberry Pi project that uses two ultrasonic sensors to operate a relay.

#### [Video Demo](https://www.youtube.com/watch?v=LjEhM52aX-M)

[Doorman](doorman.jpg)

This software uses ultrasonic sensors, relays, a security camera, and a display with my calendar, weather, and commute. Not only does the camera take a video; the pi sends that video to another computer on my local network. You could easily add a line to send your security footage to [dropbox](https://www.dropbox.com/developers/documentation/python#tutorial) or any other remote location. It also operates my lights by the front door with context, only turning on each light when it makes sense. There's also a browser based service that I crontab to run full screen on boot called [dakboard](https://www.dakboard.com/site). It shows my calendar, the weather, and my commute.

To use the software, just run the `doorman.py` file.

## Parts List

#### many of these links aren't the exact items used in this build, but I did some cursory searching on amazon. These aren't paid links.

- [2 ultrasonic sensors](https://www.amazon.com/Ultrasonic-Distance-Measuring-Duemilanove-Raspberry/dp/B01BVCLCQ6/ref=sr_1_3?dchild=1&keywords=rpi+ultrasonic+sensor&qid=1602985706&sr=8-3)
- [wide angle camera](https://www.amazon.com/Raspberry-Camera-Module-Fisheyes-Webcam/dp/B07T9ZCQLW/ref=sxts_sxwds-bia-wc-drs1_0?crid=116I7YIV8N1NZ&cv_ct_cx=rpi+camera+wide+angle&dchild=1&keywords=rpi+camera+wide+angle&pd_rd_i=B07T9ZCQLW&pd_rd_r=d627d616-146c-48f8-8492-475cdb1a0258&pd_rd_w=SHQpJ&pd_rd_wg=s8F4f&pf_rd_p=ecbfa24d-f48c-4d5c-83aa-9549f4e7c925&pf_rd_r=FDENYN2R5DDP3E79QERT&psc=1&qid=1602985858&sprefix=rpi+wide+an%2Caps%2C145&sr=1-1-f6b8d51f-2c55-4dc3-89ad-0c3639671b2d)
- [2 1k resistors](https://www.amazon.com/BOJACK-Resistors-Assortment-Thermistor-Photoresistor/dp/B07QXP4KVZ/ref=sr_1_13?dchild=1&keywords=resistors+1k+10k&qid=1602985902&sr=8-13)
- [2 10k resistors](https://www.amazon.com/BOJACK-Resistors-Assortment-Thermistor-Photoresistor/dp/B07QXP4KVZ/ref=sr_1_13?dchild=1&keywords=resistors+1k+10k&qid=1602985902&sr=8-13)
- [double relay (not exact part)](https://www.amazon.com/ARCELI-KY-019-Channel-Module-arduino/dp/B07BVXT1ZK/ref=sr_1_5?dchild=1&keywords=arduino+relay&qid=1602985977&sr=8-5)
- [wires](https://www.amazon.com/WayinTop-Expansion-Raspberry-Solderless-Breadboard/dp/B08736NSPK/ref=sr_1_3?dchild=1&keywords=rpi+wires%5C&qid=1602986050&sr=8-3)
- [prototype board](https://www.amazon.com/ElectroCookie-Solderable-Breadboard-Electronics-Gold-Plated/dp/B081MSKJJX/ref=sr_1_14?dchild=1&keywords=protoboard&qid=1602987630&sr=8-14)
- [soldering equipment](https://www.amazon.com/Electronics-Soldering-Portable-Auto-sleep-Thermostatic/dp/B0852XJN11/ref=sr_1_1_sspa?dchild=1&keywords=soldering+iron&qid=1602987773&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyS0NKT0VRMExNUTkzJmVuY3J5cHRlZElkPUEwNDM2OTQ3MU1ZVU1DUzRSRTlWQiZlbmNyeXB0ZWRBZElkPUEwNDIxNTM3MlBTVEJBQThBMVVSViZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
- [display](https://www.amazon.com/ELECROW-Display-1024X600-Function-Raspberry/dp/B01GDMDFZA/ref=sr_1_1_sspa?crid=2RTSG59KNY467&dchild=1&keywords=pi+display&qid=1602988546&sprefix=pi+disp%2Caps%2C150&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFDWlBFNVpLV1YxRjQmZW5jcnlwdGVkSWQ9QTA4MTYzNDgzVDBaWjhBSk9MN0gyJmVuY3J5cHRlZEFkSWQ9QTA4NTE1MDkyVFdNVjdVSUtYSTU4JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

## Wiring

[img of the wiring to come]

## Notes

- Ultrasonics frequently give false reads, so there is some included fault tolerance that you can adjust in the main script.
- In case you've never messed with an outlet, they are **high voltage and can kill you**. Please be careful if you intend to connect wires to an outlet.

## Ideology

##### Part of the inspiration for the doorman comes from a funny scene from Black Mirror where the antagonist doesn't tip the pizza guy. The door seemed really cool, gving me grandious ideas about hollowing out a wooden door and using inductive charing through the doorframe with a small battery in the door to keep everything on when the door is opened along with a smart lock. I live in an apartment and front doors are wildly expensive. So I made practical decisions about how far to take this idea. It's shelved for now, but I might pick it up and make a v2 one day.

[img of black mirror door]
[img of doorman]
