from statistics import mean 
import json

data = {
  "Gallatin Fossil PlantGAF-17": {
    "2010": [],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0078"
      },
      {
        "contaminant": "manganese",
        "concentration": "1.5"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.323225",
    "longitude": "-86.41495"
  },
  "Gallatin Fossil PlantGAF-19R": {
    "2010": [
      {
        "contaminant": "beryllium",
        "concentration": "0.017"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.017"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.011"
      },
      {
        "contaminant": "boron",
        "concentration": "4.2"
      },
      {
        "contaminant": "boron",
        "concentration": "3.15"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0054"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.15"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.125"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.092"
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
        "concentration": "11.0"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.17"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.16"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.12"
      },
      {
        "contaminant": "sulfate",
        "concentration": "5000.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "4500.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "4000.0"
      }
    ],
    "2011": [
      {
        "contaminant": "beryllium",
        "concentration": "0.0125"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0135"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.015"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.014"
      },
      {
        "contaminant": "boron",
        "concentration": "3.45"
      },
      {
        "contaminant": "boron",
        "concentration": "3.2"
      },
      {
        "contaminant": "boron",
        "concentration": "3.3"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.13"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.125"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.16"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.26"
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
        "contaminant": "manganese",
        "concentration": "22.0"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.13"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.14"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.15"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.18"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3600.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3350.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3200.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3200.0"
      }
    ],
    "2012": [
      {
        "contaminant": "beryllium",
        "concentration": "0.014"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.012"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0115"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.014"
      },
      {
        "contaminant": "boron",
        "concentration": "3.1"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0051"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00565"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0068"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0079"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.25"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.255"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.32"
      },
      {
        "contaminant": "manganese",
        "concentration": "23.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "33.0"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.18"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.17"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.17"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.19"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3850.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.135"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0141"
      },
      {
        "contaminant": "arsenic",
        "concentration": "0.0117"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.012"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.013"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.013"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0118"
      },
      {
        "contaminant": "boron",
        "concentration": "3.2"
      },
      {
        "contaminant": "boron",
        "concentration": "3.6"
      },
      {
        "contaminant": "boron",
        "concentration": "3.4"
      },
      {
        "contaminant": "boron",
        "concentration": "3.06"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00665"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0066"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.305"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.23"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.32"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.342"
      },
      {
        "contaminant": "manganese",
        "concentration": "29.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "23.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "27.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "27.7"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.195"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.15"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.2"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.211"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2950.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3100.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3300.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "2890.0"
      }
    ],
    "2014": [
      {
        "contaminant": "arsenic",
        "concentration": "0.011333333"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0131"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.013233333"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0114"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.011"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00598"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0083"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0052"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.196"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.288"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.282"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.149"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.24"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.128"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.182"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.169"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.14"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3460.0"
      },
      {
        "contaminant": "thallium",
        "concentration": "0.003833333"
      }
    ],
    "2015": [
      {
        "contaminant": "beryllium",
        "concentration": "0.011"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0101"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0111"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00892"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.466"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.41"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.252"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.198"
      },
      {
        "contaminant": "sulfate",
        "concentration": "3860.0"
      }
    ],
    "2016": [
      {
        "contaminant": "beryllium",
        "concentration": "0.0119"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0103"
      },
      {
        "contaminant": "beryllium",
        "concentration": "0.0105"
      },
      {
        "contaminant": "boron",
        "concentration": "3.9"
      },
      {
        "contaminant": "boron",
        "concentration": "3.98"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.01"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.00933"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0065"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.366"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.365"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.25"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.184"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.178"
      },
      {
        "contaminant": "nickel",
        "concentration": "0.132"
      }
    ],
    "2017": [],
    "latitude": "36.313439",
    "longitude": "-86.40885"
  },
  "Gallatin Fossil PlantGAF-20": {
    "2010": [
      {
        "contaminant": "boron",
        "concentration": "5.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.7"
      },
      {
        "contaminant": "boron",
        "concentration": "5.3"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.21"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.24"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.235"
      },
      {
        "contaminant": "manganese",
        "concentration": "21.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "21.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "21.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1750.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1600.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1600.0"
      }
    ],
    "2011": [
      {
        "contaminant": "boron",
        "concentration": "5.6"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.45"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.18"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.18"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.18"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.175"
      },
      {
        "contaminant": "manganese",
        "concentration": "21.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "20.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "20.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "19.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1600.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1500.0"
      }
    ],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.17"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.17"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.175"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.15"
      },
      {
        "contaminant": "manganese",
        "concentration": "19.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "16.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1800.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.078"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.6"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4"
      },
      {
        "contaminant": "boron",
        "concentration": "5.6"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.16"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.195"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.17"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.1965"
      },
      {
        "contaminant": "manganese",
        "concentration": "18.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "19.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "18.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.9"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1450.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1400.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1270.0"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.183"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.1655"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.181"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.2"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.138"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.138"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1570.0"
      }
    ],
    "2016": [
      {
        "contaminant": "cobalt",
        "concentration": "0.138"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.131"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.141"
      }
    ],
    "2017": [],
    "latitude": "36.317396",
    "longitude": "-86.411931"
  },
  "Gallatin Fossil PlantGAF-21": {
    "2010": [
      {
        "contaminant": "cadmium",
        "concentration": "0.0052"
      },
      {
        "contaminant": "cadmium",
        "concentration": "0.0055"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.24"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.3"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.28"
      },
      {
        "contaminant": "manganese",
        "concentration": "13.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "16.0"
      },
      {
        "contaminant": "manganese",
        "concentration": "17.0"
      },
      {
        "contaminant": "mercury",
        "concentration": "0.0026"
      },
      {
        "contaminant": "mercury",
        "concentration": "0.0029"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1000.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1000.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1200.0"
      }
    ],
    "2011": [
      {
        "contaminant": "cobalt",
        "concentration": "0.21"
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
        "contaminant": "mercury",
        "concentration": "0.003"
      },
      {
        "contaminant": "mercury",
        "concentration": "0.0021"
      },
      {
        "contaminant": "sulfate",
        "concentration": "910.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "950.0"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.315519",
    "longitude": "-86.40358"
  },
  "Gallatin Fossil PlantGAF-22": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.312573",
    "longitude": "-86.404983"
  },
  "Gallatin Fossil PlantGAF-23": {
    "2010": [],
    "2011": [
      {
        "contaminant": "manganese",
        "concentration": "0.3"
      }
    ],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.333063",
    "longitude": "-86.417477"
  },
  "Gallatin Fossil PlantGAF-24": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.335922",
    "longitude": "-86.415604"
  },
  "Gallatin Fossil PlantGAF-25": {
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": [],
    "2014": [],
    "2015": [],
    "2016": [],
    "2017": [],
    "latitude": "36.34197",
    "longitude": "-86.405327"
  },
  "Gallatin Fossil PlantGAF-26": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "5.9"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.014"
      },
      {
        "contaminant": "manganese",
        "concentration": "8.7"
      },
      {
        "contaminant": "sulfate",
        "concentration": "1000.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.022"
      },
      {
        "contaminant": "boron",
        "concentration": "5.8"
      },
      {
        "contaminant": "boron",
        "concentration": "5.5"
      },
      {
        "contaminant": "boron",
        "concentration": "5.35"
      },
      {
        "contaminant": "boron",
        "concentration": "6.04"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.015"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.015"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.017"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0158"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.3"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.4"
      },
      {
        "contaminant": "manganese",
        "concentration": "9.4"
      },
      {
        "contaminant": "manganese",
        "concentration": "8.96"
      },
      {
        "contaminant": "sulfate",
        "concentration": "950.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "880.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "885.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "887.0"
      }
    ],
    "2014": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0156"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0166"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.0142"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.014"
      }
    ],
    "2015": [
      {
        "contaminant": "cobalt",
        "concentration": "0.0145"
      },
      {
        "contaminant": "sulfate",
        "concentration": "918.0"
      }
    ],
    "2016": [
      {
        "contaminant": "boron",
        "concentration": "6.31"
      },
      {
        "contaminant": "boron",
        "concentration": "6.47"
      },
      {
        "contaminant": "cobalt",
        "concentration": "0.00816"
      }
    ],
    "2017": [],
    "latitude": "0.0",
    "longitude": "0.0"
  },
  "Gallatin Fossil PlantGAF-27": {
    "2010": [],
    "2011": [],
    "2012": [
      {
        "contaminant": "boron",
        "concentration": "4.8"
      },
      {
        "contaminant": "sulfate",
        "concentration": "920.0"
      }
    ],
    "2013": [
      {
        "contaminant": "arsenic",
        "concentration": "0.015"
      },
      {
        "contaminant": "boron",
        "concentration": "4.9"
      },
      {
        "contaminant": "boron",
        "concentration": "5.4"
      },
      {
        "contaminant": "boron",
        "concentration": "5.2"
      },
      {
        "contaminant": "boron",
        "concentration": "5.64"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.33"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.6"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.74"
      },
      {
        "contaminant": "manganese",
        "concentration": "0.779"
      },
      {
        "contaminant": "sulfate",
        "concentration": "840.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "920.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "970.0"
      },
      {
        "contaminant": "sulfate",
        "concentration": "874.0"
      }
    ],
    "2014": [],
    "2015": [
      {
        "contaminant": "sulfate",
        "concentration": "973.0"
      }
    ],
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

