import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image
from smart_open import smart_open
# model = pickle.load(open('final_model.save.pkl', 'rb'))


st.title("Sports Predict App")
st.header("Sports Performace Prediction")
st.write("This web app predicts the overall performance of a player based on particular features")

image = Image.open("sports.jpg")
st.image(image, use_column_width=True)
st.write("Please insert values to get overall prediction of player")


clubs = ['FC Barcelona','Juventus','Paris Saint-Germain','Manchester United','Manchester City','Chelsea','Real Madrid','Atlético Madrid','FC Bayern München','Tottenham Hotspur','Liverpool','Napoli','Arsenal','Milan','Inter','Lazio','Borussia Dortmund','Vissel Kobe','Olympique Lyonnais','Roma','Valencia CF','Guangzhou Evergrande Taobao FC','FC Porto','FC Schalke 04','Beşiktaş JK','LA Galaxy','Sporting CP','Real Betis','Olympique de Marseille','RC Celta','Bayer 04 Leverkusen','Real Sociedad','Villarreal CF','Sevilla FC','SL Benfica','AS Saint-Étienne','AS Monaco','Leicester City','Atalanta','Grêmio','Atlético Mineiro','RB Leipzig','Ajax','Dalian YiFang FC','Everton','West Ham United','FC Köln', 'TSG 1899 Hoffenheim','Shanghai SIPG FC','OGC Nice','Al Nassr','Wolverhampton Wanderers','Borussia Mönchengladbach','Hertha BSC','SV Werder Bremen', 'Cruzeiro',
'Athletic Club de Bilbao','Torino']
potential = st.slider("Player Potential: ", 0, 100)
# club = st.number_input("Pick Club number based on club description above")
club = st.selectbox('Please pick club name from list below',clubs)
wage = st.number_input("Please enter wage of player")
international_reputation = st.slider("Player International Reputation: ", 0, 5)
short_passing = st.slider("Player Short Passing: ", 0, 100)
reactions = st.slider("Player Reactions: ", 0, 100)
vision = st.slider("Player Vision: ", 0, 100)
composure = st.slider("Player Composure: ", 0, 100)
release_clause = st.input("Please enter release Clause")

data = {'Potential' : potential,
 'Club' : clubs.index(club),
 'Wage' : wage,
 'International Reputation' : international_reputation,
 'ShortPassing' : short_passing,
 'Reactions' : reactions,
 'Vision' : vision,
 'Composure' : composure,
 'ReleaseClause' : release_clause

	}
# @st.cache
# def load_model(ttl=30):
# 	  return pickle.load(open('final_model.save', 'rb'))
# model = load_model()

# model = pickle.load(smart_open('https://mlassignment.s3.eu-de.cloud-object-storage.appdomain.cloud/final_model%20(1).save', 'rb'))



if st.button('Predict Overall Performance'):
# 	model = pickle.load(open('final_model.save', 'rb'))
# 	features = pd.DataFrame(data, index=[0])
# 	prediction = model.predict(features)
	st.header("Please find predicted value below")
# 	st.write("The overall predicted score for the above player is", np.round(prediction[0]))
#   	st.write("The overall predicted score for the above player is", clubs.index(club))
else:
	st.write('Thank You For Trusting Us')
