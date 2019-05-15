# pfch_final

This is an on-going project that aims to look at coal ash contamination on groundwater in the state of Tennessee. Tennessee relies on coal-power plants for electricity or other processing and has reported a consistent rise in ground water contamination. The data used in this project comes from the Environmental Integrity Project, a nonprofit watchdog organization. They designed a website called Ashtracker, that helps the public stay informed about groundwater contamination in their area by providing open access to industry-reported data surrounding wells at other coal-burning power plants. This visualization uses python to isolate contaminated wells and pull their longitude and latitude in order to plot them in Tableau Public. 

For your own analysis you can visit www.ashtracker.org and download data sets to do your own investigation into groundwater contamination in your own area.


Background Information:
Coal ash is a huge industrial waste factor in the United States. Plants that burn coal product an ash byproduct that gets dumped (untreated) into water sources around near the site. In 2008 the largest environmental disaster occurred at the Kingston Fossil Plant. According to Earth Justice (nonprofit environmental law organization), the coal ash dam broke releasing 1.1 billion gallons of coal ash into the Emory and Clinch Rivers making it 5 times larger (by volume) than the BP Deepwater Horizon spill of 2010.  Coal ash is a toxic mis of pollutants that cause a multitude of health effects. Carcinogens like Arsenic, neurotoxins like Manganese, and other toxins have slowly been rising especially in the state of Tennessee. I am from Memphis, Tennessee. The Allen Fossil Plant lies close to our aquifer and sole source of drinking water. The aquifer supplies drinking water for residents in Tennessee and Mississippi and is slowly under attack from coal ash contaminants, particularly arsenic. This is what inspired me to visualize in my own way just how much of the groundwater supply is being contaminated in Tennessee and how this could affect drinking water standards. 


Process:
I used the Ashtracker data sets exported as a .csv file. States are required to monitor groundwater and submit to state agencies and EPA. The Environmental Integrity Project goes through the process of demanding this data from state agencies under the “Right to Know” law. 

I wrote a script that analyzed the .csv in python for each of the plant sites in Tennessee. I defined specific rows I wanted to analyze from the data that would help me build a larger JSON dictionary of only the wells that were showing contamination. I defined the JSON dictionary by year, beginning with 2010 because that is when Ashtracker started loading data. I also included Longitude and Latitude for each well in order to plot on a later visualization. Before I turned the .csv file into my JSON file, I needed to define which wells were contaminated and with what. I did this with a “if” statement defined by two factors:
•	Limit Exceeded: meaning the concentration of a particular contaminant measured above the threshold defined by the government and indicated by True or False.
•	Below Detection Limit: defined as True of False. 
The “if” statement says if the Limit Exceeded was True and Below Detection Limit was False then the well was marked as contaminated. 

Once I had my JSON of all contaminated wells (each identifying the contaminant and the measurement), I wrote a second script for each of the plant sites, that uses the statistics method to analyze the mean for each year of every contaminant. I ran these scripts in my computer’s Terminal in order to get a print out of the Well, Year, Contaminant, and Mean Value. I took that data and turned it into multiple excel files for future use. 


References: 
•	Earth Justice. (n.d.). Tennessee and Coal Ash Disposal in Ponds and Landfills [PDF]. Retrieved from https://earthjustice.org/sites/default/files/tn-coal-ash-factsheet-1111.pdf
•	Environmental Integrity Project. (n.d.). About. Retrieved from http://www.environmentalintegrity.org/who-we-are/
•	Environmental Integrity Project. (n.d.). Ashtracker. Retrieved from https://ashtracker.org/
