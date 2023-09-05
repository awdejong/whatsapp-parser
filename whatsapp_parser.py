import pandas as pd
import re
from datetime import datetime

def whatsapp_parse(source_file: str, anonymize: bool = True, exclude_media: bool = True) -> pd.DataFrame:

    # Store individual lines from source file
    with open(source_file, encoding="utf-8") as file:
        lines = file.readlines()

    # Regex for "m/d/yy, hh:mm - " followed by a phone number or contact name and a ":"
    rx = re.compile(
        r"((?:\d|1[0-2])\/(?:\d|[123]\d)\/(?:\d|\d\d)\, \d\d[:]\d\d) [-] (.+?)(?:[:] |left|added.+|changed the group.+)")

    #df = pd.DataFrame(columns=["timestamp", "user", "content"])
    rows = []

    # Go through file line by line, add new row to dataframe for each message.
    # When a line only has one element, it is a continuation of the previous message.
    for line in lines:
        parts = rx.split(line)

        if len(parts) > 1:
            #create dict for row include time
            row = dict()
            row["timestamp"] = parts[1]
            row["user"] = parts[2]
            row["content"] = parts[3]
            rows.append(row)

        else:
            if len(rows) > 0:
                last = len(rows)-1
                rows[last]["content"] = rows[last]["content"] + parts[0]

    df = pd.DataFrame(rows)
    
    # Remove empty messages and messages that only contained an image originally
    if exclude_media:
        df = df.drop(df[(df.content == "\n") | (
            df.content == "<Media omitted>\n")].index)
    else:
        df = df.drop(df[df.content == "\n"].index)

    df.reset_index(drop=True, inplace=True)

    # Convert text timestamp to datetime format
    df["datetime"] = df.timestamp.map(
        lambda x: datetime.strptime(x, "%m/%d/%y, %H:%M"))

    # Factorize phone numbers and contact names
    # Results in every user having a unique, anonymous ID
    if anonymize:
        df["user_id"] = pd.Series(pd.factorize(df.user)[0])
        df = df[["datetime", "userid", "content"]]
    
    else:
        df = df[["datetime", "user", "content"]]

    return df
