# whatsapp-parser
Python tool for parsing exported whatsapp group chats to a dataframe.

Exporting a whatsapp chat to a file results in a plain .txt file (can currently only be done in mobile client).
This simple program places the data from the file in a Pandas dataframe with columns `datetime`, `userid`, and `content`, which can be used in data science projects researching the contents of Whatsapp chats. An example of this would be the analysis of interview answers gathered in Whatsapp chats.

Phone numbers and contact names are anonymized by default.
