# MoodRecord - Waffle Hack Submission
Record your mood through our song selections

![Screen Shot 2022-06-19 at 11 31 35 PM](https://user-images.githubusercontent.com/74251221/174491109-e8f16f14-1231-4e99-8a06-01222ff85b5f.png)

# What it does 

MoodRecord hopes to help the users improve their journal practice, and improve your mood in the process. MoodRecord generates a playlist for user based on their current mood. After the playlist is created, the user has the option to answer a series of journal prompts, in the form of a letter to self describing and reflecting how their day was.

# How I built it

I used Spotipy, which is a micro Spotify api library for Python, as well as flask framework, and HTML, CSS and Javascript for front end. The algorithm first extracts user's saved tracks and recently played tracks, then extracts unknown songs from artists that are similar to user's favorite artists. In this way, I ensure that the playlist is a good mix of known and unknown songs. Then I combine these two lists of songs into one list, prioritizing known songs as people are hesitant to try out new music, especially after a tiring day of work. Then I select the songs based on the input user gave, and slowly increased the input through each iteration. Finally, I create a playlist from those songs.

# Challenges I ran into

The biggest one was how to translate my vision for the webapp into an algorithm. I have to examine our idea and problem from different angle, and visualize it into step by step algorithm. Plus, the spotify api can be inaccurate, so I have to run many trials. Moreover, this is my first hackathon, and first time I built something from backend to frontend. I have to learn a lot from scratch, such as how to connect front end and backend through Flask,...

# What I learned

I learned so much from this project!! On technical side, how to use Flask, how to design an algorithm based on an idea, just generally how to improve my web designing skill. On soft skill side, I learned key project management skills, such as never underestimate the front end, especially when styling with CSS (it takes a lot longer than I thought), the submission takes a lot of effort too, plan specifically what features I need to work on in this specific time lot,...

What's next for MoodRecord

I want to improve my algorithm, as I realize it can be very slow at the selecting songs step, plus I want to improve our ui/ux as I didn't have enough time to make it as pretty as I expect. Moreoever, I hope I can integrate more journal prompts which can allow users wider selection

