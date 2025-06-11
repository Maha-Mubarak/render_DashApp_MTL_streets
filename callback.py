'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
#import dash_html_components as html
import dash.html as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    return None, None, None, None


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    return None, None, None, None


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    
    clicked_point = figure['data'][curve]['customdata'][point]

    title_text = clicked_point[0]  # 'properties.NOM_PROJET'
    mode = clicked_point[1]   # 'properties.MODE_IMPLANTATION'
    theme_text = clicked_point[2]  # 'properties.OBJECTIF_THEMATIQUE'
    color = clicked_point[3] # trace color
    
    title = html.Div(
                title_text,
                id='marker-title', 
                style={'color': color}
    )

    # For Thématique, build an unordered list:
    theme = html.Div([
        html.Span("Thématique :"),
        html.Ul([html.Li(t) for t in theme_text.split('\n') if t])
    ])


    if style == None:
        style={
            'border': '1px solid black',
            'padding': '10px',            
            }
    style['visibility'] = 'visibible'
   
    return title, mode, theme, style

    #return None,None,None,None
   