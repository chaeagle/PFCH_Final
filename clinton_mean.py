### code written by Charlotte Eagle and reusable under MIT license ###

from statistics import mean 
import json


data = {
  "Bull Run Fossil Plant10-51": {
    "2010": [],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "0.4"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.46"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.001707",
    "longitude": "-84.155369"
  },
  "Bull Run Fossil Plant10-52": {
    "2010": [],
    "2011": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0265"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.028"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.355"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.34"
      }
    ],
    "2012": [
      {
        "contaminant": "arsenic",
        "concentration": "0.03"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.022"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.031"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.02625"
      }
    ],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0266"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0275"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.033"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0287"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0267"
      }
    ],
    "2017": [],
    "latitude": "36.000738",
    "longitude": "-84.151325"
  },
  "Bull Run Fossil PlantBRF-1": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "20.0"
      }
    ],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "19.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.8"
      }
    ],
    "2014": [
      {
        "contaminant": "barium",
        "concentration": "2.18"
      },
      {
        "contaminant": "manganese",
        "concentration": "19.6"
      }
    ],
    "2015": [
      {
        "contaminant": "barium",
        "concentration": "2.24"
      }
    ],
    "2016": [
      {
        "contaminant": "barium",
        "concentration": "2.11"
      },
      {
        "contaminant": "barium",
        "concentration": "2.06"
      }
    ],
    "2017": [],
    "latitude": "36.009988",
    "longitude": "-84.153322"
  },
  "Bull Run Fossil PlantBRF-47": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0061"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0067"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.45"
      },
      {
        "contaminant": "sulfate",
        "concentration": "580.0"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0065"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0071"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0078"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0077"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0091"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00905"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.35"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.65"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1000.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "880.0"
      }
    ],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0103"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0074"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00646"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0064"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.78"
      },
      {
        "contaminant": "sulfate",
        "concentration": "930.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "939.0"
      }
    ],
    "2015": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0111"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.008295"
      }
    ],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0344"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00922"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00858"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0111"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0492"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.05025"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0644"
      },
      {
        "contaminant": "sulfate",
        "concentration": "780.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "844.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "806.0"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.358"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.337"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.48"
      }
    ],
    "2017": [],
    "latitude": "36.011728",
    "longitude": "-84.159639"
  },
  "Bull Run Fossil PlantBRF-48": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.041"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.034"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.2"
      },
      {
        "contaminant": "strontium",
        "concentration": "6.2"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1700.0"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.017"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.034"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.026"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.036"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.042"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0436"
      },
      {
        "contaminant": "manganese",
        "concentration": "18.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.6"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.45"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1490.0"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.01775"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.03725"
      },
      {
        "contaminant": "manganese",
        "concentration": "7.39"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1275.0"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0399"
      }
    ],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0282"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0364"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.042533333"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.044425"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1440.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1580.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1795.0"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.1385"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.163"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.1565"
      }
    ],
    "2017": [],
    "latitude": "36.008866",
    "longitude": "-84.157722"
  },
  "Bull Run Fossil PlantBRF-49": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "4.4"
      }
    ],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "9.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.855"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.5"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.785"
      },
      {
        "contaminant": "sulfate",
        "concentration": "740.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "837.0"
      }
    ],
    "2014": [
      {
        "contaminant": "manganese",
        "concentration": "9.39"
      },
      {
        "contaminant": "strontium",
        "concentration": "6.25"
      },
      {
        "contaminant": "sulfate",
        "concentration": "808.0"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0117"
      }
    ],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0265"
      },
      {
        "contaminant": "boron",
        "concentration": "10.4"
      },
      {
        "contaminant": "boron",
        "concentration": "13.15"
      },
      {
        "contaminant": "boron",
        "concentration": "17.5"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0127"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0131"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0149"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.272"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.292"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.322"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1160.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1320.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.466"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.4225"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.624"
      }
    ],
    "2017": [],
    "latitude": "36.00599",
    "longitude": "-84.156632"
  },
  "Bull Run Fossil PlantBRF-50": {
    "2010": [
      {
        "contaminant": "manganese",
        "concentration": "3.7"
      }
    ],
    "2011": [],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.013"
      }
    ],
    "2013": [
      {
        "contaminant": "manganese",
        "concentration": "4.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.44"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.003465",
    "longitude": "-84.155778"
  },
  "Bull Run Fossil PlantF45R": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "16.0"
      },
      {
        "contaminant": "boron",
        "concentration": "17.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.9"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2100.0"
      }
    ],
    "2011": [],
    "2012": [],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "18.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.3"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.4"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2200.0"
      }
    ],
    "2014": [
      {
        "contaminant": "boron",
        "concentration": "19.45"
      },
      {
        "contaminant": "boron",
        "concentration": "20.1"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.65"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.92"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.17"
      },
      {
        "contaminant": "strontium",
        "concentration": "4.34"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1905.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2100.0"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "17.0"
      },
      {
        "contaminant": "boron",
        "concentration": "20.7"
      },
      {
        "contaminant": "boron",
        "concentration": "21.5"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.183"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.1895"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.206"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2220.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2330.0"
      }
    ],
    "2017": [],
    "latitude": "36.024839",
    "longitude": "-84.144651"
  },
  "Bull Run Fossil PlantG": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.025073",
    "longitude": "-84.142817"
  },
  "Bull Run Fossil PlantI": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.02865",
    "longitude": "-84.146354"
  },
  "Bull Run Fossil PlantJ": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "sulfate",
        "concentration": "1070.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "576.0"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "3.03"
      },
      {
        "contaminant": "sulfate",
        "concentration": "549.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "630.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "651.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "676.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "642.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "625.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "646.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "657.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "598.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "643.0"
      }
    ],
    "latitude": "36.02307",
    "longitude": "-84.14695"
  },
  "Bull Run Fossil PlantS": {
    "2010": [],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "0.69"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.997643",
    "longitude": "-84.154651"
  },
  "Bull Run Fossil PlantMW-3H": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "lithium",
        "concentration": "0.0744"
      }
    ],
    "2017": [],
    "latitude": "36.022941",
    "longitude": "-84.150582"
  },
  "Bull Run Fossil PlantBRF-107": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.022594",
    "longitude": "-84.148183"
  },
  "Bull Run Fossil PlantMW-3H/P-3": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "lithium",
        "concentration": "0.0616"
      }
    ],
    "2017": [
      {
        "contaminant": "lithium",
        "concentration": "0.0705"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0672"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.066"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0612"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.064"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0647"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0654"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.063"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0596"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.0629"
      }
    ],
    "latitude": "36.022941",
    "longitude": "-84.150582"
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

        