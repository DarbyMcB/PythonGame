"""
A short description.

A bit longer description.

"""
import networkx as nx
from networkx import Graph
import pandas as pd
import numpy as np
from Hex import Hex
# from Player import Player
import math
import pygame


class Map(Graph):
    """
    A short description.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """

    def __init__(self, player_num=2, screen_width=800, screen_height=600):
        """
        Initialize Map.

        Initialize Map Object,
            Calculate Board Size Generate Hexes,
            Build Graph

        Args:
            variable (type):
                self (obj),
                player_num (int),
                screen_width (int),
                screen_height (int)

        Returns:
            type: Map Object

        Raises:
            Exception: description

        """
        super().__init__(self)
        # Generates Hex radius based on the number of players/tiles
        # and Screen Size with a little padding
        # Decides the number of hexes based on number of Players
        self.width = self.get_width(player_num)

        # Calculates a Radius for each Hex based on the size of the screen
        # **SAVED TO INDIVIDUAL HEXES INSTEAD**
        hex_radius = self.gen_hex_radius(screen_width, screen_height)

        # Calculates the Border for the map entity
        self.border_size = self.get_border(screen_width,
                                           screen_height,
                                           hex_radius)

        # Decides total number of Hexes
        self.hex_num = int((self.width*(self.width-1))
                           - (self.width/2 - 1))

        # Starting center position of first Hex
        # **SAVED TO INDIVIDUAL HEXES INSTEAD**
        center = [hex_radius + self.border_size[0],
                  hex_radius + self.border_size[1]]

        # **DIRECTIONLESS GRAPH**
        self.build_self(center, hex_radius)

#############################
#   BUILD AND ADD METHODS   #
#   FOR MAP GRAPH ENTITY    #
#############################

    def build_self(self, center, hex_radius):
        """
        Build Map Graph.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        # Create a list of Hexes
        hexes = self.build_hexes(center, hex_radius)

        # Add Hexes to Self
        self.add_hexes(hexes)

        # Use the list of Hexes to generate edges for the Map Graph
        self.add_edges(self.build_edges(hexes))

        # Select a layout
#        pos = nx.kamada_kawai_layout(self)

        # Draw logic map of the  Game Map
#        nx.draw_networkx(self,pos,node_size=400,node_color='green',edge_color=
#        'orange',with_labels=True,font_size=12,font_color='red',node_shape='h')
#        plt.show()

#############################
#    BUILD AND ADD HEXES    #
#############################

    def build_hexes(self, center, hex_radius):
        """
        Build Hex Nodes.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        nodes = []
        index = 0
        # Loops Vertically
        for j in range(self.width-1):
            if j % 2 == 1:
                center[0] += (hex_radius)
                # Odd rows are 1 tile less to force symmetrical boards
                # Loops accross Horizontally
                for i in range(self.width - 1):
                    nodes.append(Hex(index, hex_radius, center[0], center[1]))
                    center[0] += ((hex_radius * 2))
                    index += 1
            else:
                # Even rows are 1 tile wider
                # Loops Horizontally
                for i in range(self.width):
                    nodes.append(Hex(index, hex_radius, center[0], center[1]))
                    center[0] += ((hex_radius * 2))
                    index += 1
            # Reset horizontal position
            # Increase vertical position
            center[0] = (hex_radius + self.border_size[0])
            center[1] += (hex_radius * math.sqrt(3))
        return nodes

    def add_hexes(self, nodes):
        """
        Add Hexes to Map Graph.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        # Add list of Hexes to Self
        for i in range(0, self.hex_num, 1):
            self.add_node(i, hex=nodes[i])

#############################
#    BUILD AND ADD EDGES    #
#############################

    def build_edges(self, nodes):
        """
        Build Map Edges from DataFrame.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        # Generates a Data Frame using a list of nodes(Hexes)
        node_df = pd.DataFrame({'index': list(range(0, len(nodes))),
                                'edge_1': np.nan,
                                'edge_2': np.nan,
                                'edge_3': np.nan})
        # Populate Data Frame with Edges,
        # starting at the top of the list pointing 'down'
        # Right to Left, Then down, just like we generated the Hex list
        for i in node_df['index']:
            # Create an Edge to the left
            if (((i + 1 % self.width) != 0)
                    and (i + 1 < self.hex_num)):
                node_df['edge_1'].loc[i] = node_df['index'].loc[i+1]
            # Create an Edge to the 'Bottom Left'
            if (((i + self.width - 1) != node_df['edge_1'].loc[i])
                    and (i + self.width < self.hex_num)):
                node_df['edge_2'].loc[i] = node_df['index'].loc[i + self.width - 1]
            # Create an Edge to the 'Bottom Right'
            if (((i + self.width != node_df['edge_1'].loc[i])
                 and (i + self.width != node_df['edge_2'].loc[i]))
                    and ((i + self.width < self.hex_num))):
                node_df['edge_3'].loc[i] = node_df['index'].loc[i + self.width]
        # Generate a DataFrame for each connection
        df1 = node_df[['index', 'edge_1']]
        df2 = node_df[['index', 'edge_2']]
        df3 = node_df[['index', 'edge_3']]
        # Align column names for combination
        df1.columns = ['index', 'edge']
        df2.columns = ['index', 'edge']
        df3.columns = ['index', 'edge']
        # Combine
        node_map = pd.concat([df1, df2, df3])
        # Sort by index
        node_map = node_map.sort_values(by=['index'])
        # Remove stragglers
        node_map = node_map.dropna()
        # print(node_map)
        return node_map

    def add_edges(self, edge_df):
        """
        Add Edges to Map Graph.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        # Generate Graph from Data Frame
        temp_graph = nx.from_pandas_edgelist(edge_df, source='index', target='edge')

        # Import edges from temp Graph
        self.add_edges_from(temp_graph.edges)

#############################
#       ENTITY METHODS      #
#############################

    def get_border(self, screen_width, screen_height, hex_radius):
        """
        Set Border Width around Map.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        return [(screen_width/2 - self.width*hex_radius),
                (screen_height/2 - ((self.width-1)*hex_radius*math.sqrt(3)/2))]

    # Generates a Hex Radius depending on Screen Size and the number of Hexes (Self.width)

    def gen_hex_radius(self, screen_width, screen_height):
        """
        Calculate Radius for Hexes.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        border_size = [screen_width*.05, screen_height*.05]
        hex_radius_hor = (((screen_width - border_size[0]*2) / (self.width))/2)
        hex_radius_vert = (
            ((screen_height - border_size[1]*2) / ((self.width - 1)*(math.sqrt(3)/2))/2))
        if (hex_radius_hor <= hex_radius_vert):
            return hex_radius_hor
        else:
            return hex_radius_vert

    # Draw Function for the Game Map currently draws a Hex Grid

    def drawmap(self, screen):
        """
        Draw Map to Screen.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        for i in self:
            radius = self.nodes[i]['hex'].radius
            center = self.nodes[i]['hex'].center
            self.draw_hex(screen, (255, 0, 0), 6, radius * 1.12, center)
            """
            pygame.draw.circle(screen,
                               (255, 0, 255),
                               (self.nodes[i]['hex'].center[0],
                                self.nodes[i]['hex'].center[1]),
                               self.nodes[i]['hex'].radius, 0)
                            """
