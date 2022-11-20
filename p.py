import streamlit as st
import pickle
import pandas as pd

Teams = ['Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Mumbai Indians']
Cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']
pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL PREDICTION')

col1,col2 = st.columns(2)

with col1:
    Batting_team = st.selectbox('Select Batting Team',sorted(Teams))
with col2:
    Bowling_team = st.selectbox('Select Bowling Team',sorted(Teams))
selected_City = st.selectbox('Select City', sorted(Cities))
target = st.number_input('Target')
col3,col4,col5 = st.columns(3)
with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Completed overs')
with col5:
    wickets = st.number_input('Wickets out')
if st.button('Predict'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    i_df = pd.DataFrame({'BattingTeam':[Batting_team],'BowlingTeam':[Bowling_team],
 'City':[selected_City],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets],
 'target':[target],'current_run_rate':[crr],'required_run_rate':[rrr]})

    result = pipe.predict_proba(i_df)
    lose = result[0][0]
    win = result[0][1]
    st.text(Batting_team + "- " + str(round(win*100)) + "%")
    st.text(Bowling_team + "- " + str(round(lose*100)) + "%")

