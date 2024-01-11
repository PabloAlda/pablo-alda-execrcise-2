#Importo json
import json
# Definir una lista para almacenar la información de los jugadores
"""jugadores = [
    #Dallas Mavericks
    {"Nombre": "Luka Doncic", "Altura": 200, "Peso": 98, "PromedioPPP": 33.6, "Asistencias": 9.1, "Rebotes": 8.1},
    {"Nombre": "Kyrie Irving", "Altura": 187, "Peso": 87, "PromedioPPP": 23.9, "Asistencias": 5.0, "Rebotes": 5.0},
    {"Nombre": "Tim Hardaway Jr.", "Altura": 195, "Peso": 92, "PromedioPPP": 17.1, "Asistencias": 1.7, "Rebotes": 3.6},
    {"Nombre": "Derrick Jones Jr.", "Altura": 198, "Peso": 90, "PromedioPPP": 10.3, "Asistencias": 1.0, "Rebotes": 3.8},
    {"Nombre": "Dante Exum", "Altura": 195, "Peso": 86, "PromedioPPP": 9.3, "Asistencias": 2.9, "Rebotes": 2.9},
    {"Nombre": "Dereck Lively II", "Altura": 215, "Peso": 104, "PromedioPPP": 8.7, "Asistencias": 1.3, "Rebotes": 7.6},
    {"Nombre": "Grant Williams", "Altura": 198, "Peso": 107, "PromedioPPP": 8.4, "Asistencias": 1.6, "Rebotes": 3.6},
    {"Nombre": "Jaden Hardy", "Altura": 193, "Peso": 89, "PromedioPPP": 7.9, "Asistencias": 1.6, "Rebotes": 2.0},
    {"Nombre": "Josh Green", "Altura": 198, "Peso": 95, "PromedioPPP": 6.6, "Asistencias": 2.4, "Rebotes": 2.8},
    {"Nombre": "Dexter Dennis", "Altura": 0, "Peso": 0, "PromedioPPP": 5.5, "Asistencias": 1.0, "Rebotes": 2.3},
    {"Nombre": "Dwight Powell", "Altura": 208, "Peso": 108, "PromedioPPP": 4.8, "Asistencias": 1.5, "Rebotes": 3.7},
    {"Nombre": "A.J. Lawson", "Altura": 198, "Peso": 80, "PromedioPPP": 4.8, "Asistencias": 0.6, "Rebotes": 1.4},
    {"Nombre": "Seth Curry", "Altura": 187, "Peso": 83, "PromedioPPP": 4.7, "Asistencias": 0.9, "Rebotes": 1.6},
    {"Nombre": "Maxi Kleber", "Altura": 208, "Peso": 108, "PromedioPPP": 3.4, "Asistencias": 2.0, "Rebotes": 4.2},
    {"Nombre": "Richaun Holmes", "Altura": 208, "Peso": 106, "PromedioPPP": 3.2, "Asistencias": 0.5, "Rebotes": 3.6},
    {"Nombre": "Olivier-Maxence Prosper", "Altura": 203, "Peso": 96, "PromedioPPP": 3.1, "Asistencias": 0.8, "Rebotes": 2.3},
    {"Nombre": "Brandon Williams", "Altura": 187, "Peso": 86, "PromedioPPP": 2.8, "Asistencias": 1.0, "Rebotes": 1.0},
    {"Nombre": "Markieff Morris", "Altura": 203, "Peso": 111, "PromedioPPP": 2.7, "Asistencias": 0.7, "Rebotes": 1.9},
    {"Nombre": "Greg Brown III", "Altura": 205, "Peso": 92, "PromedioPPP": 2.5, "Asistencias": 0.7, "Rebotes": 1.5},
    #Boston Celtics
    {"Nombre": "Jayson Tatum", "Altura": 203, "Peso": 94, "PromedioPPP": 27.5, "Asistencias": 4.5, "Rebotes": 8.7},
    {"Nombre": "Jaylen Brown", "Altura": 198, "Peso": 99, "PromedioPPP": 23.2, "Asistencias": 3.6, "Rebotes": 5.0},
    {"Nombre": "Kristaps Porzingis", "Altura": 220, "Peso": 108, "PromedioPPP": 19.8, "Asistencias": 1.9, "Rebotes": 7.0},
    {"Nombre": "Derrick White", "Altura": 193, "Peso": 86, "PromedioPPP": 16.4, "Asistencias": 5.2, "Rebotes": 4.1},
    {"Nombre": "Jrue Holiday", "Altura": 190, "Peso": 92, "PromedioPPP": 13.1, "Asistencias": 4.7, "Rebotes": 6.5},
    {"Nombre": "Sam Hauser", "Altura": 203, "Peso": 98, "PromedioPPP": 8.5, "Asistencias": 1.0, "Rebotes": 3.6},
    {"Nombre": "Al Horford", "Altura": 205, "Peso": 111, "PromedioPPP": 7.5, "Asistencias": 3.0, "Rebotes": 3.3},
    {"Nombre": "Payton Pritchard", "Altura": 187, "Peso": 86, "PromedioPPP": 7.7, "Asistencias": 3.0, "Rebotes": 6.8},
    {"Nombre": "Luke Kornet", "Altura": 218, "Peso": 113, "PromedioPPP": 5.1, "Asistencias": 0.9, "Rebotes": 3.6},
    {"Nombre": "Neemias Queta", "Altura": 213, "Peso": 111, "PromedioPPP": 4.9, "Asistencias": 0.5, "Rebotes": 4.8},
    {"Nombre": "Oshae Brissett", "Altura": 200, "Peso": 95, "PromedioPPP": 3.6, "Asistencias": 0.5, "Rebotes": 3.2},
    {"Nombre": "Drew Peterson", "Altura": 205, "Peso": 92, "PromedioPPP": 3.0, "Asistencias": 1.0, "Rebotes": 1.0},
    {"Nombre": "Dalano Banton", "Altura": 205, "Peso": 92, "PromedioPPP": 2.6, "Asistencias": 0.4, "Rebotes": 1.7},
    {"Nombre": "Lamar Stevens", "Altura": 203, "Peso": 102, "PromedioPPP": 1.8, "Asistencias": 0.3, "Rebotes": 0.9},
    {"Nombre": "Svi Mykhailiuk", "Altura": 200, "Peso": 92, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 1.0},
    {"Nombre": "JD Davison", "Altura": 190, "Peso": 88, "PromedioPPP": 2.5, "Asistencias": 0.4, "Rebotes": 1.5},
    #Milwaukee Bucks
    {"Nombre": "Damian Lillard", "Altura": 187, "Peso": 88, "PromedioPPP": 25.1, "Asistencias": 6.9, "Rebotes": 4.3},
    {"Nombre": "Cameron Payne", "Altura": 190, "Peso": 86, "PromedioPPP": 6.1, "Asistencias": 2.4, "Rebotes": 1.1},
    {"Nombre": "TyTy Washington Jr.", "Altura": 190, "Peso": 89, "PromedioPPP": 1.5, "Asistencias": 0.5, "Rebotes": 0.5},
    {"Nombre": "Malik Beasley", "Altura": 193, "Peso": 88, "PromedioPPP": 11.5, "Asistencias": 1.3, "Rebotes": 4.1},
    {"Nombre": "AJ Green", "Altura": 193, "Peso": 86, "PromedioPPP": 3.1, "Asistencias": 0.6, "Rebotes": 0.7},
    {"Nombre": "Andre Jackson Jr.", "Altura": 198, "Peso": 95, "PromedioPPP": 2.0, "Asistencias": 0.9, "Rebotes": 1.0},
    {"Nombre": "Khris Middleton", "Altura": 200, "Peso": 100, "PromedioPPP": 14.7, "Asistencias": 4.9, "Rebotes": 4.4},
    {"Nombre": "Jae Crowder", "Altura": 198, "Peso": 106, "PromedioPPP": 8.1, "Asistencias": 1.7, "Rebotes": 3.9},
    {"Nombre": "Pat Connaughton", "Altura": 195, "Peso": 94, "PromedioPPP": 5.5, "Asistencias": 1.8, "Rebotes": 3.5},
    {"Nombre": "Thanasis Antetokounmpo", "Altura": 198, "Peso": 97, "PromedioPPP": 0.5, "Asistencias": 0.1, "Rebotes": 1.0},
    {"Nombre": "Marjon Beauchamp", "Altura": 200, "Peso": 79, "PromedioPPP": 5.2, "Asistencias": 0.8, "Rebotes": 2.5},
    {"Nombre": "Chris Livingston", "Altura": 198, "Peso": 99, "PromedioPPP": 2.5, "Asistencias": 0.4, "Rebotes": 1.5},
    {"Nombre": "Giannis Antetokounmpo", "Altura": 210, "Peso": 109, "PromedioPPP": 31.4, "Asistencias": 5.9, "Rebotes": 11.5},
    {"Nombre": "Bobby Portis", "Altura": 208, "Peso": 113, "PromedioPPP": 12.0, "Asistencias": 1.1, "Rebotes": 6.6},
    {"Nombre": "Brook Lopez", "Altura": 213, "Peso": 122, "PromedioPPP": 12.6, "Asistencias": 1.4, "Rebotes": 5.1},
    {"Nombre": "Robin Lopez", "Altura": 213, "Peso": 124, "PromedioPPP": 0.8, "Asistencias": 0.2, "Rebotes": 1.0},
    #Philadelphia 76ers
    {"Nombre": "Patrick Beverley", "Altura": 185, "Peso": 83, "PromedioPPP": 5.1, "Asistencias": 2.3, "Rebotes": 2.8},
    {"Nombre": "Tyrese Maxey", "Altura": 190, "Peso": 89, "PromedioPPP": 25.9, "Asistencias": 6.6, "Rebotes": 3.6},
    {"Nombre": "Furkan Korkmaz", "Altura": 200, "Peso": 83, "PromedioPPP": 1.9, "Asistencias": 0.3, "Rebotes": 0.5},
    {"Nombre": "De'Anthony Melton", "Altura": 187, "Peso": 90, "PromedioPPP": 12.1, "Asistencias": 3.2, "Rebotes": 4.0},
    {"Nombre": "Jaden Springer", "Altura": 193, "Peso": 92, "PromedioPPP": 3.1, "Asistencias": 0.8, "Rebotes": 1.4},
    {"Nombre": "Ricky Council IV", "Altura": 198, "Peso": 92, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Terquavion Smith", "Altura": 193, "Peso": 74, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Nicolas Batum", "Altura": 205, "Peso": 90, "PromedioPPP": 5.8, "Asistencias": 2.2, "Rebotes": 3.8},
    {"Nombre": "Robert Covington", "Altura": 200, "Peso": 102, "PromedioPPP": 4.5, "Asistencias": 0.7, "Rebotes": 3.4},
    {"Nombre": "Tobias Harris", "Altura": 203, "Peso": 106, "PromedioPPP": 16.9, "Asistencias": 3.1, "Rebotes": 6.1},
    {"Nombre": "Danuel House Jr.", "Altura": 198, "Peso": 93, "PromedioPPP": 3.4, "Asistencias": 0.6, "Rebotes": 1.3},
    {"Nombre": "Kelly Oubre Jr.", "Altura": 200, "Peso": 92, "PromedioPPP": 13.7, "Asistencias": 1.0, "Rebotes": 4.2},
    {"Nombre": "KJ Martin", "Altura": 200, "Peso": 97, "PromedioPPP": 1.6, "Asistencias": 0.4, "Rebotes": 0.8},
    {"Nombre": "Marcus Morris Sr.", "Altura": 203, "Peso": 106, "PromedioPPP": 6.1, "Asistencias": 0.8, "Rebotes": 2.2},
    {"Nombre": "Paul Reed", "Altura": 205, "Peso": 99, "PromedioPPP": 5.7, "Asistencias": 1.2, "Rebotes": 4.4},
    {"Nombre": "Kenneth Lofton Jr.", "Altura": 200, "Peso": 124, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Joel Embiid", "Altura": 213, "Peso": 117, "PromedioPPP": 34.6, "Asistencias": 6.0, "Rebotes": 11.8},
    {"Nombre": "Mo Bamba", "Altura": 213, "Peso": 100, "PromedioPPP": 3.9, "Asistencias": 0.5, "Rebotes": 2.9},
    #Indiana Pacers
    {"Nombre": "T.J. McConnell", "Altura": 185, "Peso": 86, "PromedioPPP": 7.8, "Asistencias": 5.0, "Rebotes": 2.7},
    {"Nombre": "Tyrese Haliburton", "Altura": 195, "Peso": 79, "PromedioPPP": 23.6, "Asistencias": 12.5, "Rebotes": 4.2},
    {"Nombre": "Andrew Nembhard", "Altura": 195, "Peso": 87, "PromedioPPP": 7.8, "Asistencias": 3.9, "Rebotes": 1.7},
    {"Nombre": "Isaiah Wong", "Altura": 193, "Peso": 83, "PromedioPPP": 6.9, "Asistencias": 0.9, "Rebotes": 4.2},
    {"Nombre": "Ben Sheppard", "Altura": 198, "Peso": 88, "PromedioPPP": 2.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Buddy Hield", "Altura": 193, "Peso": 97, "PromedioPPP": 12.8, "Asistencias": 2.5, "Rebotes": 3.3},
    {"Nombre": "Bruce Brown", "Altura": 193, "Peso": 91, "PromedioPPP": 11.7, "Asistencias": 2.8, "Rebotes": 4.5},
    {"Nombre": "Jordan Nwora", "Altura": 200, "Peso": 102, "PromedioPPP": 5.4, "Asistencias": 0.9, "Rebotes": 1.6},
    {"Nombre": "Aaron Nesmith", "Altura": 198, "Peso": 96, "PromedioPPP": 11.8, "Asistencias": 1.1, "Rebotes": 3.3},
    {"Nombre": "Bennedict Mathurin", "Altura": 198, "Peso": 95, "PromedioPPP": 14.7, "Asistencias": 2.0, "Rebotes": 3.8},
    {"Nombre": "Kendall Brown", "Altura": 203, "Peso": 92, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "James Johnson", "Altura": 200, "Peso": 108, "PromedioPPP": 1.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Obi Toppin", "Altura": 205, "Peso": 99, "PromedioPPP": 11.6, "Asistencias": 1.4, "Rebotes": 3.9},
    {"Nombre": "Jalen Smith", "Altura": 208, "Peso": 102, "PromedioPPP": 10.3, "Asistencias": 1.0, "Rebotes": 5.4},
    {"Nombre": "Isaiah Jackson", "Altura": 208, "Peso": 93, "PromedioPPP": 6.9, "Asistencias": 0.9, "Rebotes": 4.2},
    {"Nombre": "Jarace Walker", "Altura": 203, "Peso": 112, "PromedioPPP": 3.4, "Asistencias": 0.2, "Rebotes": 1.0},
    {"Nombre": "Myles Turner", "Altura": 210, "Peso": 113, "PromedioPPP": 17.6, "Asistencias": 1.2, "Rebotes": 7.3},
    {"Nombre": "Oscar Tshiebwe", "Altura": 205, "Peso": 117, "PromedioPPP": 2.8, "Asistencias": 0.5, "Rebotes": 1.0},
    #NewYork Knciks
    {"Nombre": "Ryan Arcidiacono", "Altura": 190, "Peso": 90, "PromedioPPP": 0.7, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Jalen Brunson", "Altura": 185, "Peso": 86, "PromedioPPP": 25.6, "Asistencias": 6.4, "Rebotes": 3.9},
    {"Nombre": "Malachi Flynn", "Altura": 185, "Peso": 83, "PromedioPPP": 0.7, "Asistencias": 0.3, "Rebotes": 0.3},
    {"Nombre": "Duane Washington Jr.", "Altura": 190, "Peso": 95, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Miles McBride", "Altura": 187, "Peso": 90, "PromedioPPP": 3.3, "Asistencias": 0.8, "Rebotes": 0.4},
    {"Nombre": "Evan Fournier", "Altura": 200, "Peso": 92, "PromedioPPP": 6.0, "Asistencias": 1.5, "Rebotes": 1.5},
    {"Nombre": "Josh Hart", "Altura": 195, "Peso": 97, "PromedioPPP": 7.4, "Asistencias": 2.8, "Rebotes": 6.3},
    {"Nombre": "Donte DiVincenzo", "Altura": 193, "Peso": 92, "PromedioPPP": 10.8, "Asistencias": 2.0, "Rebotes": 3.1},
    {"Nombre": "Charlie Brown", "Altura": 198, "Peso": 90, "PromedioPPP": 1.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Quentin Grimes", "Altura": 195, "Peso": 92, "PromedioPPP": 7.0, "Asistencias": 1.1, "Rebotes": 1.7},
    {"Nombre": "OG Anunoby", "Altura": 200, "Peso": 105, "PromedioPPP": 14.2, "Asistencias": 1.0, "Rebotes": 5.0},
    {"Nombre": "Jacob Toppin", "Altura": 205, "Peso": 92, "PromedioPPP": 0.0, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Julius Randle", "Altura": 203, "Peso": 113, "PromedioPPP": 24.2, "Asistencias": 4.8, "Rebotes": 9.3},
    {"Nombre": "Precious Achiuwa", "Altura": 205, "Peso": 102, "PromedioPPP": 2.6, "Asistencias": 0.4, "Rebotes": 3.6},
    {"Nombre": "Isaiah Hartenstein", "Altura": 213, "Peso": 112, "PromedioPPP": 6.6, "Asistencias": 1.8, "Rebotes": 7.7},
    {"Nombre": "Jericho Sims", "Altura": 208, "Peso": 111, "PromedioPPP": 1.3, "Asistencias": 0.2, "Rebotes": 1.4},
    {"Nombre": "Mitchell Robinson", "Altura": 213, "Peso": 101, "PromedioPPP": 6.2, "Asistencias": 10.3, "Rebotes": 5.0},
    #Minesota Timberwolves
    {"Nombre": "Mike Conley", "Altura": 185, "Peso": 79, "PromedioPPP": 11.2, "Asistencias": 6.3, "Rebotes": 2.7},
    {"Nombre": "Jordan McLaughlin", "Altura": 180, "Peso": 83, "PromedioPPP": 2.2, "Asistencias": 1.0, "Rebotes": 1.1},
    {"Nombre": "Shake Milton", "Altura": 195, "Peso": 92, "PromedioPPP": 5.1, "Asistencias": 1.3, "Rebotes": 1.4},
    {"Nombre": "Nickeil Alexander-Walker", "Altura": 195, "Peso": 92, "PromedioPPP": 6.3, "Asistencias": 2.4, "Rebotes": 1.7},
    {"Nombre": "Wendell Moore Jr.", "Altura": 195, "Peso": 96, "PromedioPPP": 1.1, "Asistencias": 0.0, "Rebotes": 0.4},
    {"Nombre": "Anthony Edwards", "Altura": 195, "Peso": 102, "PromedioPPP": 26.2, "Asistencias": 4.9, "Rebotes": 5.3},
    {"Nombre": "Jaylen Clark", "Altura": 195, "Peso": 92, "PromedioPPP": 2.3, "Asistencias": 0.3, "Rebotes": 1.8},
    {"Nombre": "Daishen Nix", "Altura": 195, "Peso": 101, "PromedioPPP": 1.3, "Asistencias": 0.0, "Rebotes": 0.2},
    {"Nombre": "Kyle Anderson", "Altura": 205, "Peso": 104, "PromedioPPP": 6.5, "Asistencias": 3.9, "Rebotes": 3.6},
    {"Nombre": "Troy Brown Jr.", "Altura": 198, "Peso": 97, "PromedioPPP": 4.5, "Asistencias": 0.9, "Rebotes": 2.1},
    {"Nombre": "Leonard Miller", "Altura": 208, "Peso": 95, "PromedioPPP": 2.3, "Asistencias": 0.3, "Rebotes": 1.8},
    {"Nombre": "Karl-Anthony Towns", "Altura": 210, "Peso": 112, "PromedioPPP": 21.7, "Asistencias": 3.0, "Rebotes": 8.9},
    {"Nombre": "Luka Garza", "Altura": 210, "Peso": 120, "PromedioPPP": 2.1, "Asistencias": 0.9, "Rebotes": 0.9},
    {"Nombre": "Jaden McDaniels", "Altura": 205, "Peso": 90, "PromedioPPP": 10.6, "Asistencias": 1.2, "Rebotes": 2.5},
    {"Nombre": "Josh Minott", "Altura": 203, "Peso": 92, "PromedioPPP": 1.7, "Asistencias": 0.2, "Rebotes": 0.1},
    {"Nombre": "Rudy Gobert", "Altura": 215, "Peso": 111, "PromedioPPP": 12.8, "Asistencias": 1.2, "Rebotes": 12.0},
    {"Nombre": "Naz Reid", "Altura": 205, "Peso": 113, "PromedioPPP": 12.7, "Asistencias": 1.0, "Rebotes": 4.8},
    #Ocklahoma City Thunder
      {"Nombre": "Vasilije Micic", "Altura": 198, "Peso": 91, "PromedioPPP": 2.9, "Asistencias": 3.0, "Rebotes": 0.7},
    {"Nombre": "Shai Gilgeous-Alexander", "Altura": 195, "Peso": 82, "PromedioPPP": 31.5, "Asistencias": 6.4, "Rebotes": 6.0},
    {"Nombre": "Cason Wallace", "Altura": 193, "Peso": 87, "PromedioPPP": 6.9, "Asistencias": 1.5, "Rebotes": 2.1},
    {"Nombre": "Lindy Waters III", "Altura": 198, "Peso": 97, "PromedioPPP": 3.2, "Asistencias": 0.5, "Rebotes": 0.8},
    {"Nombre": "Aaron Wiggins", "Altura": 198, "Peso": 90, "PromedioPPP": 5.2, "Asistencias": 0.8, "Rebotes": 2.4},
    {"Nombre": "Isaiah Joe", "Altura": 195, "Peso": 81, "PromedioPPP": 9.3, "Asistencias": 1.1, "Rebotes": 2.3},
    {"Nombre": "Luguentz Dort", "Altura": 190, "Peso": 97, "PromedioPPP": 11.0, "Asistencias": 1.4, "Rebotes": 4.0},
    {"Nombre": "Tre Mann", "Altura": 195, "Peso": 86, "PromedioPPP": 3.2, "Asistencias": 1.3, "Rebotes": 1.4},
    {"Nombre": "Josh Giddey", "Altura": 200, "Peso": 92, "PromedioPPP": 12.0, "Asistencias": 4.6, "Rebotes": 6.0},
    {"Nombre": "Kenrich Williams", "Altura": 198, "Peso": 95, "PromedioPPP": 4.5, "Asistencias": 1.7, "Rebotes": 2.7},
    {"Nombre": "Keyontae Johnson", "Altura": 198, "Peso": 104, "PromedioPPP": 0.9, "Asistencias": 0.7, "Rebotes": 1.1},
    {"Nombre": "Jalen Williams", "Altura": 198, "Peso": 88, "PromedioPPP": 18.2, "Asistencias": 4.2, "Rebotes": 3.9},
    {"Nombre": "Ousmane Dieng", "Altura": 200, "Peso": 97, "PromedioPPP": 4.3, "Asistencias": 0.9, "Rebotes": 1.6},
    {"Nombre": "Davis Bertans", "Altura": 208, "Peso": 102, "PromedioPPP": 3.4, "Asistencias": 0.7, "Rebotes": 0.8},
    {"Nombre": "Jaylin Williams", "Altura": 208, "Peso": 108, "PromedioPPP": 3.5, "Asistencias": 1.3, "Rebotes": 3.2},
    {"Nombre": "Aleksej Pokusevski", "Altura": 213, "Peso": 94, "PromedioPPP": 2.5, "Asistencias": 0.6, "Rebotes": 3.2},
    {"Nombre": "Chet Holmgren", "Altura": 213, "Peso": 88, "PromedioPPP": 17.8, "Asistencias": 2.7, "Rebotes": 7.3},
    {"Nombre": "Olivier Sarr", "Altura": 213, "Peso": 107, "PromedioPPP": 2.5, "Asistencias": 0.3, "Rebotes": 3.3},
    #Denver Nuggets
    {"Nombre": "Reggie Jackson", "Altura": 190, "Peso": 94, "PromedioPPP": 12.1, "Asistencias": 4.5, "Rebotes": 2.2},
    {"Nombre": "Jamal Murray", "Altura": 193, "Peso": 93, "PromedioPPP": 20.6, "Asistencias": 6.2, "Rebotes": 4.0},
    {"Nombre": "Collin Gillespie", "Altura": 190, "Peso": 88, "PromedioPPP": 1.7, "Asistencias": 0.7, "Rebotes": 0.3},
    {"Nombre": "Justin Holiday", "Altura": 198, "Peso": 82, "PromedioPPP": 4.0, "Asistencias": 1.0, "Rebotes": 1.4},
    {"Nombre": "Kentavious Caldwell-Pope", "Altura": 195, "Peso": 92, "PromedioPPP": 10.1, "Asistencias": 2.6, "Rebotes": 2.2},
    {"Nombre": "Jalen Pickett", "Altura": 193, "Peso": 94, "PromedioPPP": 2.1, "Asistencias": 0.7, "Rebotes": 0.7},
    {"Nombre": "Christian Braun", "Altura": 198, "Peso": 98, "PromedioPPP": 8.1, "Asistencias": 1.7, "Rebotes": 3.6},
    {"Nombre": "Julian Strawther", "Altura": 200, "Peso": 94, "PromedioPPP": 5.9, "Asistencias": 1.1, "Rebotes": 1.5},
    {"Nombre": "Michael Porter Jr.", "Altura": 208, "Peso": 95, "PromedioPPP": 16.3, "Asistencias": 1.4, "Rebotes": 7.2},
    {"Nombre": "Peyton Watson", "Altura": 203, "Peso": 90, "PromedioPPP": 7.1, "Asistencias": 1.0, "Rebotes": 2.7},
    {"Nombre": "Aaron Gordon", "Altura": 203, "Peso": 99, "PromedioPPP": 13.9, "Asistencias": 3.2, "Rebotes": 6.6},
    {"Nombre": "Braxton Key", "Altura": 203, "Peso": 104, "PromedioPPP": 1.2, "Asistencias": 0.6, "Rebotes": 0.8},
    {"Nombre": "Vlatko Cancar", "Altura": 203, "Peso": 95, "PromedioPPP": 0.3, "Asistencias": 0.0, "Rebotes": 0.0},
    {"Nombre": "Hunter Tyson", "Altura": 203, "Peso": 98, "PromedioPPP": 0.3, "Asistencias": 0.0, "Rebotes": 0.6},
    {"Nombre": "Zeke Nnaji", "Altura": 210, "Peso": 108, "PromedioPPP": 3.3, "Asistencias": 0.7, "Rebotes": 2.3},
    {"Nombre": "DeAndre Jordan", "Altura": 210, "Peso": 120, "PromedioPPP": 5.1, "Asistencias": 1.1, "Rebotes": 5.4},
    {"Nombre": "Nikola Jokic", "Altura": 213, "Peso": 113, "PromedioPPP": 25.5, "Asistencias": 9.2, "Rebotes": 11.8},
    {"Nombre": "Jay Huff", "Altura": 215, "Peso": 108, "PromedioPPP": 0.7, "Asistencias": 0.0, "Rebotes": 0.0},
    #LA Clippers
    {"Nombre": "Kawhi Leonard", "Altura": 200, "Peso": 104, "PromedioPPP": 23.8, "Asistencias": 3.4, "Rebotes": 6.1},
    {"Nombre": "Paul George", "Altura": 203, "Peso": 99, "PromedioPPP": 23.2, "Asistencias": 3.7, "Rebotes": 5.6},
    {"Nombre": "James Harden", "Altura": 195, "Peso": 99, "PromedioPPP": 17.4, "Asistencias": 8.4, "Rebotes": 4.8},
    {"Nombre": "Norman Powell", "Altura": 190, "Peso": 97, "PromedioPPP": 13.4, "Asistencias": 1.0, "Rebotes": 2.3},
    {"Nombre": "Ivica Zubac", "Altura": 213, "Peso": 108, "PromedioPPP": 12.6, "Asistencias": 1.3, "Rebotes": 9.7},
    {"Nombre": "Russell Westbrook", "Altura": 190, "Peso": 90, "PromedioPPP": 10.9, "Asistencias": 4.6, "Rebotes": 6.1},
    {"Nombre": "Bones Hyland", "Altura": 190, "Peso": 78, "PromedioPPP": 7.1, "Asistencias": 1.8, "Rebotes": 0.9},
    {"Nombre": "Terance Mann", "Altura": 195, "Peso": 97, "PromedioPPP": 7.1, "Asistencias": 1.9, "Rebotes": 3.2},
    {"Nombre": "Daniel Theis", "Altura": 203, "Peso": 110, "PromedioPPP": 6.8, "Asistencias": 0.8, "Rebotes": 3.5},
    {"Nombre": "Brandon Boston Jr.", "Altura": 200, "Peso": 83, "PromedioPPP": 5.1, "Asistencias": 1.1, "Rebotes": 1.1},
    {"Nombre": "KJ Martin", "Altura": 203, "Peso": 100, "PromedioPPP": 5.0, "Asistencias": 0.5, "Rebotes": 1.5},
    {"Nombre": "Mason Plumlee", "Altura": 211, "Peso": 106, "PromedioPPP": 4.9, "Asistencias": 1.1, "Rebotes": 4.6},
    {"Nombre": "Amir Coffey", "Altura": 200, "Peso": 95, "PromedioPPP": 4.0, "Asistencias": 0.7, "Rebotes": 1.6},
    {"Nombre": "Robert Covington", "Altura": 206, "Peso": 102, "PromedioPPP": 3.0, "Asistencias": 2.3, "Rebotes": "INF"},
    {"Nombre": "Moussa Diabate", "Altura": 210, "Peso": 95, "PromedioPPP": 2.7, "Asistencias": 2.3, "Rebotes": 5.0},
    {"Nombre": "Nicolas Batum", "Altura": 203, "Peso": 90, "PromedioPPP": 2.7, "Asistencias": 1.7, "Rebotes": 3.5},
    {"Nombre": "Kobe Brown", "Altura": 201, "Peso": 102, "PromedioPPP": 2.3, "Asistencias": 0.2, "Rebotes": 1.3},
    {"Nombre": "Joshua Primo", "Altura": 198, "Peso": 86, "PromedioPPP": 2.0, "Asistencias": 0.3, "Rebotes": 2.3},
    {"Nombre": "Jordan Miller", "Altura": 200, "Peso": 88, "PromedioPPP": 1.7, "Asistencias": 0.2, "Rebotes": 0.0},
    {"Nombre": "P.J. Tucker", "Altura": 195, "Peso": 111, "PromedioPPP": 1.2, "Asistencias": 0.2, "Rebotes": 2.4},
    {"Nombre": "Xavier Moon", "Altura": 187, "Peso": 86, "PromedioPPP": 1.0, "Asistencias": 1.5, "Rebotes": 3.0},
]"""

