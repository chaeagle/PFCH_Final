from statistics import mean 
import json

data = {
  "Johnsonville Fossil PlantB10": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.0301",
    "longitude": "-87.977793"
  },
  "Johnsonville Fossil PlantB11": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "0.38"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.45"
      }
    ],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "0.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.6"
      }
    ],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "0.53"
      }
    ],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "0.78"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "0.41"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.034692",
    "longitude": "-87.980695"
  },
  "Johnsonville Fossil PlantB12": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "1.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.6"
      }
    ],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "1.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.2"
      }
    ],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "1.3"
      }
    ],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "1.5"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "0.696"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.036371",
    "longitude": "-87.980557"
  },
  "Johnsonville Fossil PlantB13": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "0.315"
      }
    ],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "0.46"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "0.4025"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.033452",
    "longitude": "-87.977705"
  },
  "Johnsonville Fossil PlantB30": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "0.96"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.026306",
    "longitude": "-87.973534"
  },
  "Johnsonville Fossil PlantB5": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.02347",
    "longitude": "-87.985026"
  },
  "Johnsonville Fossil PlantB6": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "3.3"
      },
      {
        "contaminant": "boron",
        "concentration": "6.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.39"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "6.1"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.023656",
    "longitude": "-87.980309"
  },
  "Johnsonville Fossil PlantB6R": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "7.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.5"
      }
    ],
    "2014": [
      {
        "contaminant": "boron",
        "concentration": "6.62"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.722"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "7.665"
      }
    ],
    "2017": [],
    "latitude": "36.024268",
    "longitude": "-87.980237"
  },
  "Johnsonville Fossil PlantB8": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "10.0"
      },
      {
        "contaminant": "boron",
        "concentration": "10.0"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.065"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.053"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.8"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "9.8"
      },
      {
        "contaminant": "boron",
        "concentration": "9.95"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.053"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0505"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.65"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "9.7"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.049"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.047"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.6"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "9.2"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.051"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.022324",
    "longitude": "-87.97939"
  },
  "Johnsonville Fossil PlantB8R": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "1.1"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "0.421"
      }
    ],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.020778",
    "longitude": "-87.979713"
  },
  "Johnsonville Fossil PlantB9": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.024444",
    "longitude": "-87.971233"
  },
  "Johnsonville Fossil PlantJOF-10-AP1": {
    "2010": [],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "6.3"
      },
      {
        "contaminant": "boron",
        "concentration": "8.1"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.021"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.011"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.3"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "7.62"
      }
    ],
    "2017": [],
    "latitude": "36.024123",
    "longitude": "-87.996897"
  },
  "Johnsonville Fossil PlantJOF-10-AP2": {
    "2010": [],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.058"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.034"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "8.3"
      },
      {
        "contaminant": "sulfate",
        "concentration": "820.0"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.03384",
    "longitude": "-87.992703"
  },
  "Johnsonville Fossil PlantJOF-10-AP3": {
    "2010": [],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "5.3"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.055"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.047"
      },
      {
        "contaminant": "manganese",
        "concentration": "20.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.0"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.11"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.11"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.12"
      },
      {
        "contaminant": "sulfate",
        "concentration": "780.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "730.0"
      }
    ],
    "2012": [
      {
        "contaminant": "nickel",
        "concentration": "0.12"
      }
    ],
    "2013": [
      {
        "contaminant": "cadmium",
        "concentration": "0.0058"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0051"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.12"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.104"
      }
    ],
    "2014": [
      {
        "contaminant": "cadmium",
        "concentration": "0.0051"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.104"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "6.13"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00587"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00502"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0389"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0368"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.101"
      },
      {
        "contaminant": "sulfate",
        "concentration": "752.0"
      }
    ],
    "2017": [],
    "latitude": "36.024175",
    "longitude": "-87.992412"
  },
  "Johnsonville Fossil PlantMW-1": {
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
  "Johnsonville Fossil PlantMW-2": {
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
  "Johnsonville Fossil PlantMW-3": {
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
  "Johnsonville Fossil PlantMW-4R": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0218"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0187"
      }
    ],
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
  "Johnsonville Fossil PlantMW-5": {
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

