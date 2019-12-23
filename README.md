A PLATFORM TO MANAGE THEATRES.

A Business owner has two theaters "Sathyam" and "Luxe Mini" with different capacity say 50 and 25 respectively at different locations.
Each theatre will host 3 shows daily. The show timings may vary form one theatre to another. The owner can decide to run same movie for all shows or with different movies. (System should be scalable to adopt multiple theatres and multiple shows)

Develop a console application which can help the business owner to to manage his ticket vending process.

The system should be capable of doing the following:

    Ability to issue and maintain tickets(for simplicity don't track about dates. assume all is for current day). The ticket prices can vary based on the selected type(I II or III class). Each ticket having a ticket number, seat number (not mandatory), name of the theatre, name of the movie and show, Ticket type and price.
    Ability to list all the movies running in a particular theatre.
    Ability to list all movies.
    Ability to list all Theatres with shows, given a movie name.
    Ability to generate report(csv or excel) about the Revenue generated per show.

Report example:

Theatre Name, Show Timing, Total Amount Sold
Sathyam,9:30 AM,22000 Rs
Sathyam,1:30 PM,25000 Rs
Sathyam,6:00PM,80000 Rs
Luxe Mini,9:30 AM,25890 Rs
Luxe Mini,1:30 PM,28000 Rs
Luxe Mini,6:00PM,65000 Rs

Today's show details available in a csv file (Today.csv)

Sathyam,10:00 AM,Avengers: Endgame
Sathyam,14:00 AM,AD ASTRA
Sathyam,18:00 AM,Avengers: Endgame
Luxe Mini,10:00 AM,STAR WARS: THE RISE OF SKYWALKER
Luxe Mini,15:00 AM,STAR WARS: THE RISE OF SKYWALKER
Luxe Mini,18:30 AM,Avengers: Endgame

