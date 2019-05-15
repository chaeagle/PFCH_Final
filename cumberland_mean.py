from statistics import mean 
import json

data = {
  "Cumberland Fossil PlantCUF-204": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.37641",
    "longitude": "-87.676662"
  },
  "Cumberland Fossil PlantCUF-10-1": {
    "2010": [],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0074"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0064"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.3"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.01"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0089"
      }
    ],
    "2014": [],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.00717"
      }
    ],
    "2016": [],
    "2017": [],
    "latitude": "36.396959",
    "longitude": "-87.66205"
  },
  "Cumberland Fossil PlantCUF-10-2": {
    "2010": [],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.15"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.13"
      },
      {
        "contaminant": "manganese",
        "concentration": "16.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.0"
      }
    ],
    "2012": [
      {
        "contaminant": "cobalt",
        "concentration": "0.18"
      },
      {
        "contaminant": "manganese",
        "concentration": "18.0"
      }
    ],
    "2013": [
      {
        "contaminant": "cobalt",
        "concentration": "0.15"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.0"
      }
    ],
    "2014": [],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.147"
      }
    ],
    "2016": [],
    "2017": [],
    "latitude": "36.395192",
    "longitude": "-87.659122"
  },
  "Cumberland Fossil PlantCUF-93-1": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0069"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0087"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.4"
      },
      {
        "contaminant": "manganese",
        "concentration": "32.0"
      }
    ],
    "2011": [
      {
        "contaminant": "arsenic",
        "concentration": "0.013"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0073"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0078"
      },
      {
        "contaminant": "manganese",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "5.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "7.7"
      }
    ],
    "2012": [
      {
        "contaminant": "arsenic",
        "concentration": "0.011"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.01"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "11.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0184"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0089"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "6.64"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.010665"
      }
    ],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0136"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0104"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.016"
      }
    ],
    "2017": [],
    "latitude": "36.3861111",
    "longitude": "-87.6647222"
  },
  "Cumberland Fossil PlantCUF-93-2": {
    "2010": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0145"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.017"
      },
      {
        "contaminant": "boron",
        "concentration": "36.5"
      },
      {
        "contaminant": "boron",
        "concentration": "34.0"
      },
      {
        "contaminant": "boron",
        "concentration": "34.0"
      },
      {
        "contaminant": "boron",
        "concentration": "34.0"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0087"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0094"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0082"
      },
      {
        "contaminant": "manganese",
        "concentration": "2.7"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.9"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.9"
      },
      {
        "contaminant": "manganese",
        "concentration": "4.8"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.485"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.42"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.43"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.43"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2000.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1900.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2000.0"
      }
    ],
    "2011": [
      {
        "contaminant": "arsenic",
        "concentration": "0.012"
      },
      {
        "contaminant": "boron",
        "concentration": "33.5"
      },
      {
        "contaminant": "boron",
        "concentration": "34.0"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0072"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "3.5"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.47"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.51"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1900.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1800.0"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.3830556",
    "longitude": "-87.6616667"
  },
  "Cumberland Fossil PlantCUF-93-2R": {
    "2010": [
      {
        "contaminant": "arsenic",
        "concentration": "0.012"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.014"
      },
      {
        "contaminant": "boron",
        "concentration": "13.0"
      },
      {
        "contaminant": "boron",
        "concentration": "12.0"
      },
      {
        "contaminant": "boron",
        "concentration": "13.0"
      },
      {
        "contaminant": "boron",
        "concentration": "16.0"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.009"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00685"
      },
      {
        "contaminant": "manganese",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "12.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "15.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      }
    ],
    "2011": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0118"
      },
      {
        "contaminant": "boron",
        "concentration": "16.0"
      },
      {
        "contaminant": "boron",
        "concentration": "13.5"
      },
      {
        "contaminant": "boron",
        "concentration": "14.0"
      },
      {
        "contaminant": "boron",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "12.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "14.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1250.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "14.0"
      },
      {
        "contaminant": "boron",
        "concentration": "14.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "12.5"
      },
      {
        "contaminant": "manganese",
        "concentration": "11.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.035075"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.011"
      },
      {
        "contaminant": "boron",
        "concentration": "13.0"
      },
      {
        "contaminant": "boron",
        "concentration": "13.35"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.15"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1220.0"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "21.3"
      },
      {
        "contaminant": "boron",
        "concentration": "17.5"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1330.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1170.0"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "23.0"
      },
      {
        "contaminant": "boron",
        "concentration": "19.9"
      },
      {
        "contaminant": "boron",
        "concentration": "20.6"
      },
      {
        "contaminant": "boron",
        "concentration": "29.6"
      },
      {
        "contaminant": "boron",
        "concentration": "17.1"
      },
      {
        "contaminant": "boron",
        "concentration": "14.9"
      },
      {
        "contaminant": "boron",
        "concentration": "19.4"
      },
      {
        "contaminant": "boron",
        "concentration": "11.9"
      },
      {
        "contaminant": "boron",
        "concentration": "13.7"
      },
      {
        "contaminant": "boron",
        "concentration": "17.6"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1310.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1280.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1310.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1350.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1360.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1350.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1320.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1270.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1410.0"
      }
    ],
    "latitude": "36.3830556",
    "longitude": "-87.6616667"
  },
  "Cumberland Fossil PlantCUF-93-3": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "6.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7"
      },
      {
        "contaminant": "boron",
        "concentration": "5.85"
      },
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.1"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.93"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.1"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "6.0"
      },
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "boron",
        "concentration": "6.0"
      },
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.1"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.95"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.2"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "6.2"
      },
      {
        "contaminant": "boron",
        "concentration": "6.15"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.3"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.3"
      }
    ],
    "2013": [
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "boron",
        "concentration": "5.51"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.8"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "7.07"
      },
      {
        "contaminant": "lithium",
        "concentration": "0.07115"
      }
    ],
    "2017": [],
    "latitude": "36.3808333",
    "longitude": "-87.6533333"
  },
  "Cumberland Fossil PlantCUF-93-4": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "5.6"
      },
      {
        "contaminant": "boron",
        "concentration": "5.2"
      },
      {
        "contaminant": "boron",
        "concentration": "4.5"
      },
      {
        "contaminant": "boron",
        "concentration": "6.2"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.32"
      },
      {
        "contaminant": "sulfate",
        "concentration": "840.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "810.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "750.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "900.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "6.9"
      },
      {
        "contaminant": "boron",
        "concentration": "6.3"
      },
      {
        "contaminant": "boron",
        "concentration": "3.9"
      },
      {
        "contaminant": "boron",
        "concentration": "3.8"
      },
      {
        "contaminant": "sulfate",
        "concentration": "970.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "850.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "620.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "8.1"
      },
      {
        "contaminant": "boron",
        "concentration": "6.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.51"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.33"
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
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.01785"
      },
      {
        "contaminant": "boron",
        "concentration": "7.2"
      },
      {
        "contaminant": "boron",
        "concentration": "8.78"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1240.0"
      }
    ],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "11.9"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1210.0"
      }
    ],
    "2017": [],
    "latitude": "36.3922222",
    "longitude": "-87.6602778"
  },
  "Cumberland Fossil PlantCUF-RS": {
    "2010": [
      {
        "contaminant": "cobalt",
        "concentration": "0.01"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0095"
      },
      {
        "contaminant": "lead",
        "concentration": "0.023"
      },
      {
        "contaminant": "lead",
        "concentration": "0.017"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.71"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.59"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.68"
      }
    ],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.3805556",
    "longitude": "-87.6452778"
  },
  "Cumberland Fossil PlantCUF-201": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.387786",
    "longitude": "-87.678644"
  },
  "Cumberland Fossil PlantCUF-202": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.386753",
    "longitude": "-87.676117"
  },
  "Cumberland Fossil PlantCUF-205": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.395439",
    "longitude": "-87.660833"
  },
  "Cumberland Fossil PlantCUF-206": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0102"
      },
      {
        "contaminant": "boron",
        "concentration": "21.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "942.0"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0102"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0104"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0103"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0105"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0104"
      },
      {
        "contaminant": "boron",
        "concentration": "24.7"
      },
      {
        "contaminant": "boron",
        "concentration": "21.1"
      },
      {
        "contaminant": "boron",
        "concentration": "21.0"
      },
      {
        "contaminant": "boron",
        "concentration": "24.2"
      },
      {
        "contaminant": "boron",
        "concentration": "19.0"
      },
      {
        "contaminant": "boron",
        "concentration": "19.4"
      },
      {
        "contaminant": "boron",
        "concentration": "19.5"
      },
      {
        "contaminant": "boron",
        "concentration": "18.5"
      },
      {
        "contaminant": "boron",
        "concentration": "21.6"
      },
      {
        "contaminant": "boron",
        "concentration": "21.2"
      },
      {
        "contaminant": "sulfate",
        "concentration": "993.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1030.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "977.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1090.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1020.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1060.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1070.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1040.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "978.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1080.0"
      }
    ],
    "latitude": "36.391744",
    "longitude": "-87.665625"
  },
  "Cumberland Fossil PlantCUF-207": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "27.4"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1040.0"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "32.4"
      },
      {
        "contaminant": "boron",
        "concentration": "26.7"
      },
      {
        "contaminant": "boron",
        "concentration": "27.7"
      },
      {
        "contaminant": "boron",
        "concentration": "32.6"
      },
      {
        "contaminant": "boron",
        "concentration": "23.8"
      },
      {
        "contaminant": "boron",
        "concentration": "25.9"
      },
      {
        "contaminant": "boron",
        "concentration": "25.2"
      },
      {
        "contaminant": "boron",
        "concentration": "24.9"
      },
      {
        "contaminant": "boron",
        "concentration": "26.6"
      },
      {
        "contaminant": "boron",
        "concentration": "27.6"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1090.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1060.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1170.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1120.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1010.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1110.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1050.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1160.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "latitude": "36.394814",
    "longitude": "-87.664703"
  },
  "Cumberland Fossil PlantCUF-208": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "16.9"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00827"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1100.0"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "19.0"
      },
      {
        "contaminant": "boron",
        "concentration": "16.5"
      },
      {
        "contaminant": "boron",
        "concentration": "16.9"
      },
      {
        "contaminant": "boron",
        "concentration": "18.8"
      },
      {
        "contaminant": "boron",
        "concentration": "15.0"
      },
      {
        "contaminant": "boron",
        "concentration": "15.3"
      },
      {
        "contaminant": "boron",
        "concentration": "13.5"
      },
      {
        "contaminant": "boron",
        "concentration": "15.5"
      },
      {
        "contaminant": "boron",
        "concentration": "12.4"
      },
      {
        "contaminant": "boron",
        "concentration": "15.6"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00699"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00672"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0068"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00624"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00659"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1220.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1210.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1290.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1220.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1280.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1250.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1240.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1200.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1240.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1230.0"
      }
    ],
    "latitude": "36.392211",
    "longitude": "-87.666272"
  },
  "Cumberland Fossil PlantCUF-209": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "molybdenum",
        "concentration": "0.0492"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0105"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0121"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0127"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0124"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0113"
      },
      {
        "contaminant": "boron",
        "concentration": "4.34"
      },
      {
        "contaminant": "boron",
        "concentration": "5.89"
      },
      {
        "contaminant": "boron",
        "concentration": "5.54"
      },
      {
        "contaminant": "boron",
        "concentration": "7.64"
      },
      {
        "contaminant": "boron",
        "concentration": "4.14"
      },
      {
        "contaminant": "boron",
        "concentration": "3.58"
      },
      {
        "contaminant": "boron",
        "concentration": "5.27"
      },
      {
        "contaminant": "boron",
        "concentration": "7.64"
      },
      {
        "contaminant": "boron",
        "concentration": "6.81"
      },
      {
        "contaminant": "boron",
        "concentration": "6.19"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0446"
      }
    ],
    "latitude": "36.389203",
    "longitude": "-87.667039"
  },
  "Cumberland Fossil PlantCUF-211": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "5.09"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00668"
      }
    ],
    "2017": [
      {
        "contaminant": "arsenic",
        "concentration": "0.0115"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0108"
      },
      {
        "contaminant": "boron",
        "concentration": "6.29"
      },
      {
        "contaminant": "boron",
        "concentration": "5.67"
      },
      {
        "contaminant": "boron",
        "concentration": "5.44"
      },
      {
        "contaminant": "boron",
        "concentration": "8.19"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4"
      },
      {
        "contaminant": "boron",
        "concentration": "5.47"
      },
      {
        "contaminant": "boron",
        "concentration": "5.08"
      },
      {
        "contaminant": "boron",
        "concentration": "4.64"
      },
      {
        "contaminant": "boron",
        "concentration": "5.76"
      },
      {
        "contaminant": "boron",
        "concentration": "5.65"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0072"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00639"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00705"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00629"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00607"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00667"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00699"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00683"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00645"
      }
    ],
    "latitude": "36.384964",
    "longitude": "-87.662928"
  },
  "Cumberland Fossil PlantCUF-212": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "36.8"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0949"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1310.0"
      }
    ],
    "2017": [
      {
        "contaminant": "boron",
        "concentration": "47.1"
      },
      {
        "contaminant": "boron",
        "concentration": "42.3"
      },
      {
        "contaminant": "boron",
        "concentration": "39.8"
      },
      {
        "contaminant": "boron",
        "concentration": "52.4"
      },
      {
        "contaminant": "boron",
        "concentration": "35.1"
      },
      {
        "contaminant": "boron",
        "concentration": "36.8"
      },
      {
        "contaminant": "boron",
        "concentration": "54.2"
      },
      {
        "contaminant": "boron",
        "concentration": "37.4"
      },
      {
        "contaminant": "boron",
        "concentration": "39.8"
      },
      {
        "contaminant": "boron",
        "concentration": "36.8"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0108"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.012"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0137"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0143"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0108"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0115"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0164"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0187"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0171"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0179"
      },
      {
        "contaminant": "molybdenum",
        "concentration": "0.0412"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1370.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1430.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1460.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1470.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1500.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1510.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1480.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1410.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1520.0"
      }
    ],
    "latitude": "36.380867",
    "longitude": "-87.657836"
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


