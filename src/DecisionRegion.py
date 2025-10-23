from itertools import (
    combinations
    )
from matplotlib.pyplot import (
    subplots
    )
from matplotlib.colors import (
    ListedColormap
    )
from numpy import (
    array, unique, min, max,
    meshgrid, linspace, ravel,
    average,
    )
from pandas import DataFrame

available_markers = ('.', 's', 'x', 'o', '+', '^', 'v')
available_colors = ('red', 'lightgreen', 'blue', 'yellow', 'magenta', 'cyan', 'pink')

def classification_plots( classifier,
                          data: DataFrame,
                          feature_headers,
                          label_header: str,
                          *,
                          steps=50,
                          plotsize=(8, 8),
                          ) :
    
    data_labels = data[ label_header ]
    unique_labels = unique( data_labels )
    plot_combinations = list( combinations( feature_headers, 2 ) )
    
    number_of_labels = len( data_labels )
    number_of_plots = len( plot_combinations )
    
    (figure, axes
     ) = subplots( 1, number_of_plots,
                   figsize=array( plotsize ) * array( [ number_of_plots, 1 ] ) )
    if number_of_plots<2 :
        axes = [ axes ]
    
    (markers, colors
     ) = (available_markers[ :number_of_labels ], available_colors[ :number_of_labels ])
    
    contour_cmap = ListedColormap( colors )
    
    for i, (plot_features, axis) in enumerate( zip( plot_combinations, axes ) ) :
        
        (feat_1, feat_2
         ) = plot_features
        
        (f1_lo, f1_hi
         ) = (min( data[ feat_1 ] ) - 1, max( data[ feat_1 ] ) + 1)
        (f2_lo, f2_hi
         ) = (min( data[ feat_2 ] ) - 1, max( data[ feat_2 ] ) + 1)
        (xx1, xx2
         ) = meshgrid( linspace( f1_lo, f1_hi, steps ),
                       linspace( f2_lo, f2_hi, steps ) )
        
        
        xx = DataFrame( )
        xx[ feat_1 ] = xx1.ravel( )
        xx[ feat_2 ] = xx2.ravel( )
        
        if number_of_plots > 2 :
            non_plot_headers = list( set( feature_headers ) - set( plot_features ) )
            non_plot_averages = list( average( data[ non_plot_headers ],
                                               axis=0 ) )
            xx[ non_plot_headers ] = array(steps ** 2 * [non_plot_averages])
        
        xx = xx[ feature_headers ]

        axis.contourf( xx1, xx2,
                       classifier.predict( xx ).reshape(xx1.shape),
                       alpha=.1, cmap=contour_cmap )
        
        for (label, marker, color) in zip( unique_labels, markers, colors ) :
            
            plotting_data = data[ [ feat_1, feat_2 ] ][ data_labels == label ]
            
            axis.scatter( plotting_data[ feat_1 ], plotting_data[ feat_2 ], label=label,
                          marker=marker, color=color,
                          alpha=.8, edgecolor='black', )
            
            axis.legend( )
            axis.set_xlabel( feat_1 )
            axis.set_ylabel( feat_2 )
    
    figure.show( )