#############################
#       STATIC METHODS      #
#############################

    # Checks how many players and forces an even width for symmetrical boards

    @staticmethod
    def get_width(player_num):
        """
        Get the number of Hexes across.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        if (player_num % 2 == 1):
            return ((player_num+1)*4)
        else:
            return ((player_num+1)*4)

    # Test Function to draw N-Gons

    @staticmethod
    def draw_ngon(surface, color, n, radius, position):
        """
        Draw a Polygon.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        pi2 = 2 * 3.14

        for i in range(0, n):
            pygame.draw.line(surface,
                             color,
                             position,
                             (math.sin(i / n * pi2) * radius + position[0],
                              math.cos(i / n * pi2) * radius + position[1]))
        return pygame.draw.lines(surface,
                                 color,
                                 True,
                                 [(math.sin(i / n * pi2) * radius + position[0],
                                   math.cos(i / n * pi2) * radius + position[1])
                                  for i in range(0, n)])

    # Actual Draw Function for game Tiles
    # **VERY USEFUL**

    @staticmethod
    def draw_hex(surface, color, vertex_count, radius, position):
        """
        Draw a Hex Tile.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        pi2 = 2 * 3.14
        n, r = vertex_count, radius
        x, y = position
        pygame.draw.polygon(surface, color,
                            [(math.sin(i / n * pi2) * r + x, math.cos(i / n * pi2) * r + y)
                             for i in range(0, n)])

        pygame.draw.polygon(surface, (0, 0, 0),
                            [(math.sin(i / n * pi2) * r + x, math.cos(i / n * pi2) * r + y)
                             for i in range(0, n)], 2)
