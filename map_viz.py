'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    
    fig.add_trace(
            go.Choroplethmapbox(
                
                geojson= montreal_data,
                locations=locations,
                featureidkey="properties.NOM",
                z=z_vals,
                zmin=1,
                zmax= 1,
                colorscale=colorscale,
                marker_opacity=0.2, 
                marker_line_width=0, 
                showscale=False, 
                #customdatasrc  ='locations',
                customdata=[[name] for name in locations],
                hovertemplate= hover.map_base_hover_template()
            )
        )
    
    return fig


def add_scatter_traces(fig, street_df, locations):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base

    scatter_fig = px.scatter_map(street_df, 
                        lat='properties.LATITUDE', lon='properties.LONGITUDE', 
                        color='properties.TYPE_SITE_INTERVENTION', zoom=10
                                               
                        
    )

    color_mapping = {
        trace.name: trace.marker.color
        for trace in scatter_fig.data
    }
    

    for type_name, df_type in street_df.groupby('properties.TYPE_SITE_INTERVENTION'):
        tooltip = df_type['properties.TYPE_SITE_INTERVENTION']
        trace_color=color_mapping.get(type_name)
        custom_data=df_type[[
                'properties.NOM_PROJET',
                'properties.MODE_IMPLANTATION',
                'properties.OBJECTIF_THEMATIQUE'
                    ]].copy()
        custom_data['color'] = trace_color 
        fig.add_trace(
            go.Scattermapbox(
                lat=df_type['properties.LATITUDE'],
                lon=df_type['properties.LONGITUDE'],
                mode='markers',
                marker=dict(size=20, color=trace_color),
                name=type_name,
                customdata=custom_data,
                      
                hovertemplate=hover.map_marker_hover_template(tooltip)
            )
        )
    


    
    return fig
