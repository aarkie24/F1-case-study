"""
Data Collection & Generation Script for F1 Global Baseline (2010-2019)
Generates data/raw/f1_races_raw.csv containing all 198 historical Formula 1 Grand Prix races
with sporting parameters, circuit metrics, race attendance figures, and macroeconomic indicators.
"""

import os
import pandas as pd
import numpy as np

# Ensure data directories exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("notebooks", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("sources", exist_ok=True)

# Master Circuit Database with historical parameters
CIRCUITS = {
    "albert_park": {
        "circuit_id": "albert_park", "name": "Albert Park Grand Prix Circuit", "locality": "Melbourne",
        "country": "Australia", "continent": "Oceania", "circuit_type": "Hybrid", "length_km": 5.303,
        "gdp_per_capita": {2010: 52022, 2011: 62518, 2012: 67677, 2013: 67792, 2014: 62215, 2015: 56561, 2016: 49971, 2017: 54066, 2018: 57355, 2019: 55060},
        "inaugural_year": 1996, "base_attendance": 100000, "weekend_mult": 3.1
    },
    "sepang": {
        "circuit_id": "sepang", "name": "Sepang International Circuit", "locality": "Kuala Lumpur",
        "country": "Malaysia", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.543,
        "gdp_per_capita": {2010: 9069, 2011: 10433, 2012: 10791, 2013: 10830, 2014: 11184, 2015: 9643, 2016: 9508, 2017: 9952, 2018: 11124, 2019: 11414},
        "inaugural_year": 1999, "base_attendance": 65000, "weekend_mult": 1.7
    },
    "shanghai": {
        "circuit_id": "shanghai", "name": "Shanghai International Circuit", "locality": "Shanghai",
        "country": "China", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.451,
        "gdp_per_capita": {2010: 4550, 2011: 5618, 2012: 6317, 2013: 7051, 2014: 7679, 2015: 8069, 2016: 8148, 2017: 8879, 2018: 9977, 2019: 10217},
        "inaugural_year": 2004, "base_attendance": 55000, "weekend_mult": 2.5
    },
    "bahrain": {
        "circuit_id": "bahrain", "name": "Bahrain International Circuit", "locality": "Sakhir",
        "country": "Bahrain", "continent": "Middle East", "circuit_type": "Permanent", "length_km": 5.412,
        "gdp_per_capita": {2010: 20722, 2011: 22519, 2012: 23654, 2013: 24737, 2014: 24982, 2015: 22634, 2016: 22615, 2017: 23743, 2018: 24022, 2019: 23504},
        "inaugural_year": 2004, "base_attendance": 32000, "weekend_mult": 2.8
    },
    "catalunya": {
        "circuit_id": "catalunya", "name": "Circuit de Barcelona-Catalunya", "locality": "Montmeló",
        "country": "Spain", "continent": "Europe", "circuit_type": "Permanent", "length_km": 4.655,
        "gdp_per_capita": {2010: 30737, 2011: 31835, 2012: 28562, 2013: 29210, 2014: 29623, 2015: 25754, 2016: 26523, 2017: 28170, 2018: 30371, 2019: 29565},
        "inaugural_year": 1991, "base_attendance": 85000, "weekend_mult": 1.9
    },
    "monaco": {
        "circuit_id": "monaco", "name": "Circuit de Monaco", "locality": "Monte-Carlo",
        "country": "Monaco", "continent": "Europe", "circuit_type": "Street", "length_km": 3.337,
        "gdp_per_capita": {2010: 153000, 2011: 168000, 2012: 163000, 2013: 173000, 2014: 185000, 2015: 166000, 2016: 169000, 2017: 180000, 2018: 190000, 2019: 195000},
        "inaugural_year": 1950, "base_attendance": 60000, "weekend_mult": 3.3
    },
    "istanbul": {
        "circuit_id": "istanbul", "name": "Istanbul Park", "locality": "Istanbul",
        "country": "Turkey", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.338,
        "gdp_per_capita": {2010: 10672, 2011: 11341, 2012: 11720, 2013: 12615, 2014: 12158, 2015: 10988, 2016: 10863, 2017: 10590, 2018: 9454, 2019: 9127},
        "inaugural_year": 2005, "base_attendance": 38000, "weekend_mult": 1.8
    },
    "villeneuve": {
        "circuit_id": "villeneuve", "name": "Circuit Gilles Villeneuve", "locality": "Montreal",
        "country": "Canada", "continent": "Americas", "circuit_type": "Hybrid", "length_km": 4.361,
        "gdp_per_capita": {2010: 47447, 2011: 52082, 2012: 52497, 2013: 52414, 2014: 50443, 2015: 43316, 2016: 42158, 2017: 45039, 2018: 46233, 2019: 46195},
        "inaugural_year": 1978, "base_attendance": 105000, "weekend_mult": 2.9
    },
    "valencia": {
        "circuit_id": "valencia", "name": "Valencia Street Circuit", "locality": "Valencia",
        "country": "Spain", "continent": "Europe", "circuit_type": "Street", "length_km": 5.419,
        "gdp_per_capita": {2010: 30737, 2011: 31835, 2012: 28562, 2013: 29210, 2014: 29623, 2015: 25754, 2016: 26523, 2017: 28170, 2018: 30371, 2019: 29565},
        "inaugural_year": 2008, "base_attendance": 50000, "weekend_mult": 1.9
    },
    "silverstone": {
        "circuit_id": "silverstone", "name": "Silverstone Circuit", "locality": "Silverstone",
        "country": "United Kingdom", "continent": "Europe", "circuit_type": "Permanent", "length_km": 5.891,
        "gdp_per_capita": {2010: 39642, 2011: 41412, 2012: 41791, 2013: 42724, 2014: 46783, 2015: 44306, 2016: 40445, 2017: 40361, 2018: 43043, 2019: 42330},
        "inaugural_year": 1950, "base_attendance": 135000, "weekend_mult": 2.6
    },
    "hockenheimring": {
        "circuit_id": "hockenheimring", "name": "Hockenheimring", "locality": "Hockenheim",
        "country": "Germany", "continent": "Europe", "circuit_type": "Permanent", "length_km": 4.574,
        "gdp_per_capita": {2010: 41786, 2011: 45936, 2012: 44065, 2013: 46531, 2014: 47903, 2015: 41242, 2016: 42233, 2017: 44470, 2018: 47603, 2019: 46445},
        "inaugural_year": 1970, "base_attendance": 65000, "weekend_mult": 2.0
    },
    "nurburgring": {
        "circuit_id": "nurburgring", "name": "Nürburgring", "locality": "Nürburg",
        "country": "Germany", "continent": "Europe", "circuit_type": "Permanent", "length_km": 5.148,
        "gdp_per_capita": {2010: 41786, 2011: 45936, 2012: 44065, 2013: 46531, 2014: 47903, 2015: 41242, 2016: 42233, 2017: 44470, 2018: 47603, 2019: 46445},
        "inaugural_year": 1951, "base_attendance": 55000, "weekend_mult": 2.0
    },
    "hungaroring": {
        "circuit_id": "hungaroring", "name": "Hungaroring", "locality": "Mogyoród",
        "country": "Hungary", "continent": "Europe", "circuit_type": "Permanent", "length_km": 4.381,
        "gdp_per_capita": {2010: 13092, 2011: 14078, 2012: 12845, 2013: 13600, 2014: 14169, 2015: 12470, 2016: 12882, 2017: 14352, 2018: 16186, 2019: 16732},
        "inaugural_year": 1986, "base_attendance": 75000, "weekend_mult": 2.7
    },
    "spa": {
        "circuit_id": "spa", "name": "Circuit de Spa-Francorchamps", "locality": "Stavelot",
        "country": "Belgium", "continent": "Europe", "circuit_type": "Permanent", "length_km": 7.004,
        "gdp_per_capita": {2010: 44360, 2011: 47710, 2012: 44741, 2013: 46543, 2014: 47343, 2015: 40367, 2016: 41261, 2017: 43339, 2018: 46582, 2019: 46163},
        "inaugural_year": 1950, "base_attendance": 85000, "weekend_mult": 2.8
    },
    "monza": {
        "circuit_id": "monza", "name": "Autodromo Nazionale di Monza", "locality": "Monza",
        "country": "Italy", "continent": "Europe", "circuit_type": "Permanent", "length_km": 5.793,
        "gdp_per_capita": {2010: 35849, 2011: 38335, 2012: 34814, 2013: 35370, 2014: 35397, 2015: 30442, 2016: 30939, 2017: 32327, 2018: 34483, 2019: 33567},
        "inaugural_year": 1950, "base_attendance": 85000, "weekend_mult": 2.1
    },
    "marina_bay": {
        "circuit_id": "marina_bay", "name": "Marina Bay Street Circuit", "locality": "Marina Bay",
        "country": "Singapore", "continent": "Asia", "circuit_type": "Street", "length_km": 5.065,
        "gdp_per_capita": {2010: 47237, 2011: 53890, 2012: 55546, 2013: 56906, 2014: 57560, 2015: 55646, 2016: 56896, 2017: 61176, 2018: 66679, 2019: 65233},
        "inaugural_year": 2008, "base_attendance": 85000, "weekend_mult": 3.1
    },
    "suzuka": {
        "circuit_id": "suzuka", "name": "Suzuka International Racing Course", "locality": "Suzuka",
        "country": "Japan", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.807,
        "gdp_per_capita": {2010: 44508, 2011: 48168, 2012: 48603, 2013: 40454, 2014: 38109, 2015: 34524, 2016: 39213, 2017: 38428, 2018: 39159, 2019: 40113},
        "inaugural_year": 1987, "base_attendance": 90000, "weekend_mult": 2.2
    },
    "yeongam": {
        "circuit_id": "yeongam", "name": "Korea International Circuit", "locality": "Yeongam",
        "country": "South Korea", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.615,
        "gdp_per_capita": {2010: 23087, 2011: 25100, 2012: 25467, 2013: 27179, 2014: 29253, 2015: 28732, 2016: 29289, 2017: 31605, 2018: 33423, 2019: 31846},
        "inaugural_year": 2010, "base_attendance": 50000, "weekend_mult": 1.9
    },
    "buddh": {
        "circuit_id": "buddh", "name": "Buddh International Circuit", "locality": "Greater Noida",
        "country": "India", "continent": "Asia", "circuit_type": "Permanent", "length_km": 5.125,
        "gdp_per_capita": {2010: 1345, 2011: 1458, 2012: 1443, 2013: 1449, 2014: 1573, 2015: 1605, 2016: 1729, 2017: 1980, 2018: 1997, 2019: 2100},
        "inaugural_year": 2011, "base_attendance": 95000, "weekend_mult": 1.2
    },
    "interlagos": {
        "circuit_id": "interlagos", "name": "Autódromo José Carlos Pace", "locality": "São Paulo",
        "country": "Brazil", "continent": "Americas", "circuit_type": "Permanent", "length_km": 4.309,
        "gdp_per_capita": {2010: 11286, 2011: 13245, 2012: 12370, 2013: 12300, 2014: 12112, 2015: 8814, 2016: 8712, 2017: 9924, 2018: 9151, 2019: 8897},
        "inaugural_year": 1973, "base_attendance": 70000, "weekend_mult": 2.1
    },
    "yas_marina": {
        "circuit_id": "yas_marina", "name": "Yas Marina Circuit", "locality": "Abu Dhabi",
        "country": "United Arab Emirates", "continent": "Middle East", "circuit_type": "Permanent", "length_km": 5.554,
        "gdp_per_capita": {2010: 35038, 2011: 40434, 2012: 42076, 2013: 43312, 2014: 44443, 2015: 39122, 2016: 38141, 2017: 40649, 2018: 43839, 2019: 42701},
        "inaugural_year": 2009, "base_attendance": 55000, "weekend_mult": 2.4
    },
    "americas": {
        "circuit_id": "americas", "name": "Circuit of the Americas", "locality": "Austin",
        "country": "United States", "continent": "Americas", "circuit_type": "Permanent", "length_km": 5.513,
        "gdp_per_capita": {2010: 48466, 2011: 49883, 2012: 51603, 2013: 53107, 2014: 55033, 2015: 56803, 2016: 57904, 2017: 59928, 2018: 62805, 2019: 65095},
        "inaugural_year": 2012, "base_attendance": 105000, "weekend_mult": 2.6
    },
    "red_bull_ring": {
        "circuit_id": "red_bull_ring", "name": "Red Bull Ring", "locality": "Spielberg",
        "country": "Austria", "continent": "Europe", "circuit_type": "Permanent", "length_km": 4.318,
        "gdp_per_capita": {2010: 46858, 2011: 51786, 2012: 48567, 2013: 50716, 2014: 51717, 2015: 44178, 2016: 45277, 2017: 47429, 2018: 51462, 2019: 50138},
        "inaugural_year": 1970, "base_attendance": 85000, "weekend_mult": 2.3
    },
    "sochi": {
        "circuit_id": "sochi", "name": "Sochi Autodrom", "locality": "Sochi",
        "country": "Russia", "continent": "Europe", "circuit_type": "Permanent", "length_km": 5.848,
        "gdp_per_capita": {2010: 10675, 2011: 14351, 2012: 15435, 2013: 15975, 2014: 14126, 2015: 9329, 2016: 8705, 2017: 10720, 2018: 11289, 2019: 11498},
        "inaugural_year": 2014, "base_attendance": 55000, "weekend_mult": 2.6
    },
    "rodriguez": {
        "circuit_id": "rodriguez", "name": "Autódromo Hermanos Rodríguez", "locality": "Mexico City",
        "country": "Mexico", "continent": "Americas", "circuit_type": "Permanent", "length_km": 4.304,
        "gdp_per_capita": {2010: 9271, 2011: 10203, 2012: 10242, 2013: 10725, 2014: 10929, 2015: 9617, 2016: 8745, 2017: 9288, 2018: 9687, 2019: 9950},
        "inaugural_year": 1963, "base_attendance": 130000, "weekend_mult": 2.6
    },
    "baku": {
        "circuit_id": "baku", "name": "Baku City Circuit", "locality": "Baku",
        "country": "Azerbaijan", "continent": "Asia", "circuit_type": "Street", "length_km": 6.003,
        "gdp_per_capita": {2010: 5843, 2011: 7189, 2012: 7496, 2013: 7876, 2014: 7891, 2015: 5500, 2016: 3881, 2017: 4147, 2018: 4721, 2019: 4794},
        "inaugural_year": 2016, "base_attendance": 30000, "weekend_mult": 2.5
    },
    "ricard": {
        "circuit_id": "ricard", "name": "Circuit Paul Ricard", "locality": "Le Castellet",
        "country": "France", "continent": "Europe", "circuit_type": "Permanent", "length_km": 5.842,
        "gdp_per_capita": {2010: 40703, 2011: 43810, 2012: 40838, 2013: 42593, 2014: 43011, 2015: 36613, 2016: 36870, 2017: 38699, 2018: 41464, 2019: 40494},
        "inaugural_year": 1971, "base_attendance": 65000, "weekend_mult": 2.3
    }
}

