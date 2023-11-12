scanUp.py is used for scanning and app.py is the web interface

## Inspiration

At least two of us weren't registered going into the event so we got up at 8AM to get to Education Sciences, hoping to be one of the first on the waitlist. 

We were not. 

When we did eventually enter, we thought that the check-in system was overloaded (no fault of the organizers!) just because of the sheer number of people who showed up. We thought we could create a more efficient system. In addition, we wanted to create a way to explore local events using the data from the check-in system so that more people could check out what was happening around Madison.   

## What it does

Our project is effectively split into two different sets of users: organizers and event-goers. 

- Organizers: The ability to create events and a check-in system that uses WiscIDs
- Event-goers: A map to check out local events with different intensities depending on how many people are in attendance 

## How we built it

- Scanning WiscIDs: used OpenCV to scan the bar code on WiscIDs using a connected iPhone
- Databases with MongoDB: kept track of new events and users at events through databases
- Creating events: Using location names, long/lat coordinates, and a login secret key to make changes to events
- Map to check out local events: WIP

## Challenges we ran into
- Learning curves associated with front-end development
- The staticness of Github pages
- Low-resolution webcams on computers
  
## Accomplishments that we're proud of
We are proud of the fact our project was capable of being both technologically complex and simple in operation for users. The ability to market this project to users for increasing their quality of life was fundamental to the foundations of the idea, and we believe we have accomplished this goal beyond what we set out to do. 

## What we learned
From this Hackathon and our project overall, we have learned that coding is hard. Alike to our original predicament of signing up for MadHacks, creating efficient systems is time-consuming and we have developed a newfound appreciation for the organizers of MadHacks Fall 2023. Much of hackathons and coding in general revolves around the idea of nonlinear development of projects, and throughout these two days we have found that that is in fact true, especially in web development. 

## What's next for our project:
After we refine the operability of Bouncer and increase user friendliness, we hope to market this website across our campus in order to increase user count. Later on, we hope to create a mobile app for organizers for barcode scanning without the need of a computer for events, as well as the inclusion of a management system within the app. Finally, we will market the project across other college campuses and venues, in hopes of increasing customer use and improving the efficiency of as many events as possible. 
