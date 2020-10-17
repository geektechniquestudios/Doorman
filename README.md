# Currently Under Construction
---
---
# Doorman
### This is a personal Raspberry Pi project that uses two ultrasonic sensors to operate a relay.
#### [Video Demo](https://www.youtube.com/watch?v=LjEhM52aX-M)
[gif of kirstie walking thorugh door]

This software uses ultrasonic sensors, relays, a security camera, and a display with my calendar, weather, and commute to welcome me and see me off. Not only does the camera take a video; the pi sends that video to another computer on my local network. You could easily add a line to send your security footage to [dropbox](https://www.dropbox.com/developers/documentation/python#tutorial) or any other remote location. It also operates my lights by the front door with context, only turning on each light when it makes sense. There's also a browser based service that I crontab to run full screen on boot called [dakboard](https://www.dakboard.com/site). It shows my calendar, the weather, and my commute.

To use the software just run the `doorman.py` file

## Wiring
- parts list
  - [2 ultrasonic sensors](amazon.com/)
  - [wide angle camera](amazon.com/)
  - [2 1k resistors](??)
  - [2 10k resistors](??)
  - [double relay](amazon.com/)
  - [breadboard and wires](amazon.com/)
  - [prototype board](amazon.com/)
  - [soldering equipment](amazon.com/)
- how to wire up the parts
  [img of the wiring]
  
## Notes
  - there is some included fault tolerance that you can adjust. Ultrasonics frequently give false reads.
  - @todo
  
  
## Ideology
##### I was somewhat inspired by funny scene from Black Mirror where the antagonist doesn't tip the pizza guy. The door seemed really cool, gving me grandious ideas about hollowing out a wooden door and using inductive charing through the doorframe with a small battery in the door to keep everything on when the door is opened along with a smart lock. I live in an apartment and front doors are wildly expensive. So I made practical decisions about how far to take this idea. It's shelved for now, but I might pick it up and make a v2 one day.

[img of black mirror door]
[img of doorman]
