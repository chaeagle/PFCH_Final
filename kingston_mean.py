
from statistics import mean 
import json

data = {
  "Kingston Fossil Plant22": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "2.15"
      }
    ],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "1.83"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0115"
      }
    ],
    "2015": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0696"
      }
    ],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0112"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0119"
      }
    ],
    "2017": [],
    "latitude": "35.909305",
    "longitude": "-84.504861"
  },
  "Kingston Fossil Plant6AR": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0871"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0991"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.104"
      },
      {
        "contaminant": "manganese",
        "concentration": "26.9"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.111"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0842"
      },
      {
        "contaminant": "manganese",
        "concentration": "35.8"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0968"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.106"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.117"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.111"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.117"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.12"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.121"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.119"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.126"
      }
    ],
    "2016": [
      {
        "contaminant": "cobalt",
        "concentration": "0.14"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.13"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.131"
      }
    ],
    "2017": [],
    "latitude": "35.904582",
    "longitude": "-84.504883"
  },
  "Kingston Fossil PlantAD-1": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.908929",
    "longitude": "-84.519528"
  },
  "Kingston Fossil PlantAD-2": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00642"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00608"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.742"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.739"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.832"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00684"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00858"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00998"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0101"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0112"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.67"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0108"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00887"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00689"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00746"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00798"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00647"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00702"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00676"
      }
    ],
    "2016": [],
    "2017": [],
    "latitude": "35.902915",
    "longitude": "-84.51499"
  },
  "Kingston Fossil PlantAD-3": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "5.64"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.13"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.345"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.006245"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.75"
      },
      {
        "contaminant": "sulfate",
        "concentration": "552.0"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00831"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.84"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.007335"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00772"
      }
    ],
    "2014": [],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0077"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00644"
      }
    ],
    "2016": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00631"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00657"
      },
      {
        "contaminant": "sulfate",
        "concentration": "971.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "659.5"
      }
    ],
    "2017": [],
    "latitude": "35.904124",
    "longitude": "-84.511698"
  },
  "Kingston Fossil PlantKIF-G1B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.896122",
    "longitude": "-84.508339"
  },
  "Kingston Fossil PlantKIF-G3A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.892041",
    "longitude": "-84.510798"
  },
  "Kingston Fossil PlantKIF-G3B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.892041",
    "longitude": "-84.510798"
  },
  "Kingston Fossil PlantKIF-G4B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0101"
      }
    ],
    "2016": [],
    "2017": [],
    "latitude": "35.891627",
    "longitude": "-84.508799"
  },
  "Kingston Fossil PlantKIF-G5A": {
    "2010": [
      {
        "contaminant": "selenium",
        "concentration": "0.379"
      }
    ],
    "2011": [
      {
        "contaminant": "selenium",
        "concentration": "0.137"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.102"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.07275"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.0608"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.891705",
    "longitude": "-84.506888"
  },
  "Kingston Fossil PlantKIF-G5B": {
    "2010": [
      {
        "contaminant": "selenium",
        "concentration": "0.412"
      }
    ],
    "2011": [
      {
        "contaminant": "selenium",
        "concentration": "0.188"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.141"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.131"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.144"
      }
    ],
    "2012": [
      {
        "contaminant": "selenium",
        "concentration": "0.124"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.124"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.117"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.106"
      }
    ],
    "2013": [
      {
        "contaminant": "selenium",
        "concentration": "0.0874"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.07595"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.0672"
      },
      {
        "contaminant": "selenium",
        "concentration": "0.059"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.891705",
    "longitude": "-84.506888"
  },
  "Kingston Fossil PlantKIF-G6B": {
    "2010": [
      {
        "contaminant": "selenium",
        "concentration": "0.0993"
      }
    ],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.892141",
    "longitude": "-84.504912"
  },
  "Kingston Fossil PlantKIF-G2A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0451"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0101"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0398"
      },
      {
        "contaminant": "lead",
        "concentration": "0.149"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.27"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.897368",
    "longitude": "-84.505996"
  },
  "Kingston Fossil PlantKIF-G2B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.897368",
    "longitude": "-84.505996"
  },
  "Kingston Fossil PlantKIF-G7A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.892629",
    "longitude": "-84.503279"
  },
  "Kingston Fossil PlantKIF-G7B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.892629",
    "longitude": "-84.503279"
  },
  "Kingston Fossil PlantKIF-G8A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00656"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.307"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.893625",
    "longitude": "-84.500839"
  },
  "Kingston Fossil PlantKIF-G8B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.893625",
    "longitude": "-84.500839"
  },
  "Kingston Fossil PlantKIF-G9A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "1.34"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.89427",
    "longitude": "-84.500234"
  },
  "Kingston Fossil PlantKIF-G9B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "2.1"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.89427",
    "longitude": "-84.500234"
  },
  "Kingston Fossil PlantKIF-G10A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.895426",
    "longitude": "-84.498771"
  },
  "Kingston Fossil PlantKIF-G10B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.895426",
    "longitude": "-84.498771"
  },
  "Kingston Fossil Plant22B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.909305",
    "longitude": "-84.504861"
  },
  "Kingston Fossil Plant27A": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0168"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0096"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00843"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00821"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00771"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00788"
      }
    ],
    "2016": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00676"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00711"
      }
    ],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "Kingston Fossil PlantGW01": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "Kingston Fossil Plant27B": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "Kingston Fossil PlantKIF-101": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  }
}


