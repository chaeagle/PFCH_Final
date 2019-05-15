### code written by Charlotte Eagle and reusable under MIT license ###

from statistics import mean 
import json

data = {
  "Allen Fossil PlantP1": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "0.5900000000"
      }
    ],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.071199",
    "longitude": "-90.149379"
  },
  "Allen Fossil PlantP4": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "0.8800000000"
      }
    ],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.074798",
    "longitude": "-90.142416"
  },
  "Allen Fossil PlantP5": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "manganese",
        "concentration": "0.4700000000"
      }
    ],
    "2013": [
      {
        "contaminant": "barium",
        "concentration": "2.4000000000"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.073632",
    "longitude": "-90.133827"
  },
  "Allen Fossil PlantP6": {
    "2010": [],
    "2011": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0420000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0200000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0150000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0320000000"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.8700000000"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.8400000000"
      }
    ],
    "2012": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0220000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0430000000"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.5800000000"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0250000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0328000000"
      }
    ],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0317000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0420000000"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0272000000"
      }
    ],
    "2017": [],
    "latitude": "35.074899",
    "longitude": "-90.138542"
  },
  "Allen Fossil PlantP2": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.075259",
    "longitude": "-90.150808"
  },
  "Allen Fossil PlantALF-206": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "35.073483",
    "longitude": "-90.132903"
  },
  "Allen Fossil PlantALF-203": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "3.9000000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.8700000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "5.2600000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0362000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2840000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "4.1400000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.6200000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.5600000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.5500000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.5200000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.3700000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.2300000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "3.2200000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "2.8900000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.8300000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4100000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.3100000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.2500000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.2300000000"
      },
      {
        "contaminant": "boron",
        "concentration": "4.7300000000"
      },
      {
        "contaminant": "boron",
        "concentration": "4.0800000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "5.5300000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "5.4400000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "5.2600000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "5.0100000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.9700000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.9400000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.5300000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.4600000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.3400000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.1400000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0673000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0639000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0613000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0604000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0568000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0565000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0559000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0420000000"
      },
      {
        "contaminant": "lead",
        "concentration": "0.0363000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3070000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3010000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2960000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2840000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2760000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2700000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2670000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2560000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2540000000"
      }
    ],
    "latitude": "35.074344",
    "longitude": "-90.139839"
  },
  "Allen Fossil PlantALF-201": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "3.8700000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2470000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0185000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.1300000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.6800000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.5700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.3800000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.3100000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3960000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3000000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2900000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2440000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2400000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2390000000"
      }
    ],
    "latitude": "35.069411",
    "longitude": "-90.139789"
  },
  "Allen Fossil PlantALF-210": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0106000000"
      }
    ],
    "latitude": "35.070925",
    "longitude": "-90.151436"
  },
  "Allen Fossil PlantALF-205": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "6.9900000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2520000000"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "9.1400000000"
      },
      {
        "contaminant": "boron",
        "concentration": "8.8100000000"
      },
      {
        "contaminant": "boron",
        "concentration": "7.9500000000"
      },
      {
        "contaminant": "boron",
        "concentration": "7.8800000000"
      },
      {
        "contaminant": "boron",
        "concentration": "7.4700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "7.4600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.9700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.7200000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.2900000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5300000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3650000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3370000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3250000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3250000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3140000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3110000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2990000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2920000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2790000000"
      }
    ],
    "latitude": "35.073714",
    "longitude": "-90.134178"
  },
  "Allen Fossil PlantALF-204": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0460000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0569000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0499000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0491000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0473000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0455000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0428000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0387000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0368000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0364000000"
      }
    ],
    "latitude": "35.074328",
    "longitude": "-90.136978"
  },
  "Allen Fossil PlantALF-202": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.1770000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.3700000000"
      },
      {
        "contaminant": "fluoride",
        "concentration": "4.4500000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.4730000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.2980000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.2810000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.2450000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.2340000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.2280000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.2210000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.1990000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.1970000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.1760000000"
      },
      {
        "contaminant": "boron",
        "concentration": "7.1600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.2900000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.1300000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.0600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "6.0100000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7400000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5100000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.3900000000"
      },
      {
        "contaminant": "boron",
        "concentration": "5.1000000000"
      },
      {
        "contaminant": "boron",
        "concentration": "4.9000000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.4780000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3490000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3400000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3290000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3130000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.3090000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2910000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2880000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.2880000000"
      }
    ],
    "latitude": "35.069247",
    "longitude": "-90.136086"
  },
  "Allen Fossil PlantALF-212": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0116000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0363000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0154000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0145000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0123000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0122000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.7600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.3000000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.2700000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.0600000000"
      },
      {
        "contaminant": "boron",
        "concentration": "3.0500000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0474000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0456000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0439000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0408000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0408000000"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0407000000"
      }
    ],
    "latitude": "35.069239",
    "longitude": "-90.133592"
  },
  "Allen Fossil PlantALF-213": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0316000000"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0396000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0164000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0151000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0127000000"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0114000000"
      }
    ],
    "latitude": "35.071608",
    "longitude": "-90.132625"
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

