# AstroPi
## My Project Title: Investigating Environmental Parameters Aboard the ISS

# Overview
This project explores the variations in environmental parameters aboard the International Space Station (ISS) according to its position relative to the Earth and the sun. We focus on factors such as temperature, humidity, and pressure, evaluating their stability to ensure safe living conditions for the crew. The team aims to understand how these parameters fluctuate with solar exposure and Earth’s shadow and detect Earth's magnetic field from the ISS’s altitude.

# Introduction
Environmental control systems aboard the ISS are designed to maintain stability in humidity, temperature, and pressure levels, crucial for both crew health and scientific research. This study hypothesised minor fluctuations in readings when the ISS moves in and out of sunlight. A significant deviation could indicate potential issues in environmental control, risking crew health and equipment functionality.

# Methodology
Data collection involved a Python 3 script capturing continuous environmental data every second, saving it as a CSV file for secure logging. Photos were taken every minute to corroborate data. Post-collection, the data was imported into spreadsheets and analysed using libraries like Matplotlib, Plotly, PyEphem, and Basemap. These tools enabled us to chart ISS environmental changes and reconstruct its flight path.

# Key Findings
- Stability of Pressure: Pressure remained stable within a few tenths of a millibar, influenced slightly by temperature changes due to Gay-Lussac’s law (pressure is proportional to temperature).
- Cyclic Temperature Variations: A rise in temperature indicated solar exposure, while a decline implied Earth’s shadow. We observed this cycle repeated every 46 minutes.
- Humidity and Temperature Correlation: As temperature rose, humidity decreased, consistent with inverse temperature-humidity relationships.
- Magnetic Field Detection: Stable magnetic readings were obtained, confirming that the Earth’s magnetic field can be detected from the ISS’s altitude.

# Conclusion
The experiment successfully demonstrated that temperature, humidity, and pressure fluctuate in relation to the ISS’s position. Minor anomalies in data may result from equipment interference or slight movement of sensors aboard the ISS. Further experiments with data collection from multiple ISS locations could enhance accuracy.


