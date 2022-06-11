# News Summary using tkinter and Tensorflow

## Prerequisires
- tkinter
- turtle
- nltk
- textblob
- newspaper module

## Process
1. Open a GUI webpage consisting of several inputs
2. Disable all textfield till user pastes URL 
3. When he pressed Summarise button, command summarise function
4. We used article package to get the data from given URL and do natural language processing using nlp()
5. After getting all processed data, place into them respective places, like title, author, publisher etc
6. To do sentiment analysis we need convert text into blob
7. Then we get polarity from that analysis
8. That's it. Whole thing is done by the package itself.
