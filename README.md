# whatsapp-parser
Python tool for parsing exported whatsapp groupchats to a dataframe.

Exporting a whatsapp chat to a file results in a plain .txt file (can currently only be done in mobile client).
This simple program places the data from the file in a Pandas dataframe with columns 'datetime', 'userid', and 'content'.
Phone numbers and contact names are anonymized by default.
