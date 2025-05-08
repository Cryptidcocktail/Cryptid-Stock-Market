import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

st.title("Cryptid Stock Market Tracker")
st.write("Tracking Google Trends popularity of your favorite cryptids in near real time.")

cryptids = [
    'Mothman', 'Flatwoods Monster', 'Bigfoot', 'Sam The Sandown Clown',
    'Grafton Monster', 'Fresno Nightcrawler', 'Chupacabra', 'Wendigo',
    'Van Meter Visitor', 'Dover Demon', 'Sheepsquatch', 'Batsquatch',
    'Black Eyed Kids', 'Dogman'
]

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(cryptids, timeframe='now 1-d')
data = pytrends.interest_over_time().drop(columns=['isPartial'])

st.subheader("Current Trend Chart")
fig, ax = plt.subplots(figsize=(12, 6))
for cryptid in cryptids:
    ax.plot(data.index, data[cryptid], label=cryptid)

ax.set_xlabel("Time")
ax.set_ylabel("Search Popularity (0–100)")
ax.set_title("Cryptid Search Trends (Past 24 Hours)")
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
st.pyplot(fig)

if st.checkbox("Show raw data table"):
    st.write(data)
