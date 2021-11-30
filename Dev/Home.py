import streamlit as st
import streamlit.components.v1 as components
import pickle
import pandas as pd
import requests
import numpy as np


games_dict = pickle.load(open('dict_games','rb'))  #reading the pickle file for game details
games = pd.DataFrame(games_dict) #converting to a dataframe

users_dict = pickle.load(open('dict_users','rb'))  #reading the pickle file for user details
users = pd.DataFrame(users_dict)  #converting to a dataframe

dict_game_names = pickle.load(open('dict_games_with_names','rb'))
game_names = pd.DataFrame(dict_game_names)


dict_pre_games = pickle.load(open('dict_games_with_names_and_prevplayed','rb'))
pre_games = pd.DataFrame(dict_pre_games)

st.set_page_config(layout="wide")
first,middle,last = st.columns([1,2,1])
first.title("Dashboard")
game_array = np.insert(game_names["name"].values[0:30],0,'<select>',axis=0)
# st.write(game_array)
selected_game = middle.selectbox("Games",game_array)
selected_user = last.selectbox('userIDs',users['steamid'].values[0:30]) 

def find_appid(name):
    id = game_names.loc[game_names["name"]==name]
    appID = id["appid"]
    return int(appID)
 
# st.write(type(find_appid(selected_game)))


# st.write(selected_user)

def user_recommended_games(selected_user):
    selected_row = users.loc[users['steamid']== selected_user]
    values = list(selected_row['similar'])
    # st.write(values[0])
    return values[0]

def fetch_image(value):
    return "https://steamcdn-a.akamaihd.net/steam/apps/{}/header.jpg".format(value)

def fetch_name(value):
    name = game_names.loc[game_names["appid"]==value]
    str_name = name["name"].to_string(index=False)
    return str_name

def recommended_games(selected_game):
    selected_row = games.loc[games["appid"]==selected_game]
    values = list(selected_row['similar'])
    # st.write(values[0])
    return values[0]



if(selected_user and selected_game != '<select>'):
    selected_game = find_appid(selected_game)
    game_recommendations = recommended_games(selected_game)

    components.html(
    """
    <style>
    
    .vl {
    border-bottom: 1px solid white;
    }
    </style>
    <div class="vl"></div>
    

    """
    )

    col0,col01 = st.columns(2)
    with col0:
        st.image(fetch_image(selected_game),caption=fetch_name(selected_game))
    # with col01:
    #     st.markdown("Generating random paragraphs c"*10)

    components.html(
        """
        <style>
        .v2{
            text-align:center;
        }
        hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(255, 255, 255,0), rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0));
        }
        </style>
        <div class="v2"><h2 style="color:white;margin-left:1%;margin-top:4%;margin-bottom:0%;font-family:Garamond;">MORE LIKE THIS</h2></div>
        <hr width="18%" align="center">
        """
    )

    
    

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.image(fetch_image(game_recommendations[0]),caption=fetch_name(game_recommendations[0]))
    with col2:
        st.image(fetch_image(game_recommendations[1]),caption=fetch_name(game_recommendations[1]))
    with col3:
        st.image(fetch_image(game_recommendations[2]),caption=fetch_name(game_recommendations[2]))
    with col4:
        st.image(fetch_image(game_recommendations[3]),caption=fetch_name(game_recommendations[3]))



    col5,col6,col7,col8 = st.columns(4)

    with col5:
        st.image(fetch_image(game_recommendations[4]),caption=fetch_name(game_recommendations[4]))
    with col6:
        st.image(fetch_image(game_recommendations[5]),caption=fetch_name(game_recommendations[5]))
    with col7:
        st.image(fetch_image(game_recommendations[6]),caption=fetch_name(game_recommendations[6]))
    with col8:
        st.image(fetch_image(game_recommendations[7]),caption=fetch_name(game_recommendations[7]))



    col9,col10,col11,col12 = st.columns(4)
    with col10:
        st.image(fetch_image(game_recommendations[8]),caption=fetch_name(game_recommendations[8]))
    with col11:
        st.image(fetch_image(game_recommendations[9]),caption=fetch_name(game_recommendations[9]))















elif(selected_user):
    previous_played = pre_games.loc[pre_games['steamid']==selected_user]["previously_played"].iloc[0]
    user_recommendation = user_recommended_games(selected_user)
    components.html(
    """
    <style>
    
    .vl {
    border-bottom: 1px solid white;
    }
    .v2{
        text-align:center;
    }
    
    hr {
    border: 0;
    height: 1px;
    background-image: linear-gradient(to right, rgba(255, 255, 255,0), rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0));
    }
    </style>
    <div class="vl"></div>
    <div class="v2"><h2 style="color:white;margin-left:1%;margin-top:4%;margin-bottom:0%;font-family:Montserrat;">Home</h2></div>
    
    <hr width="18%" align="center">
    """
    )



    col1,col2,col3,col4 = st.columns(4)
        
    try:
        with col1:
            st.image(fetch_image(previous_played[0][0]),caption=fetch_name(previous_played[0][0]))
        with col2:
            st.image(fetch_image(previous_played[1][0]),caption=fetch_name(previous_played[1][0]))
        with col3:
            st.image(fetch_image(previous_played[2][0]),caption=fetch_name(previous_played[2][0]))
        with col4:
            st.image(fetch_image(previous_played[3][0]),caption=fetch_name(previous_played[3][0]))
    except Exception:
        pass


    components.html(
        """
        <style>
        .v2{
            text-align:center;
        }
        hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(255, 255, 255,0), rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0));
        }
        </style>
        <div class="v2"><h2 style="color:white;margin-left:1%;margin-top:4%;margin-bottom:0%;font-family:Garamond;">Recommended</h2></div>
        <hr width="18%" align="center">
        """
    )

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.image(fetch_image(user_recommendation[0]),caption=fetch_name(user_recommendation[0]))
    with col2:
        st.image(fetch_image(user_recommendation[1]),caption=fetch_name(user_recommendation[1]))
    with col3:
        st.image(fetch_image(user_recommendation[2]),caption=fetch_name(user_recommendation[2]))
    with col4:
        st.image(fetch_image(user_recommendation[3]),caption=fetch_name(user_recommendation[3]))



    col5,col6,col7,col8 = st.columns(4)

    with col5:
        st.image(fetch_image(user_recommendation[4]),caption=fetch_name(user_recommendation[4]))
    with col6:
        st.image(fetch_image(user_recommendation[5]),caption=fetch_name(user_recommendation[5]))
    with col7:
        st.image(fetch_image(user_recommendation[6]),caption=fetch_name(user_recommendation[6]))
    with col8:
        st.image(fetch_image(user_recommendation[7]),caption=fetch_name(user_recommendation[7]))



    col9,col10,col11,col12 = st.columns(4)
    with col10:
        st.image(fetch_image(user_recommendation[8]),caption=fetch_name(user_recommendation[8]))
    with col11:
        st.image(fetch_image(user_recommendation[9]),caption=fetch_name(user_recommendation[9]))








