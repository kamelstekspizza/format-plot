#!/usr/bin/python3
#Collection of functions that are useful for plotting in python
#Mainly related to stuff that useful for formatting the plot, and does not need to be repated in every program
import matplotlib.pyplot as plt


def format_plot(fig,ax,xlabel,ylabel,**kwargs):
    #Pass fig and ax objects to format the plot
    title = kwargs.get('title',False)
    grid = kwargs.get('grid',True)


    ax.set_xlabel(xlabel,fontsize = 20)
    ax.set_ylabel(ylabel,fontsize = 20)
    if title:
        ax.set_title(title,fontsize = 20)
    ax.tick_params(axis = 'both', labelsize = 20)
    if grid:
        ax.grid()
    fig.tight_layout()
    return 