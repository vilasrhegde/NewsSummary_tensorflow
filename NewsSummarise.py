import tkinter as tk
from turtle import color 
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt')

def summarise():

    url = utext.get('1.0','end').strip()
    # url = 'https://edition.cnn.com/2022/02/18/us/california-family-yosemite-final-moments-trnd/index.html'

    article= Article(url)

    article.download()
    article.parse()

    article.nlp() #natural language processing

    # print(f"\n\nTitle: {article.title}")
    # print(f"\nAuthors: {article.authors}")
    # print(f"\nPublication: {article.publish_date}")
    # print(f"\n\nSummary: {article.summary}\n\n")

    title.config(state='normal')
    author.config(state='normal')
    pub.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    pub.delete('1.0','end')
    pub.insert('1.0',article.publish_date)
    
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis = TextBlob(article.text) #whole text
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}  Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    pub.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


    # analysis = TextBlob(article.text) #whole text
    # print(analysis.polarity)
    # print(f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

#GUI

root = tk.Tk()
root.title('Summary of your news') 
root.geometry('1200x600')

print('GUI is opened!')
ulabel = tk.Label(root,text='URL')
ulabel.pack()

utext = tk.Text(root,height=3, width=150)
utext.pack()
btn = tk.Button(root,text='Summarise', command=summarise)
btn.config(state='normal',bg='#000',fg='#fff')
btn.pack()

tlabel = tk.Label(root,text='Title')
tlabel.pack()

title = tk.Text(root,height=1, width=150)
title.config(state='disabled',bg='#dddddd')
title.pack()

alabel = tk.Label(root,text='Author')
alabel.pack()

author = tk.Text(root,height=1, width=150)
author.config(state='disabled',bg='#dddddd')
author.pack()

plabel = tk.Label(root,text='Publication')
plabel.pack()

pub = tk.Text(root,height=1, width=150)
pub.config(state='disabled',bg='#dddddd')
pub.pack()

slabel = tk.Label(root,text='Summary')
slabel.pack()

summary = tk.Text(root,height=15, width=150)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

sentlabel = tk.Label(root,text='Sentiment Analysis')
sentlabel.pack()

sentiment = tk.Text(root,height=1, width=150)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()



 

root.mainloop()