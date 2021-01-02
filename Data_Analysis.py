from Get_Rezension import df_google

df_google=df_google.replace({"Bewertung: 5,0 von 5,": 5, "Bewertung: 4,0 von 5,": 4, "Bewertung: 3,0 von 5,": 3,
                   "Bewertung: 2,0 von 5,": 2, "Bewertung: 1,0 von 5,": 1})

# how to deal with the date?