#This looks at wells from the overall JSON file.
for wells in data:

  for year in ["2010","2011", "2012", "2013", "2014", "2015", "2016", "2017"]:

    arsenic_values = []
    boron_values = []
    cobalt_values = []
    fluoride_values = []
    lead_values = []
    lithium_values = []
    manganese_values = []
    molybdenum_values = []
    nickel_values = []
    selenium_values = []
    sulfate_values = []
    strontium_values = []

    all_year_data = data[wells][year]

#This for loop isolates each contaminent.
    for measurement in all_year_data:

      if measurement['contaminant'] == "arsenic":
        arsenic_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "boron":
        boron_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "cobalt":
        cobalt_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "fluoride":
        fluoride_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "lithium":
        lithium_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "lead":
        lead_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "manganese":
        manganese_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "molybdenum":
        molybdenum_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "nickel":
       nickel_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "selenium":
        selenium_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "sulfate":
       sulfate_values.append(float(measurement["concentration"]))

      if measurement['contaminant'] == "strontium":
        strontium_values.append(float(measurement["concentration"]))


#this looks at mean of data for each contaimenent, every year, from all plants that are exhibiting contaminated wells.    
      if len(arsenic_values) > 0:
        arsenic_mean = mean(arsenic_values)
        print (wells, year, "arsenic", arsenic_mean)

      if len(boron_values) > 0:
        boron_mean = mean(boron_values)
        print(wells, year, "boron", boron_mean)

      if len(cobalt_values) > 0:
        cobalt_mean = mean(cobalt_values)
        print(wells, year, "cobalt", cobalt_mean)

      if len(fluoride_values) > 0:
        fluoride_mean = mean(fluoride_values)
        print(wells, year, "fluoride", fluoride_mean)

      if len(lead_values) > 0:
        lead_mean = mean(lead_values)
        print(wells, year, "lead", lead_mean)

      if len(lithium_values) > 0:
        lithium_mean = mean(lithium_values)
        print(wells, year, "lithium", lithium_mean)

      if len(manganese_values) > 0:
        manganese_mean = mean(manganese_values)
        print(wells, year, "manganese", manganese_mean)

      if len(molybdenum_values) > 0:
        molybdenum_mean = mean(molybdenum_values)
        print (wells, year, "molybdenum", molybdenum_mean)

      if len(nickel_values) > 0:
        nickel_mean = mean(nickel_values)
        print (wells, year, "nickel", nickel_mean)

      if len(selenium_values) > 0:
        selenium_mean = mean(selenium_values)
        print(wells, year, "selenium", selenium_mean)

      if len(sulfate_values) > 0:
        sulfate_mean = mean(sulfate_values)
        print (wells, year, "sulfate", sulfate_mean)

      if len(strontium_values) > 0:
        strontium_mean = mean(strontium_values)
        print(wells, year, "strontium", strontium_mean)

