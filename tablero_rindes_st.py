import streamlit as st
import pandas as pd
from datetime import datetime  # Import the datetime class from the datetime module
import time
import plotly.express as px
from PIL import Image

# Cargar la imagen
page_icon = Image.open("favicon geoagro nuevo-13.png")

st.set_page_config(
    page_title="Tablero de Rindes",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://support.geoagro.com/es/',
        'Report a bug': "https://geoagro1.atlassian.net/servicedesk/customer/portal/5",
        'About': "Este tablero de rindes toma la metadata de las capas de las capas de rindes cargadas en 360 para generarse."
    }
)

st.title('Tablero de Rindes')

# Read the CSV file into a DataFrame
filtered_df = pd.read_csv('csv_rindes.csv')


with st.sidebar:

    ############################################################################
    # Selector de color
    ############################################################################

    # Obtener la lista de rampas de colores cualitativos
    color_ramps = dir(px.colors.qualitative)
    # Filtrar los elementos que no son rampas de colores
    color_ramps = [ramp for ramp in color_ramps if not ramp.startswith("__")]
    # Encontrar el índice de 'Pastel' en la lista de rampas de colores
    default_index = color_ramps.index('Pastel') if 'Pastel' in color_ramps else 0

    # Selector para la rampa de colores con un valor predeterminado
    selected_color_ramp = st.selectbox('Paleta de colores', color_ramps, index=default_index)

    # Usa getattr para obtener la rampa de colores seleccionada
    selected_colors = getattr(px.colors.qualitative, selected_color_ramp)


    ############################################################################
    # Area
    ############################################################################

    areas = filtered_df['area_name'].unique()

    selector_areas = st.multiselect(
        'Area',
        areas,
        placeholder='elije una opción')

    ############################################################################
    # Workspace
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['area_name'].isin(selector_areas)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    workspaces = filtered_df['workspace_name'].unique()

    selector_workspaces = st.multiselect(
        'Workspace',
        workspaces,
        placeholder='elije una opción')

    ############################################################################
    # Season
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['workspace_name'].isin(selector_workspaces)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    seasons = filtered_df['season_name'].unique()

    selector_seasons = st.multiselect(
        'Season',
        seasons,
        placeholder='elije una opción')

    ############################################################################
    # Farm
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['season_name'].isin(selector_seasons)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    farms = filtered_df['farm_name'].unique()

    selector_farms = st.multiselect(
        'Farm',
        farms,
        placeholder='elije una opción')

    ############################################################################
    # Cultivo
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['farm_name'].isin(selector_farms)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    crop = filtered_df['crop'].unique()

    selector_crop = st.multiselect(
        'Cultivo',
        crop,
        placeholder='elije una opción')

    ############################################################################
    # Híbrido
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['crop'].isin(selector_crop)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    hybridos = filtered_df['hybrid'].unique()

    selector_hybrid = st.multiselect(
        'Híbrido / Variedad',
        hybridos,
        default=hybridos,
        placeholder='elije una opción')

    ############################################################################
    # Capas
    ############################################################################

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['hybrid'].isin(selector_hybrid)]
    # Obtén los nombres de los workspaces únicos del DataFrame filtrado
    capas = filtered_df['Nombre'].unique()

    selector_capas = st.multiselect(
        'Capas de rindes',
        capas,
        default=capas,
        placeholder='elije una opción')

    # Filtra el DataFrame basado en las áreas seleccionadas
    filtered_df = filtered_df[filtered_df['Nombre'].isin(selector_capas)]

    # Cargar la imagen
    imagen = Image.open("powered_by_GeoAgro.png")
    # Mostrar la imagen en la aplicación
    st.image(imagen, use_column_width=False)

############################################################################

