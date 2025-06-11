'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.
      
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    hover_template = ("&nbsp;%{customdata[0]}<extra></extra>" )
    return hover_template


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    #hover_template = ("%{customdata[0]}" )
    hover_template = ("&nbsp;"+name+"<extra></extra>" )
    return hover_template