# Grand Prix calendars by season (2010 - 2019)
SEASON_RACES = {
    2010: [
        ("Bahrain Grand Prix", "bahrain", 49, "2010-03-14", "Fernando Alonso", "Ferrari", 99.3, 195.8, 118.3, 16.1, 16, 8, 38, 30000),
        ("Australian Grand Prix", "albert_park", 58, "2010-03-28", "Jenson Button", "McLaren", 93.6, 196.9, 88.4, 12.0, 14, 10, 52, 108000),
        ("Malaysian Grand Prix", "sepang", 56, "2010-04-04", "Sebastian Vettel", "Red Bull", 93.8, 198.5, 97.1, 4.8, 17, 7, 34, 62000),
        ("Chinese Grand Prix", "shanghai", 56, "2010-04-18", "Jenson Button", "McLaren", 106.7, 171.6, 102.1, 1.5, 17, 7, 65, 50000),
        ("Spanish Grand Prix", "catalunya", 66, "2010-05-09", "Mark Webber", "Red Bull", 95.9, 192.1, 84.4, 24.1, 16, 8, 32, 92000),
        ("Monaco Grand Prix", "monaco", 78, "2010-05-16", "Mark Webber", "Red Bull", 110.1, 141.8, 75.2, 0.4, 15, 9, 28, 62000),
        ("Turkish Grand Prix", "istanbul", 58, "2010-05-30", "Lewis Hamilton", "McLaren", 88.6, 209.6, 86.3, 2.6, 18, 6, 36, 36000),
        ("Canadian Grand Prix", "villeneuve", 70, "2010-06-13", "Lewis Hamilton", "McLaren", 93.9, 195.1, 76.9, 2.3, 17, 7, 61, 102000),
        ("European Grand Prix", "valencia", 57, "2010-06-27", "Sebastian Vettel", "Red Bull", 100.4, 184.6, 98.8, 5.0, 20, 4, 39, 45000),
        ("British Grand Prix", "silverstone", 52, "2010-07-11", "Mark Webber", "Red Bull", 84.6, 216.9, 90.9, 1.4, 19, 5, 33, 115000),
        ("German Grand Prix", "hockenheimring", 67, "2010-07-25", "Fernando Alonso", "Ferrari", 87.6, 209.9, 75.9, 4.2, 19, 5, 38, 65000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2010-08-01", "Mark Webber", "Red Bull", 101.1, 181.9, 82.4, 17.8, 17, 7, 35, 70000),
        ("Belgian Grand Prix", "spa", 44, "2010-08-29", "Lewis Hamilton", "McLaren", 89.1, 207.7, 109.1, 1.6, 17, 7, 54, 75000),
        ("Italian Grand Prix", "monza", 53, "2010-09-12", "Fernando Alonso", "Ferrari", 76.4, 241.5, 84.1, 3.4, 18, 6, 29, 82000),
        ("Singapore Grand Prix", "marina_bay", 61, "2010-09-26", "Fernando Alonso", "Ferrari", 117.9, 157.2, 108.0, 0.3, 17, 7, 30, 83000),
        ("Japanese Grand Prix", "suzuka", 53, "2010-10-10", "Sebastian Vettel", "Red Bull", 90.5, 203.9, 93.5, 0.9, 16, 8, 26, 96000),
        ("Korean Grand Prix", "yeongam", 55, "2010-10-24", "Fernando Alonso", "Ferrari", 178.6, 103.8, 110.2, 15.0, 15, 9, 48, 80000),
        ("Brazilian Grand Prix", "interlagos", 71, "2010-11-07", "Sebastian Vettel", "Red Bull", 92.2, 198.8, 73.9, 4.2, 19, 5, 34, 72000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2010-11-14", "Sebastian Vettel", "Red Bull", 99.6, 184.0, 101.3, 10.2, 18, 6, 31, 50000)
    ],
    2011: [
        ("Australian Grand Prix", "albert_park", 58, "2011-03-27", "Sebastian Vettel", "Red Bull", 89.5, 205.8, 89.8, 22.3, 14, 8, 44, 111000),
        ("Malaysian Grand Prix", "sepang", 56, "2011-04-10", "Sebastian Vettel", "Red Bull", 97.6, 190.8, 100.6, 3.3, 17, 7, 58, 65000),
        ("Chinese Grand Prix", "shanghai", 56, "2011-04-17", "Lewis Hamilton", "McLaren", 96.9, 188.9, 99.8, 5.2, 18, 6, 67, 52000),
        ("Turkish Grand Prix", "istanbul", 58, "2011-05-08", "Sebastian Vettel", "Red Bull", 90.3, 205.7, 89.7, 8.8, 21, 3, 82, 32000),
        ("Spanish Grand Prix", "catalunya", 66, "2011-05-22", "Sebastian Vettel", "Red Bull", 99.1, 186.0, 86.7, 0.6, 18, 6, 76, 78000),
        ("Monaco Grand Prix", "monaco", 78, "2011-05-29", "Sebastian Vettel", "Red Bull", 129.6, 120.6, 76.2, 1.1, 15, 9, 36, 60000),
        ("Canadian Grand Prix", "villeneuve", 70, "2011-06-12", "Jenson Button", "McLaren", 244.7, 74.9, 73.1, 2.7, 17, 7, 79, 104000),
        ("European Grand Prix", "valencia", 57, "2011-06-26", "Sebastian Vettel", "Red Bull", 99.6, 186.1, 101.9, 10.9, 24, 0, 56, 40000),
        ("British Grand Prix", "silverstone", 52, "2011-07-10", "Fernando Alonso", "Ferrari", 88.8, 206.6, 94.9, 16.5, 17, 7, 63, 122000),
        ("German Grand Prix", "nurburgring", 60, "2011-07-24", "Lewis Hamilton", "McLaren", 97.5, 190.1, 94.4, 4.0, 18, 6, 60, 52000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2011-07-31", "Jenson Button", "McLaren", 106.7, 172.5, 83.4, 3.6, 19, 5, 84, 72000),
        ("Belgian Grand Prix", "spa", 44, "2011-08-28", "Sebastian Vettel", "Red Bull", 86.7, 213.3, 109.9, 3.7, 18, 6, 63, 76000),
        ("Italian Grand Prix", "monza", 53, "2011-09-11", "Sebastian Vettel", "Red Bull", 74.8, 246.6, 86.1, 9.6, 15, 9, 35, 78000),
        ("Singapore Grand Prix", "marina_bay", 61, "2011-09-25", "Sebastian Vettel", "Red Bull", 119.1, 155.7, 108.5, 1.7, 17, 7, 59, 82000),
        ("Japanese Grand Prix", "suzuka", 53, "2011-10-09", "Jenson Button", "McLaren", 90.9, 203.2, 96.6, 1.2, 19, 5, 58, 102000),
        ("Korean Grand Prix", "yeongam", 55, "2011-10-16", "Sebastian Vettel", "Red Bull", 98.0, 188.7, 99.6, 12.0, 19, 5, 52, 60000),
        ("Indian Grand Prix", "buddh", 60, "2011-10-30", "Sebastian Vettel", "Red Bull", 90.6, 204.0, 87.2, 8.4, 17, 7, 54, 95000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2011-11-13", "Lewis Hamilton", "McLaren", 99.6, 184.1, 102.6, 8.5, 19, 5, 49, 50000),
        ("Brazilian Grand Prix", "interlagos", 71, "2011-11-27", "Mark Webber", "Red Bull", 92.3, 198.8, 75.3, 17.0, 19, 5, 48, 70000)
    ],
    2012: [
        ("Australian Grand Prix", "albert_park", 58, "2012-03-18", "Jenson Button", "McLaren", 94.1, 195.8, 89.2, 2.1, 16, 8, 41, 114000),
        ("Malaysian Grand Prix", "sepang", 56, "2012-03-25", "Fernando Alonso", "Ferrari", 164.9, 112.9, 100.7, 2.2, 18, 6, 73, 63000),
        ("Chinese Grand Prix", "shanghai", 56, "2012-04-15", "Nico Rosberg", "Mercedes", 96.4, 189.9, 100.0, 20.6, 22, 2, 53, 54000),
        ("Bahrain Grand Prix", "bahrain", 57, "2012-04-22", "Sebastian Vettel", "Red Bull", 95.2, 194.5, 96.4, 3.3, 21, 3, 64, 28000),
        ("Spanish Grand Prix", "catalunya", 66, "2012-05-13", "Pastor Maldonado", "Williams", 99.2, 185.8, 86.3, 3.2, 19, 5, 56, 82000),
        ("Monaco Grand Prix", "monaco", 78, "2012-05-27", "Mark Webber", "Red Bull", 106.1, 147.3, 77.3, 0.6, 15, 9, 29, 61000),
        ("Canadian Grand Prix", "villeneuve", 70, "2012-06-10", "Lewis Hamilton", "McLaren", 92.5, 198.0, 73.7, 2.5, 19, 5, 38, 107000),
        ("European Grand Prix", "valencia", 57, "2012-06-24", "Fernando Alonso", "Ferrari", 104.3, 177.7, 102.2, 6.4, 15, 9, 39, 41000),
        ("British Grand Prix", "silverstone", 52, "2012-07-08", "Mark Webber", "Red Bull", 85.3, 215.1, 94.7, 3.0, 20, 4, 45, 127000),
        ("German Grand Prix", "hockenheimring", 67, "2012-07-22", "Fernando Alonso", "Ferrari", 91.1, 201.8, 78.7, 3.7, 21, 3, 51, 58000),
        ("Hungarian Grand Prix", "hungaroring", 69, "2012-07-29", "Lewis Hamilton", "McLaren", 101.1, 179.3, 84.1, 1.0, 20, 4, 49, 74000),
        ("Belgian Grand Prix", "spa", 44, "2012-09-02", "Jenson Button", "McLaren", 89.1, 207.6, 112.8, 13.6, 18, 6, 29, 78000),
        ("Italian Grand Prix", "monza", 53, "2012-09-09", "Lewis Hamilton", "McLaren", 79.7, 230.9, 87.2, 4.4, 17, 7, 31, 84000),
        ("Singapore Grand Prix", "marina_bay", 59, "2012-09-23", "Sebastian Vettel", "Red Bull", 120.4, 148.9, 111.1, 8.9, 16, 8, 38, 85000),
        ("Japanese Grand Prix", "suzuka", 53, "2012-10-07", "Sebastian Vettel", "Red Bull", 88.9, 207.5, 95.8, 20.6, 19, 5, 34, 103000),
        ("Korean Grand Prix", "yeongam", 55, "2012-10-14", "Sebastian Vettel", "Red Bull", 96.4, 191.9, 102.1, 8.2, 20, 4, 44, 45000),
        ("Indian Grand Prix", "buddh", 60, "2012-10-28", "Sebastian Vettel", "Red Bull", 91.2, 202.4, 88.2, 9.4, 19, 5, 30, 65000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2012-11-04", "Kimi Räikkönen", "Lotus", 106.0, 172.9, 103.9, 0.9, 17, 7, 34, 52000),
        ("United States Grand Prix", "americas", 56, "2012-11-18", "Lewis Hamilton", "McLaren", 95.9, 193.1, 99.4, 0.7, 21, 3, 27, 117000),
        ("Brazilian Grand Prix", "interlagos", 71, "2012-11-25", "Jenson Button", "McLaren", 105.4, 173.8, 78.1, 2.7, 18, 6, 68, 71000)
    ],
    2013: [
        ("Australian Grand Prix", "albert_park", 58, "2013-03-17", "Kimi Räikkönen", "Lotus", 90.0, 204.9, 89.3, 12.5, 18, 4, 49, 103000),
        ("Malaysian Grand Prix", "sepang", 56, "2013-03-24", "Sebastian Vettel", "Red Bull", 98.9, 188.3, 99.2, 4.3, 17, 5, 75, 61000),
        ("Chinese Grand Prix", "shanghai", 56, "2013-04-14", "Fernando Alonso", "Ferrari", 96.5, 189.7, 100.8, 10.2, 18, 4, 62, 53000),
        ("Bahrain Grand Prix", "bahrain", 57, "2013-04-21", "Sebastian Vettel", "Red Bull", 96.0, 192.9, 96.9, 9.1, 20, 2, 69, 28000),
        ("Spanish Grand Prix", "catalunya", 66, "2013-05-12", "Fernando Alonso", "Ferrari", 99.3, 185.7, 86.3, 9.3, 18, 4, 78, 80000),
        ("Monaco Grand Prix", "monaco", 78, "2013-05-26", "Nico Rosberg", "Mercedes", 137.9, 113.4, 76.6, 3.9, 15, 7, 34, 60000),
        ("Canadian Grand Prix", "villeneuve", 70, "2013-06-09", "Sebastian Vettel", "Red Bull", 92.2, 198.7, 76.2, 14.4, 17, 5, 41, 106000),
        ("British Grand Prix", "silverstone", 52, "2013-06-30", "Nico Rosberg", "Mercedes", 92.9, 197.6, 93.4, 0.8, 17, 5, 52, 120000),
        ("German Grand Prix", "nurburgring", 60, "2013-07-07", "Sebastian Vettel", "Red Bull", 101.2, 183.1, 93.4, 1.0, 18, 4, 57, 45000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2013-07-28", "Lewis Hamilton", "Mercedes", 102.4, 179.5, 84.1, 10.9, 17, 5, 55, 72000),
        ("Belgian Grand Prix", "spa", 44, "2013-08-25", "Sebastian Vettel", "Red Bull", 83.7, 220.8, 110.8, 16.9, 18, 4, 38, 75000),
        ("Italian Grand Prix", "monza", 53, "2013-09-08", "Sebastian Vettel", "Red Bull", 78.6, 234.3, 85.8, 5.5, 19, 3, 27, 75000),
        ("Singapore Grand Prix", "marina_bay", 61, "2013-09-22", "Sebastian Vettel", "Red Bull", 119.2, 155.5, 108.6, 32.6, 17, 5, 38, 86000),
        ("Korean Grand Prix", "yeongam", 55, "2013-10-06", "Sebastian Vettel", "Red Bull", 103.2, 179.2, 101.4, 4.2, 16, 6, 42, 40000),
        ("Japanese Grand Prix", "suzuka", 53, "2013-10-13", "Sebastian Vettel", "Red Bull", 86.8, 212.5, 94.6, 7.1, 18, 4, 43, 89000),
        ("Indian Grand Prix", "buddh", 60, "2013-10-27", "Sebastian Vettel", "Red Bull", 91.2, 202.4, 87.7, 29.8, 17, 5, 36, 60000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2013-11-03", "Sebastian Vettel", "Red Bull", 98.1, 186.9, 103.4, 30.8, 20, 2, 35, 50000),
        ("United States Grand Prix", "americas", 56, "2013-11-17", "Sebastian Vettel", "Red Bull", 92.7, 199.7, 99.9, 6.3, 20, 2, 24, 113000),
        ("Brazilian Grand Prix", "interlagos", 71, "2013-11-24", "Sebastian Vettel", "Red Bull", 92.6, 197.8, 79.0, 10.5, 17, 5, 38, 70000)
    ],
    2014: [
        ("Australian Grand Prix", "albert_park", 57, "2014-03-16", "Nico Rosberg", "Mercedes", 92.9, 195.1, 92.5, 26.8, 14, 8, 30, 101000),
        ("Malaysian Grand Prix", "sepang", 56, "2014-03-30", "Lewis Hamilton", "Mercedes", 100.4, 185.5, 103.1, 17.3, 15, 7, 47, 58000),
        ("Bahrain Grand Prix", "bahrain", 57, "2014-04-06", "Lewis Hamilton", "Mercedes", 99.7, 185.7, 97.0, 1.1, 17, 5, 42, 31000),
        ("Chinese Grand Prix", "shanghai", 54, "2014-04-20", "Lewis Hamilton", "Mercedes", 93.5, 188.7, 100.4, 18.0, 18, 4, 36, 54000),
        ("Spanish Grand Prix", "catalunya", 66, "2014-05-11", "Lewis Hamilton", "Mercedes", 101.1, 182.4, 88.9, 0.6, 18, 4, 46, 84000),
        ("Monaco Grand Prix", "monaco", 78, "2014-05-25", "Nico Rosberg", "Mercedes", 109.3, 142.8, 78.5, 9.2, 14, 8, 23, 62000),
        ("Canadian Grand Prix", "villeneuve", 70, "2014-06-08", "Daniel Ricciardo", "Red Bull", 99.2, 184.6, 78.5, 4.2, 11, 11, 33, 110000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2014-06-22", "Nico Rosberg", "Mercedes", 87.9, 209.3, 72.2, 1.9, 18, 4, 39, 90000),
        ("British Grand Prix", "silverstone", 52, "2014-07-06", "Lewis Hamilton", "Mercedes", 146.9, 125.0, 97.2, 30.1, 14, 8, 30, 120000),
        ("German Grand Prix", "hockenheimring", 67, "2014-07-20", "Nico Rosberg", "Mercedes", 93.7, 196.2, 79.9, 20.8, 16, 6, 44, 52000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2014-07-27", "Daniel Ricciardo", "Red Bull", 113.1, 162.6, 85.7, 5.2, 16, 6, 46, 75000),
        ("Belgian Grand Prix", "spa", 44, "2014-08-24", "Daniel Ricciardo", "Red Bull", 84.6, 218.4, 110.5, 3.4, 18, 4, 39, 80000),
        ("Italian Grand Prix", "monza", 53, "2014-09-07", "Lewis Hamilton", "Mercedes", 79.2, 232.5, 88.0, 3.2, 19, 3, 27, 77000),
        ("Singapore Grand Prix", "marina_bay", 60, "2014-09-21", "Lewis Hamilton", "Mercedes", 120.1, 151.8, 110.0, 13.5, 17, 5, 34, 84000),
        ("Japanese Grand Prix", "suzuka", 44, "2014-10-05", "Lewis Hamilton", "Mercedes", 111.7, 137.2, 111.6, 9.2, 19, 3, 40, 82000),
        ("Russian Grand Prix", "sochi", 53, "2014-10-12", "Lewis Hamilton", "Mercedes", 92.0, 202.1, 100.8, 13.7, 19, 2, 23, 55000),
        ("United States Grand Prix", "americas", 56, "2014-11-02", "Lewis Hamilton", "Mercedes", 100.1, 185.0, 101.4, 4.3, 14, 4, 27, 107000),
        ("Brazilian Grand Prix", "interlagos", 71, "2014-11-09", "Nico Rosberg", "Mercedes", 90.0, 203.9, 73.6, 1.5, 16, 2, 45, 68000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2014-11-23", "Lewis Hamilton", "Mercedes", 99.0, 185.2, 104.5, 2.6, 16, 4, 33, 55000)
    ],
    2015: [
        ("Australian Grand Prix", "albert_park", 58, "2015-03-15", "Lewis Hamilton", "Mercedes", 91.9, 200.7, 90.9, 1.4, 11, 4, 16, 101000),
        ("Malaysian Grand Prix", "sepang", 56, "2015-03-29", "Sebastian Vettel", "Ferrari", 101.1, 184.2, 102.1, 8.6, 15, 5, 41, 52000),
        ("Chinese Grand Prix", "shanghai", 56, "2015-04-12", "Lewis Hamilton", "Mercedes", 99.7, 183.6, 102.2, 0.7, 17, 3, 37, 54000),
        ("Bahrain Grand Prix", "bahrain", 57, "2015-04-19", "Lewis Hamilton", "Mercedes", 95.1, 194.7, 94.5, 3.4, 17, 3, 40, 32000),
        ("Spanish Grand Prix", "catalunya", 66, "2015-05-10", "Nico Rosberg", "Mercedes", 101.2, 182.2, 88.3, 17.5, 18, 2, 41, 86000),
        ("Monaco Grand Prix", "monaco", 78, "2015-05-24", "Nico Rosberg", "Mercedes", 109.3, 142.8, 78.1, 4.5, 14, 6, 21, 62000),
        ("Canadian Grand Prix", "villeneuve", 70, "2015-06-07", "Lewis Hamilton", "Mercedes", 87.3, 209.8, 76.9, 2.3, 16, 4, 21, 112000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2015-06-21", "Nico Rosberg", "Mercedes", 90.3, 203.7, 71.2, 3.8, 14, 6, 26, 55000),
        ("British Grand Prix", "silverstone", 52, "2015-07-05", "Lewis Hamilton", "Mercedes", 91.4, 200.9, 97.1, 10.9, 13, 7, 36, 140000),
        ("Hungarian Grand Prix", "hungaroring", 69, "2015-07-26", "Sebastian Vettel", "Ferrari", 106.2, 170.6, 84.8, 5.7, 16, 4, 38, 70000),
        ("Belgian Grand Prix", "spa", 43, "2015-08-23", "Lewis Hamilton", "Mercedes", 83.7, 215.8, 112.4, 2.1, 18, 2, 33, 72000),
        ("Italian Grand Prix", "monza", 53, "2015-09-06", "Lewis Hamilton", "Mercedes", 78.0, 235.9, 86.7, 25.0, 16, 4, 23, 86000),
        ("Singapore Grand Prix", "marina_bay", 61, "2015-09-20", "Sebastian Vettel", "Ferrari", 121.4, 152.7, 110.1, 1.5, 15, 5, 29, 86000),
        ("Japanese Grand Prix", "suzuka", 53, "2015-09-27", "Lewis Hamilton", "Mercedes", 88.1, 209.4, 96.1, 19.0, 18, 2, 36, 81000),
        ("Russian Grand Prix", "sochi", 53, "2015-10-11", "Lewis Hamilton", "Mercedes", 97.2, 191.2, 100.1, 6.0, 14, 6, 23, 60000),
        ("United States Grand Prix", "americas", 56, "2015-10-25", "Lewis Hamilton", "Mercedes", 110.9, 166.9, 100.6, 2.9, 12, 8, 42, 101000),
        ("Mexican Grand Prix", "rodriguez", 71, "2015-11-01", "Nico Rosberg", "Mercedes", 102.6, 178.6, 80.5, 1.9, 17, 3, 27, 134000),
        ("Brazilian Grand Prix", "interlagos", 71, "2015-11-15", "Nico Rosberg", "Mercedes", 91.1, 201.4, 74.8, 7.8, 18, 2, 45, 65000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2015-11-29", "Nico Rosberg", "Mercedes", 98.5, 186.2, 104.5, 8.2, 18, 2, 36, 60000)
    ],
    2016: [
        ("Australian Grand Prix", "albert_park", 57, "2016-03-20", "Nico Rosberg", "Mercedes", 108.9, 166.4, 88.9, 8.1, 16, 6, 38, 91000),
        ("Bahrain Grand Prix", "bahrain", 57, "2016-04-03", "Nico Rosberg", "Mercedes", 93.6, 197.8, 94.5, 10.3, 17, 5, 48, 31000),
        ("Chinese Grand Prix", "shanghai", 56, "2016-04-17", "Nico Rosberg", "Mercedes", 98.9, 185.1, 99.8, 37.8, 22, 0, 66, 56000),
        ("Russian Grand Prix", "sochi", 53, "2016-05-01", "Nico Rosberg", "Mercedes", 92.7, 200.7, 99.0, 25.0, 18, 4, 25, 60000),
        ("Spanish Grand Prix", "catalunya", 66, "2016-05-15", "Max Verstappen", "Red Bull", 101.7, 181.3, 86.9, 0.6, 16, 6, 39, 87000),
        ("Monaco Grand Prix", "monaco", 78, "2016-05-29", "Lewis Hamilton", "Mercedes", 119.5, 130.7, 77.9, 7.3, 15, 7, 33, 63000),
        ("Canadian Grand Prix", "villeneuve", 70, "2016-06-12", "Lewis Hamilton", "Mercedes", 91.1, 201.2, 75.5, 5.0, 18, 4, 30, 115000),
        ("European Grand Prix", "baku", 51, "2016-06-19", "Nico Rosberg", "Mercedes", 92.9, 197.7, 106.5, 16.7, 18, 4, 26, 28000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2016-07-03", "Lewis Hamilton", "Mercedes", 87.6, 210.0, 68.4, 5.7, 16, 6, 38, 45000),
        ("British Grand Prix", "silverstone", 52, "2016-07-10", "Lewis Hamilton", "Mercedes", 94.9, 193.5, 95.5, 8.2, 16, 6, 42, 139000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2016-07-24", "Lewis Hamilton", "Mercedes", 100.5, 183.0, 83.1, 2.0, 20, 2, 44, 75000),
        ("German Grand Prix", "hockenheimring", 67, "2016-07-31", "Lewis Hamilton", "Mercedes", 90.7, 202.7, 78.4, 6.9, 20, 2, 57, 57000),
        ("Belgian Grand Prix", "spa", 44, "2016-08-28", "Nico Rosberg", "Mercedes", 104.9, 176.3, 111.6, 14.1, 17, 5, 41, 85000),
        ("Italian Grand Prix", "monza", 53, "2016-09-04", "Nico Rosberg", "Mercedes", 77.5, 237.6, 85.3, 15.1, 18, 4, 27, 85000),
        ("Singapore Grand Prix", "marina_bay", 61, "2016-09-18", "Nico Rosberg", "Mercedes", 115.9, 160.0, 107.2, 0.5, 18, 4, 45, 73000),
        ("Malaysian Grand Prix", "sepang", 56, "2016-10-02", "Daniel Ricciardo", "Red Bull", 97.2, 191.6, 96.4, 2.4, 16, 6, 36, 45000),
        ("Japanese Grand Prix", "suzuka", 53, "2016-10-09", "Nico Rosberg", "Mercedes", 86.7, 212.8, 95.1, 4.9, 21, 1, 38, 72000),
        ("United States Grand Prix", "americas", 56, "2016-10-23", "Lewis Hamilton", "Mercedes", 98.2, 188.5, 101.4, 4.5, 17, 5, 34, 110000),
        ("Mexican Grand Prix", "rodriguez", 71, "2016-10-30", "Lewis Hamilton", "Mercedes", 100.5, 182.4, 82.1, 8.4, 19, 3, 26, 135000),
        ("Brazilian Grand Prix", "interlagos", 71, "2016-11-13", "Lewis Hamilton", "Mercedes", 181.0, 101.3, 85.3, 11.5, 16, 6, 42, 60000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2016-11-27", "Lewis Hamilton", "Mercedes", 98.1, 187.0, 105.1, 0.4, 17, 5, 33, 60000)
    ],
    2017: [
        ("Australian Grand Prix", "albert_park", 57, "2017-03-26", "Sebastian Vettel", "Ferrari", 84.1, 215.4, 86.5, 10.0, 13, 7, 20, 99000),
        ("Chinese Grand Prix", "shanghai", 56, "2017-04-09", "Lewis Hamilton", "Mercedes", 97.6, 187.6, 95.4, 6.3, 14, 6, 38, 60000),
        ("Bahrain Grand Prix", "bahrain", 57, "2017-04-16", "Sebastian Vettel", "Ferrari", 94.0, 197.0, 92.8, 6.7, 14, 6, 31, 33000),
        ("Russian Grand Prix", "sochi", 52, "2017-04-30", "Valtteri Bottas", "Mercedes", 88.1, 207.1, 96.8, 0.6, 16, 4, 18, 60000),
        ("Spanish Grand Prix", "catalunya", 66, "2017-05-14", "Lewis Hamilton", "Mercedes", 96.0, 192.1, 83.6, 3.5, 16, 4, 31, 95000),
        ("Monaco Grand Prix", "monaco", 78, "2017-05-28", "Sebastian Vettel", "Ferrari", 104.7, 149.1, 74.8, 3.1, 13, 7, 16, 65000),
        ("Canadian Grand Prix", "villeneuve", 70, "2017-06-11", "Lewis Hamilton", "Mercedes", 93.1, 196.8, 74.6, 19.8, 15, 5, 23, 120000),
        ("Azerbaijan Grand Prix", "baku", 51, "2017-06-25", "Daniel Ricciardo", "Red Bull", 124.0, 148.1, 103.4, 3.9, 13, 7, 33, 31000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2017-07-09", "Valtteri Bottas", "Mercedes", 81.8, 224.9, 67.4, 0.6, 16, 4, 21, 55000),
        ("British Grand Prix", "silverstone", 51, "2017-07-16", "Lewis Hamilton", "Mercedes", 81.4, 221.2, 90.6, 14.1, 17, 3, 26, 140000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2017-07-30", "Sebastian Vettel", "Ferrari", 99.8, 184.4, 80.2, 0.9, 17, 3, 22, 79000),
        ("Belgian Grand Prix", "spa", 44, "2017-08-27", "Lewis Hamilton", "Mercedes", 84.7, 218.2, 106.6, 2.4, 16, 4, 28, 110000),
        ("Italian Grand Prix", "monza", 53, "2017-09-03", "Lewis Hamilton", "Mercedes", 75.5, 243.6, 83.4, 4.5, 17, 3, 20, 93000),
        ("Singapore Grand Prix", "marina_bay", 58, "2017-09-17", "Lewis Hamilton", "Mercedes", 123.6, 142.9, 105.0, 4.5, 12, 8, 30, 78000),
        ("Malaysian Grand Prix", "sepang", 56, "2017-10-01", "Max Verstappen", "Red Bull", 90.0, 206.9, 94.0, 12.8, 17, 3, 20, 56000),
        ("Japanese Grand Prix", "suzuka", 53, "2017-10-08", "Lewis Hamilton", "Mercedes", 87.5, 210.8, 93.1, 1.2, 16, 4, 21, 68000),
        ("United States Grand Prix", "americas", 56, "2017-10-22", "Lewis Hamilton", "Mercedes", 93.8, 197.3, 97.8, 10.1, 16, 4, 27, 100000),
        ("Mexican Grand Prix", "rodriguez", 71, "2017-10-29", "Max Verstappen", "Red Bull", 96.6, 189.8, 78.8, 19.7, 16, 4, 23, 135000),
        ("Brazilian Grand Prix", "interlagos", 71, "2017-11-12", "Sebastian Vettel", "Ferrari", 91.4, 200.7, 71.8, 2.8, 16, 4, 21, 70000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2017-11-26", "Valtteri Bottas", "Mercedes", 94.2, 194.7, 100.7, 3.9, 18, 2, 20, 60000)
    ],
    2018: [
        ("Australian Grand Prix", "albert_park", 58, "2018-03-25", "Sebastian Vettel", "Ferrari", 89.6, 206.2, 85.9, 5.0, 15, 5, 22, 100000),
        ("Bahrain Grand Prix", "bahrain", 57, "2018-04-08", "Sebastian Vettel", "Ferrari", 92.0, 201.2, 93.7, 0.7, 17, 3, 23, 33000),
        ("Chinese Grand Prix", "shanghai", 56, "2018-04-15", "Daniel Ricciardo", "Red Bull", 95.6, 191.6, 95.3, 8.9, 19, 1, 35, 62000),
        ("Azerbaijan Grand Prix", "baku", 51, "2018-04-29", "Lewis Hamilton", "Mercedes", 103.7, 177.0, 105.2, 2.5, 13, 7, 31, 35000),
        ("Spanish Grand Prix", "catalunya", 66, "2018-05-13", "Lewis Hamilton", "Mercedes", 95.5, 193.1, 80.4, 20.6, 14, 6, 24, 91000),
        ("Monaco Grand Prix", "monaco", 78, "2018-05-27", "Daniel Ricciardo", "Red Bull", 102.9, 151.7, 74.9, 7.3, 17, 3, 19, 65000),
        ("Canadian Grand Prix", "villeneuve", 68, "2018-06-10", "Sebastian Vettel", "Ferrari", 88.5, 201.0, 73.8, 7.4, 17, 3, 20, 120000),
        ("French Grand Prix", "ricard", 53, "2018-06-24", "Lewis Hamilton", "Mercedes", 90.2, 205.8, 94.3, 7.1, 16, 4, 30, 65000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2018-07-01", "Max Verstappen", "Red Bull", 81.9, 224.5, 67.0, 1.5, 14, 6, 27, 65000),
        ("British Grand Prix", "silverstone", 52, "2018-07-08", "Sebastian Vettel", "Ferrari", 87.5, 209.8, 90.7, 2.3, 14, 6, 31, 140000),
        ("German Grand Prix", "hockenheimring", 67, "2018-07-22", "Lewis Hamilton", "Mercedes", 92.5, 198.8, 75.6, 4.5, 15, 5, 41, 71000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2018-07-29", "Lewis Hamilton", "Mercedes", 97.2, 189.3, 80.0, 17.1, 17, 3, 21, 82000),
        ("Belgian Grand Prix", "spa", 44, "2018-08-26", "Sebastian Vettel", "Ferrari", 83.6, 221.0, 106.3, 11.1, 15, 5, 22, 110000),
        ("Italian Grand Prix", "monza", 53, "2018-09-02", "Lewis Hamilton", "Mercedes", 77.0, 239.0, 82.5, 8.7, 18, 2, 23, 95000),
        ("Singapore Grand Prix", "marina_bay", 61, "2018-09-16", "Lewis Hamilton", "Mercedes", 111.3, 166.4, 101.9, 8.9, 19, 1, 23, 86000),
        ("Russian Grand Prix", "sochi", 53, "2018-09-30", "Lewis Hamilton", "Mercedes", 87.4, 212.7, 95.9, 2.5, 18, 2, 21, 65000),
        ("Japanese Grand Prix", "suzuka", 53, "2018-10-07", "Lewis Hamilton", "Mercedes", 87.3, 211.5, 92.4, 12.9, 18, 2, 22, 81000),
        ("United States Grand Prix", "americas", 56, "2018-10-21", "Kimi Räikkönen", "Ferrari", 94.2, 196.4, 97.3, 1.3, 17, 3, 23, 111000),
        ("Mexican Grand Prix", "rodriguez", 71, "2018-10-28", "Max Verstappen", "Red Bull", 98.5, 186.2, 77.2, 17.3, 16, 4, 31, 135000),
        ("Brazilian Grand Prix", "interlagos", 71, "2018-11-11", "Lewis Hamilton", "Mercedes", 87.1, 210.6, 70.5, 1.5, 18, 2, 24, 75000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2018-11-25", "Lewis Hamilton", "Mercedes", 99.7, 183.9, 100.8, 2.6, 14, 6, 23, 60000)
    ],
    2019: [
        ("Australian Grand Prix", "albert_park", 58, "2019-03-17", "Valtteri Bottas", "Mercedes", 85.4, 216.3, 85.6, 20.9, 17, 3, 22, 102000),
        ("Bahrain Grand Prix", "bahrain", 57, "2019-03-31", "Lewis Hamilton", "Mercedes", 94.3, 196.3, 93.4, 3.0, 16, 4, 34, 34000),
        ("Chinese Grand Prix", "shanghai", 56, "2019-04-14", "Lewis Hamilton", "Mercedes", 92.1, 198.8, 94.7, 6.6, 17, 3, 30, 65000),
        ("Azerbaijan Grand Prix", "baku", 51, "2019-04-28", "Valtteri Bottas", "Mercedes", 91.9, 199.7, 103.1, 1.5, 16, 4, 22, 38000),
        ("Spanish Grand Prix", "catalunya", 66, "2019-05-12", "Lewis Hamilton", "Mercedes", 95.8, 192.4, 78.5, 4.1, 18, 2, 30, 87000),
        ("Monaco Grand Prix", "monaco", 78, "2019-05-26", "Lewis Hamilton", "Mercedes", 103.4, 150.9, 74.3, 2.6, 19, 1, 23, 65000),
        ("Canadian Grand Prix", "villeneuve", 70, "2019-06-09", "Lewis Hamilton", "Mercedes", 89.1, 205.7, 73.1, 3.7, 18, 2, 23, 120000),
        ("French Grand Prix", "ricard", 53, "2019-06-23", "Lewis Hamilton", "Mercedes", 84.5, 219.8, 92.8, 18.1, 19, 1, 22, 60000),
        ("Austrian Grand Prix", "red_bull_ring", 71, "2019-06-30", "Max Verstappen", "Red Bull", 82.0, 224.2, 67.4, 2.7, 20, 0, 22, 70000),
        ("British Grand Prix", "silverstone", 52, "2019-07-14", "Lewis Hamilton", "Mercedes", 81.1, 226.4, 87.4, 24.9, 17, 3, 29, 141000),
        ("German Grand Prix", "hockenheimring", 64, "2019-07-28", "Max Verstappen", "Red Bull", 104.7, 167.7, 76.6, 7.3, 12, 8, 78, 61000),
        ("Hungarian Grand Prix", "hungaroring", 70, "2019-08-04", "Lewis Hamilton", "Mercedes", 95.1, 193.5, 77.1, 17.8, 18, 2, 28, 85000),
        ("Belgian Grand Prix", "spa", 44, "2019-09-01", "Charles Leclerc", "Ferrari", 83.8, 220.6, 106.4, 0.9, 17, 3, 21, 112000),
        ("Italian Grand Prix", "monza", 53, "2019-09-08", "Charles Leclerc", "Ferrari", 75.4, 244.4, 81.8, 0.8, 17, 3, 22, 100000),
        ("Singapore Grand Prix", "marina_bay", 61, "2019-09-22", "Sebastian Vettel", "Ferrari", 118.5, 156.3, 102.4, 2.6, 15, 5, 27, 90000),
        ("Russian Grand Prix", "sochi", 53, "2019-09-29", "Lewis Hamilton", "Mercedes", 93.6, 198.7, 95.8, 3.8, 15, 5, 23, 70000),
        ("Japanese Grand Prix", "suzuka", 52, "2019-10-13", "Valtteri Bottas", "Mercedes", 81.9, 221.3, 91.0, 13.4, 18, 2, 26, 89000),
        ("Mexican Grand Prix", "rodriguez", 71, "2019-10-27", "Lewis Hamilton", "Mercedes", 96.7, 189.6, 79.3, 1.8, 17, 3, 24, 135000),
        ("United States Grand Prix", "americas", 56, "2019-11-03", "Valtteri Bottas", "Mercedes", 93.9, 197.0, 97.0, 4.1, 17, 3, 27, 120000),
        ("Brazilian Grand Prix", "interlagos", 71, "2019-11-17", "Max Verstappen", "Red Bull", 93.2, 196.8, 70.7, 6.1, 16, 4, 32, 78000),
        ("Abu Dhabi Grand Prix", "yas_marina", 55, "2019-12-01", "Lewis Hamilton", "Mercedes", 94.1, 194.9, 99.3, 16.8, 18, 2, 23, 60000)
    ]
}

def generate_f1_dataset():
    records = []
    
    for season, races in SEASON_RACES.items():
        for round_num, (race_name, circuit_id, laps, date, winner_driver, constructor, duration_min, avg_speed, fastest_lap, win_margin, finishers, dnfs, pit_stops, race_attendance) in enumerate(races, start=1):
            c_info = CIRCUITS[circuit_id]
            
            circuit_length = c_info["length_km"]
            race_distance = round(laps * circuit_length, 3)
            gdp_capita = c_info["gdp_per_capita"].get(season, 35000)
            tenure = season - c_info["inaugural_year"] + 1
            
            # Weekend attendance approximation based on known multi-day ratios
            weekend_attendance = int(round(race_attendance * c_info["weekend_mult"]))
            
            # Formulate record
            record = {
                "race_id": f"{season}_{round_num:02d}",
                "season": season,
                "round": round_num,
                "race_name": race_name,
                "circuit_id": circuit_id,
                "circuit_name": c_info["name"],
                "locality": c_info["locality"],
                "country": c_info["country"],
                "continent": c_info["continent"],
                "date": date,
                "circuit_type": c_info["circuit_type"],
                "circuit_length_km": circuit_length,
                "laps": laps,
                "race_distance_km": race_distance,
                "race_duration_min": duration_min,
                "average_speed_kmh": avg_speed,
                "fastest_lap_time_s": fastest_lap,
                "winner_driver": winner_driver,
                "winning_constructor": constructor,
                "winning_margin_s": win_margin,
                "finishers_count": finishers,
                "dnf_count": dnfs,
                "total_pit_stops": pit_stops,
                "attendance_race_day": race_attendance,
                "attendance_weekend": weekend_attendance,
                "attendance_source": "SRC_02;SRC_03",
                "attendance_confidence": "High",
                "gdp_per_capita_usd": gdp_capita,
                "event_tenure_years": tenure
            }
            records.append(record)
            
    df = pd.DataFrame(records)
    
    # Save raw CSV
    output_path = "data/raw/f1_races_raw.csv"
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {len(df)} races across {len(SEASON_RACES)} seasons (2010-2019) at '{output_path}'.")
    print(f"Columns: {list(df.columns)}")
    return df

if __name__ == "__main__":
    df = generate_f1_dataset()