if selector_capas:

    ############################################################################
    # Gráfico
    ############################################################################
    campos_agrupamiento = {
        'Area': 'area_name',
        'Workspace': 'workspace_name',
        'Farm':'farm_name',
        'Cultivo': 'crop',
        'Híbrido / Variedad': 'hybrid'
    }

    # Obtener el índice de 'Farm' en la lista de claves
    default_index = list(campos_agrupamiento.keys()).index('Farm')
    # Selector para elegir una clave del diccionario
    selected_key = st.selectbox('Seleccione un campo de agrupamiento:', list(campos_agrupamiento.keys()), index=default_index)
    # Obtén el valor asociado a la clave seleccionada
    selected_value = campos_agrupamiento[selected_key]
    # Ordenar el DataFrame primero por farm_name y luego por Rendimiento medio ajustado
    filtered_df = filtered_df.sort_values(by='Rendimiento medio ajustado', ascending=False)



    # Crear un gráfico de barras interactivo con Plotly
    fig = px.bar(
        filtered_df,
        x='Nombre',
        y='Rendimiento medio ajustado',
        color=selected_value,
        title='Rendimiento medio ajustado por ' + selected_key,
        labels={'Rendimiento medio ajustado': 'Rendimiento Medio Ajustado'},
        height=500,
        hover_data={
            'Nombre': True,  # Mantener la etiqueta de Nombre
            'Rendimiento medio ajustado': ':.2f',  # Formatear el rendimiento a 2 decimales
            selected_value: True,  # Mantener la etiqueta del valor seleccionado
        },
        color_discrete_sequence=selected_colors  # Aquí se actualiza la paleta de colores
    )

    # Personalizar el diseño del gráfico
    fig.update_xaxes(title_text='Capa de Rinde')
    fig.update_yaxes(title_text='Rendimiento Medio Ajustado')
    fig.update_layout(xaxis_tickangle=-45)

    # fig.write_html('bar_graph.html')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


    ############################################################################
    # Gráfico
    ############################################################################

    # Obtener los nombres de los grupos en el orden del 'Rendimiento medio ajustado'
    ordered_groups = filtered_df.sort_values(
        by='Rendimiento medio ajustado', ascending=False
    )[selected_value].unique()

    # Agrupa por el valor seleccionado y calcula el rendimiento ponderado para cada grupo
    grouped = filtered_df.groupby(selected_value).apply(
        lambda x: x['Producción total'].sum() / x['hectares'].sum()
    ).reset_index()

    # Cambia el nombre de la columna 0 a 'Rendimiento Ponderado'
    grouped = grouped.rename(columns={0: 'Rendimiento Ponderado'})

    # Ordena el DataFrame 'grouped' según el orden de 'ordered_groups'
    grouped['order'] = grouped[selected_value].apply(lambda x: list(ordered_groups).index(x))
    grouped = grouped.sort_values('order').drop(columns='order')

    # Crear un gráfico de barras con Plotly
    fig = px.bar(
        grouped,
        x=selected_value,
        y='Rendimiento Ponderado',
        color=selected_value,
        title='Rendimiento Ponderado por ' + selected_key,
        labels={'Rendimiento Ponderado': 'Rendimiento Ponderado'},
        height=500,
        color_discrete_sequence=selected_colors  # Aquí se actualiza la paleta de colores
    )

    # Personalizar el diseño del gráfico
    fig.update_xaxes(title_text=selected_key)
    fig.update_yaxes(title_text='Rendimiento Ponderado')
    fig.update_layout(xaxis_tickangle=-45)

    # Agregar anotaciones para mostrar los valores de Y sobre cada barra
    for i, val in enumerate(grouped['Rendimiento Ponderado']):
        fig.add_annotation(
            dict(
                x=grouped[selected_value].iloc[i], # posición x (nombre del grupo)
                y=val,  # posición y (valor de la barra)
                text=f'{val:.2f}',  # texto a mostrar (valor de la barra formateado)
                showarrow=False,  # no mostrar flecha
                yshift=10,  # ajustar la posición verticalmente para que no se superponga con la barra
                # font=dict(size=15)  # tamaño de la fuente, color de la fuente, es opcional
            )
        )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

    ############################################################################
    # mapa
    ############################################################################
    st.divider()

    import streamlit as st
    import pandas as pd
    import plotly.express as px
    from shapely import wkt
    import geopandas as gpd
    import folium
    from folium import FeatureGroup, LayerControl
    from streamlit_folium import folium_static

    # Mapear los colores del gráfico a los valores únicos de la columna de agrupamiento
    colors = selected_colors
    unique_values = filtered_df[selected_value].unique()
    color_map = {val: colors[i % len(colors)] for i, val in enumerate(unique_values)}
    filtered_df['color'] = filtered_df[selected_value].map(color_map)

    # Convertir la columna 'centroid' a objetos de geometría
    filtered_df['geometry'] = filtered_df['centroid'].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(filtered_df, geometry='geometry')

    st.caption('Mapa de puntos por capa según ' + selected_key)

    # Crear mapa
    m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=7)
    feature_groups = {}

    for idx, row in gdf.iterrows():
        group_name = row[selected_value]
        if group_name not in feature_groups:
            feature_groups[group_name] = FeatureGroup(name=str(group_name))

        marker = folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=9,
            color=row['color'],
            fill=True,
            fill_opacity=0.8,
            fill_color=row['color'],
            tooltip=f"{row['Nombre']}<br>Area: {row['area_name']}<br>WS: {row['workspace_name']}<br>Season: {row['season_name']}<br>Establecimiento: {row['farm_name']}<br>Cultivo: {row['crop']}<br>Híbrido / Variedad: {row['hybrid']}<br>Rendimiento Medio Ajustado: {row['Rendimiento medio ajustado']:.2f}"
        )
        marker.add_to(feature_groups[group_name])

    for group_name, feature_group in feature_groups.items():
        feature_group.add_to(m)

    # Agrega la capa de teselas de Esri World Imagery
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' 
    attr = 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'

    # Agrega las capas de teselas adicionales y el control de capas
    folium.TileLayer(tiles, attr=attr, name='Esri World Imagery', show=True).add_to(m)

    LayerControl(collapsed=True).add_to(m)

    # m.save("map.html")
    
    folium_static(m)



else:
    st.warning("Debe seleccionar una capa de rindes para continuar")

st.caption("Powered by GeoAgro")