with open ("datos.json","r") as file:
    jugadores = json.loads(file.read())

# Solicitar al usuario el nombre del jugador
nombre_jugador = input("Ingrese el nombre del jugador: ")

# Buscar al jugador por nombre
jugador_encontrado = next((jugador for jugador in jugadores if jugador["Nombre"] == nombre_jugador), None)

# Validar si se encontró al jugador
if jugador_encontrado:
    # Definir criterios para clasificar a los jugadores en posiciones
    def clasificar_posicion(jugador):
        if (jugador["Altura"] > 210 and jugador["Peso"] > 110 and jugador["Rebotes"] > 15):
           return "Super-Pívot"
        elif (jugador["Asistencias"] > 20):
            return "Pulpo"
        elif (jugador["PromedioPPP"] > 30 and jugador["Asistencias"] < 3 and jugador["Rebotes"] < 3 ):
            return "Francotirador"
        elif (jugador["Altura"] > 200 and jugador["Peso"] > 90 and jugador["PromedioPPP"] > 15) or (jugador["Asistencias"] > 5 and jugador["Rebotes"] > 10):
            return "Pívot"
        elif (jugador["Altura"] > 190 and jugador["PromedioPPP"] > 10) or (jugador["Asistencias"] > 3 and jugador["Rebotes"] > 8):
            return "Ala-Pívot"
        elif (jugador["Altura"] > 180 and jugador["PromedioPPP"] > 8) or (jugador["Asistencias"] > 2 and jugador["Rebotes"] > 5):
            return "Alero"
        elif (jugador["PromedioPPP"] > 12) or (jugador["Asistencias"] > 4 and jugador["Rebotes"] > 3):
            return "Escolta"
        elif (jugador["PromedioPPP"] < 4 and jugador["Asistencias"] < 3 and jugador["Rebotes"] < 3 ):
            return "Banquillo"
        elif (jugador["PromedioPPP"] > 30 and jugador["Asistencias"] > 10 and jugador["Rebotes"] > 10 ):
            return "PUEDE JUGAR DE LO QUE QUIERA, ES UNA ESTRELLA"
        else:
            return "Base"
    
    # Clasificar al jugador y mostrar la posición
    posicion = clasificar_posicion(jugador_encontrado)
    print(f"{jugador_encontrado['Nombre']}: {posicion}")
else:
    print(f"No se encontró información para el jugador {nombre_jugador}.")
