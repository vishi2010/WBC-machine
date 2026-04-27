# White Blood Cell counting machine 

I was inspired to make this project after my Grandmother was diagnosed with Pancreatic cancer, which lead to low White blood cell count. Machines that count white blood cell can be extremely expensive ranges from $500 to $5,000. The schematic for Segment A (re-usable section) that analyses the white blood cell count and sends results to reciever costs about $46. Segment B (work in progress) will cost about $1.60. However, due to it being non-reusable the consumer would have to spend $1.60 per use.  

Segment A includes: a 3.3v 500Mah battery, a charging module (TP4056), STM32F411CEU6 essentially the brain; essentially where the CNN lives and all the logic. OV5460-A71A, the 5mp camera which takes the photos of the Microfluidic chamber. TP4056, the charging module which charges the battery. The HM-10 the bluetooth chip which sends information to the phone of the user. The wiring still needs to be down between the HM-10 and the STM32F411CEU6 (brain and bluetooth). 

Segment B will include: a needle that will get a small sample of blood, a microfluidic chmaber which seperate the sample into 8 different chambers. the camer will face the MC and will take photos of each chamber. the CNN will count the number of white blood cells and then take the average of all 8 chambers, multiply it by volumbe of blood in the body depending on height, weight, and age. It will then send a diagnosis depending on wether the number of white blood cells falls it estimates in the body. 

created with fusion 360. 
Segment A schematic 
<img width="1470" height="956" alt="Screenshot 2026-04-26 at 8 24 36 PM" src="https://github.com/user-attachments/assets/79a77deb-98d9-4a7f-9476-d601460e8d1f" />

Segment A schematic 
<img width="1470" height="956" alt="Screenshot 2026-04-27 at 8 34 12 AM" src="https://github.com/user-attachments/assets/60b574c9-14e8-4760-b278-9e5a53d24edc" />

Segment A schematic
<img width="1470" height="956" alt="Screenshot 2026-04-27 at 8 34 16 AM" src="https://github.com/user-attachments/assets/285d0b18-202d-4beb-8fb5-6eb9f02da710" />


Segment B coming soon...
