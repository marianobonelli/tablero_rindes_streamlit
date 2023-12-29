# Tablero de Rindes

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

![image](assets/GeoAgro.png)

  </a>

  <p align="center">
      This microservice generates a summary dashboard of yield data uploaded to 360, developed with Streamlit and Python <br />
    <br />
    <a href="https://tablerorindesapp.streamlit.app/">Try Demo App</a>
    ·
    <a href="https://geoagro1.atlassian.net/servicedesk/customer/portal/5">Report Bug</a>
    ·
    <a href="https://geoagro1.atlassian.net/servicedesk/customer/portal/5">Request Feature</a>
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#arquitechture-diagram">Arquitechture-Diagram</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#Roadmap-and-Related-documentation">Roadmap and Related documentation</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About the Project

This microservice generates a summary dashboard of Fields and Crops data uploaded to 360, based on the selected Domain, Area(s), Workspace(s), Season(s), and Farm(s), Crop(s), Hybrid(s)/Variety(ies) and Yield Layer(s).

[![Product Name Screen Shot][product-screenshot]](assets/Tablero.png)

### 1. Filters (Sidebar):
Users can filter data according to Domain, Area(s), Workspace(s), Season(s), Farm(s), Crop(s), Hybrid(s)/Variety(ies) and Yield Layer(s). An option to "select all" is available for all categories. Additionally, the sidebar includes a color palette selector for use in the charts.

### 2. Upper Section:
This section includes the Domain logo, the dashboard title, a language selector, and user information.

### 3. Metrics:
Coming soon. 

### 4. Charts and Maps:

#### Sub Filters:

Users can group information according to Area, Workspace, Season, Farm, Crop, and Hybrid/Variety. This grouping will be the basis for visualizations in the following charts. 

#### Bar Chart 1 - Adjusted Average Yield by Farm:

Displays a bar chart for each layer of yields, grouped according to the previously selected grouping value. The bars are ordered from highest to lowest yield.

#### Bar Chart 2 - Weighted Yield by Farm:

Shows a bar chart with the weighted average yield value for each unique value of the selected grouping field. It maintains the same order as the previous chart.

#### Map:

Displays the centroid of each yield layer, grouped according to the selected grouping field. They maintain the same order and symbolism as the previous charts. Additionally, it is possible to change the background map and view a heatmap generated from the yield values of each layer.

### 5. Download:

Enables downloading the information used in the analysis as a CSV file according to the filters in the sidebar.

Coming soon, it will allow downloading a PDF printout of the dashboard.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Arquitechture Diagram 

[![arquitectura][arquitectura]](assets/arquitectura.png)

### Description

   
1. The user must login in 360.geoagro.com.

2. In the switcher (up-right corner) must select "___________".

3. It opens the url with two tokens, token1 has an info of user like:
   
     user_info={'email': user_email, 'language': 'es', 'env': 'prod', 'domainId': None, 'areaId': None,   'workspaceId': None, 'seasonId': None, 'farmId': None}

4. An Application Load Balancer take the request and send to fargate.
  
5. In fargate, the dashboard is running troughby docker as service.
   


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [![Python][Python.org]][Python-url]
* [![Docker][docker]][docker-url]
* [![Streamlit][streamlit]][streamlit-url]
* [![Plotly][plotly]][plotly-url]
* [![Pandas][pandas]][pandas-url]
* [![GeoPandas][geopandas]][geopandas-url]
* [![Folium][folium]][folium-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/marianobonelli/tablero_rindes_streamlit.git
   ```
2. Install dependencies
   ```sh
     pip3 install -r requirements.txt
   ```
3. Execute
   ```sh
     streamlit python3 tablero_rindes_st.py 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Usage

Uncomment lines __ to __ and Comment lines __ to __.

In this way, the app runs with info presetted in user_info (Please, use your email).

Run:
 ```sh
    http://localhost:5000/
 ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP AND RELATED DOCUMENTATION -->
## Roadmap and Related documentation

<a href="https://docs.google.com/document/d/19VhJlm70Q17YGFvpXy7lmjpxVoGL94f7krxuTHCWmGE/edit?usp=sharing">
  Tablero de Lotes y Cultivos
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

### Mariano Bonelli

[![Email Badge](https://img.shields.io/badge/-mbonelli@geoagro.com-gray?style=flat&logo=gmail&logoColor=white)](mailto:mbonelli@geoagro.com?subject=[GitHub]tablero_lotes_cultivos)
[![LinkedIn Badge](https://img.shields.io/badge/-marianobonelli-gray?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariano-francisco-bonelli/)
[![Twitter Badge](https://img.shields.io/badge/-marianobonelli-gray?logo=x&logoColor=white)](https://twitter.com/marianobonelli)


### Adrian Cuello (API)

[![Email Badge](https://img.shields.io/badge/-acuello@geoagro.com-gray?style=flat&logo=gmail&logoColor=white)](mailto:acuello@geoagro.com?subject=[GitHub]tablero_lotes_cultivos)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: assets/Tablero.png

[arquitectura]: assets/arquitectura.png

[Python.org]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/

[streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://docs.streamlit.io/

[docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/

[plotly]: https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white
[plotly-url]: https://plotly.com/python/

[pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[pandas-url]: https://pandas.pydata.org/

[geopandas]: https://img.shields.io/badge/GeoPandas-119DFF?style=for-the-badge&logo=geopandas&logoColor=white
[geopandas-url]: https://geopandas.org/

[folium]: https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=folium&logoColor=white
[folium-url]: https://python-visualization.github.io/folium/