#Inspiration 
Within the realm of socialization and making new connections, there exists the question of how much you can really learn about one's personality via text or voice patterns. The best way to descern this is by general inference given social interaction. Also, at times when you may have someone who is not around to converse as often but you long for their company in some form during the interim. Suppose there was a way to simulate someone which impact you in some way (i.e. humor, love, intellect etc) in a way such that the interaction is seemlessly like that person. This can be done by taking voice and text from a friend. Later able to dessiminate this data in the form of a conversation by text (later by voice).

#What it does
This starts by allowing the user to choose a text message feed from anyone (Assuming 2 person conversation) and will create a personality based off the recipient of the convesation. The derived data will rely on the sender (you) for guaging proper weights, determining a pattern and trend analysis. This will be used with how the chat bot responds to texts given conditions. These conditions are determined based on preset categories (i.e. education, happiness, politics, anger, sad etc). The Vent Bot will train off data provided as well as your conversations with it.

#How we Built it
Using python along with the libraries SQLite, Pandas, Tensorflow, regex, colorama, Py-Levenshtein, and requests we began by importing a text file into XML format. Then created a database table RECIPIENTS to house the data extracted from the XML file in columns ID, textbody etc. Then extracted those into the trainng sets to and from which distinguishing by type id (who the person sending the message is). The program can run an inference script off this data.

#Challenges we ran into
The initial part which was having the date inserted into a database caused some trouble but we were able to overcome this. However, this caused a major delay in the other parts of the program. Therefore we weren't able to have it run as effectively as planned. Voice recognition could not be implimentented. Also ran into issues using Kuda tool kit to install for the chat bot training.

#Accomplishments that we are proud of
We were able to successfully load into a database table then sort into training files. Then successful creation of the inference script for responses.


# VentBot
An artificially intelligent bot with a loaded personality of choice to vent with.

This bot is meant to be there for you when there seems to be no one around to understand how you feel. Talk to this bot and it will surely uplift your spirits. Why? Because it replicates talking to your best friend, favorite relative, or even yourself!

### Features
* Create a personality based on text and/or voice data from a friend, relative, or yourself
* Learns talking patterns of personality provided
* Uses LyreBird on voice data (if provided) to recreate the voice of the personality provided

### Platforms
* Windows
* Linux/Unix
* Android (Post-Hackathon)
* iOS (Post-Hackathon)


### How it Works
* Use sqlite3 python library to create database of text message data and voice data to be queried by neural network
* Use TensorFLow to create a chatbot neural network
* Chatbot learns on text message data

Programming Language: **Python**

<a href="https://hackumbc-s18.slack.com">HackUMBC 2018 Link</a>
