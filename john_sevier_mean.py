### code written by Charlotte Eagle and reusable under MIT license ###

from statistics import mean 
import json

data = {
  "John Sevier Fossil Plant1": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.366929",
    "longitude": "-82.969608"
  },
  "John Sevier Fossil PlantJSF-10-36": {
    "2010": [],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "1.85"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.8"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "manganese",
        "concentration": "1.57"
      }
    ],
    "2017": [],
    "latitude": "36.371343",
    "longitude": "-82.967041"
  },
  "John Sevier Fossil PlantJSF-10-37": {
    "2010": [],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "0.75"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.371053",
    "longitude": "-82.973709"
  },
  "John Sevier Fossil PlantW30": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "5.0"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "970.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "4.8"
      },
      {
        "contaminant": "boron",
        "concentration": "5.65"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.0"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.05"
      },
      {
        "contaminant": "sulfate",
        "concentration": "960.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "4.3"
      },
      {
        "contaminant": "boron",
        "concentration": "4.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.8"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.7"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.6"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1000.0"
      }
    ],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "4.1"
      },
      {
        "contaminant": "boron",
        "concentration": "4.48"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.82"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.6"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.6"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1080.0"
      }
    ],
    "2014": [
      {
        "contaminant": "boron",
        "concentration": "4.02"
      },
      {
        "contaminant": "boron",
        "concentration": "4.41"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.13"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.95"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.32"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.66"
      },
      {
        "contaminant": "sulfate",
        "concentration": "997.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "949.0"
      }
    ],
    "2015": [
      {
        "contaminant": "boron",
        "concentration": "4.145"
      },
      {
        "contaminant": "boron",
        "concentration": "4.36"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.175"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.87"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.14"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.09"
      },
      {
        "contaminant": "sulfate",
        "concentration": "959.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1090.0"
      }
    ],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "4.05"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.12"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.45"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1150.0"
      }
    ],
    "2017": [],
    "latitude": "36.375854",
    "longitude": "-82.972778"
  },
  "John Sevier Fossil PlantW28": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "2.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.1"
      },
      {
        "contaminant": "sulfate",
        "concentration": "870.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "890.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "3.1"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "880.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "750.0"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0064"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.96"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "790.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "760.0"
      }
    ],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "3.04"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.8"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.41"
      },
      {
        "contaminant": "sulfate",
        "concentration": "860.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "821.0"
      }
    ],
    "2014": [
      {
        "contaminant": "boron",
        "concentration": "3.02"
      },
      {
        "contaminant": "boron",
        "concentration": "3.04"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.69"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.42"
      },
      {
        "contaminant": "sulfate",
        "concentration": "740.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "631.0"
      }
    ],
    "2015": [
      {
        "contaminant": "manganese",
        "concentration": "2.84"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.66"
      },
      {
        "contaminant": "sulfate",
        "concentration": "723.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "748.0"
      }
    ],
    "2016": [
      {
        "contaminant": "manganese",
        "concentration": "5.04"
      },
      {
        "contaminant": "sulfate",
        "concentration": "684.0"
      }
    ],
    "2017": [],
    "latitude": "36.379237",
    "longitude": "-82.967543"
  },
  "John Sevier Fossil PlantW29": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "2.8"
      },
      {
        "contaminant": "manganese",
        "concentration": "8.3"
      }
    ],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "1.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.0"
      }
    ],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "1.04"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.5"
      }
    ],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "1.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.25"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "4.18"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.435"
      }
    ],
    "2015": [
      {
        "contaminant": "manganese",
        "concentration": "0.794"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.55"
      }
    ],
    "2016": [
      {
        "contaminant": "manganese",
        "concentration": "4.42"
      }
    ],
    "2017": [],
    "latitude": "36.378272",
    "longitude": "-82.969887"
  },
  "John Sevier Fossil PlantW31": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "12.0"
      },
      {
        "contaminant": "boron",
        "concentration": "16.0"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0061"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0082"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.1"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1800.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "11.0"
      },
      {
        "contaminant": "boron",
        "concentration": "18.0"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0068"
      },
      {
        "contaminant": "strontium",
        "concentration": "6.3"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1150.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1500.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "12.0"
      },
      {
        "contaminant": "boron",
        "concentration": "15.5"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.9"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1600.0"
      }
    ],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "11.0"
      },
      {
        "contaminant": "boron",
        "concentration": "15.4"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "4.42"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.82"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1670.0"
      }
    ],
    "2014": [
      {
        "contaminant": "boron",
        "concentration": "13.6"
      },
      {
        "contaminant": "boron",
        "concentration": "8.59"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "2.21"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1190.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "826.0"
      }
    ],
    "2015": [
      {
        "contaminant": "boron",
        "concentration": "13.4"
      },
      {
        "contaminant": "boron",
        "concentration": "15.5"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.38"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.88"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1190.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1485.0"
      }
    ],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "15.8"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1870.0"
      }
    ],
    "2017": [],
    "latitude": "36.372717",
    "longitude": "-82.978161"
  },
  "John Sevier Fossil PlantW32": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.370966",
    "longitude": "-82.978064"
  },
  "John Sevier Fossil PlantAP2": {
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
  "John Sevier Fossil Plant101": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "manganese",
        "concentration": "1.34"
      },
      {
        "contaminant": "sulfate",
        "concentration": "574.0"
      }
    ],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "John Sevier Fossil Plant102": {
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
  "John Sevier Fossil Plant103": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "sulfate",
        "concentration": "1230.0"
      }
    ],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "John Sevier Fossil Plant104": {
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
  "John Sevier Fossil Plant105": {
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
  "John Sevier Fossil PlantLeachate Collection System": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0145"
      },
      {
        "contaminant": "boron",
        "concentration": "4.05"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.55"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.54"
      },
      {
        "contaminant": "sulfate",
        "concentration": "736.0"
      }
    ],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "3.25"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.49"
      },
      {
        "contaminant": "strontium",
        "concentration": "5.56"
      },
      {
        "contaminant": "sulfate",
        "concentration": "608.0"
      }
    ],
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

