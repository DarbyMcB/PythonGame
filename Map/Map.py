"""
Map Object File

Map is a networkx Graph, with each node containing a Hex tile

"""
import networkx as nx
from networkx import Graph
import pandas as pd
import numpy as np
from .City import City
from .Swamp import Swamp
from .Forest import Forest
from .Plains import Plains
from .Mountain import Mountain
from .Hill import Hill
from .Lake import Lake
# from Player import Player
import math
import random
import pygame
import matplotlib.pyplot as plt


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

        # Number of hexes from center to edge of the map
        self._degree = player_num + 1

        # Decides total number of Hexes
        self.hex_num = self.calc_hex_num(self._degree)

        # Starting center position of first Hex
        # **SAVED TO INDIVIDUAL HEXES INSTEAD**
        self._center = [screen_width / 2,
                        screen_height / 2]

        # **DIRECTIONLESS GRAPH**
        self.build_self()

    """
    BUILD AND ADD METHODS
    FOR MAP GRAPH ENTITY
    """

    def build_self(self):
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
        hexes = self.build_hexes()

        # Add Hexes to Self
        self.add_hexes(hexes)

        # Use the list of Hexes to generate edges for the Map Graph
        self.add_edges(self.build_edges(hexes))

        # Select a layout
        pos = nx.kamada_kawai_layout(self)

        # Draw logic map of the  Game Map
        nx.draw_networkx(self, pos, node_size=400, node_color='green', edge_color='orange',
                         with_labels=True, font_size=12, font_color='red', node_shape='h')
        plt.show()

#############################
#    BUILD AND ADD HEXES    #
#############################

    def build_hexes(self):
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
        # Make sure hex postion and map position are aligned
        hex_center = self._center
        hex_coord = [0, 0]
        hex_radius = 50
        terrain = []
        index = 0  # Super easy way to keep track of which node we're on
        # Transformations for going clockwise around the map
        x_shift = [3*hex_radius/2, 0, -3*hex_radius/2,
                   -3*hex_radius/2, 0, 3*hex_radius/2]
        y_shift = [math.sqrt(3)*hex_radius/2, math.sqrt(3)*hex_radius, math.sqrt(3)*hex_radius/2,
                   -math.sqrt(3)*hex_radius/2, -math.sqrt(3)*hex_radius, -math.sqrt(3)*hex_radius/2]
        q_shift = [1, 0, -1, -1, 0, 1]
        r_shift = [0, 1, 1, 0, -1, -1]
        terrain = self.gen_terrain(self._degree, hex_radius)
        for type in terrain:
            nodes.append(type)
        # First hex at map center
        nodes[0].center = [hex_center[0], hex_center[1]]
        nodes[0].hex_coord = [hex_coord[0], hex_coord[1]]
        # For each ring
        for k in range(0, self._degree):
            n = 0
            # Each new ring starts directly above the previous ring start
            hex_center[1] -= math.sqrt(3)*hex_radius
            hex_coord[1] -= 1
            # For each side
            for n in range(0, 6):
                # For each hex on a side (side length is proportional to degree of ring)
                for i in range(0, k + 1):
                    index += 1
                    nodes[index].center = [hex_center[0], hex_center[1]]
                    nodes[index].coord = [hex_coord[0], hex_coord[1]]
                    hex_center[0] = hex_center[0] + x_shift[n]
                    hex_center[1] = hex_center[1] + y_shift[n]
                    hex_coord[0] = hex_coord[0] + q_shift[n]
                    hex_coord[1] = hex_coord[1] + r_shift[n]
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
                                'edge_3': np.nan,
                                'edge_4': np.nan})
        # Edge 1 is for previous node, and Edge 4 is for finishing a ring
        # Populate Data Frame with Edges,
        # Starts with node 1, the top node of ring w/ degree 1
        idx = 1
        # For each ring
        for ring_deg in range(1, self._degree + 1):
            # For each side of the ring going clockwise
            for n in range(0, 6):
                # For each hex on the side going clopckwise
                for i in range(0, ring_deg):
                    # If it's a corner hex
                    if ((idx-1) % ring_deg == 0):
                        # If not the first corner in a ring, connect to the previous node
                        if (n != 0):
                            node_df['edge_1'].loc[idx] = node_df['index'].loc[idx - 1]

                        # If this is the last hex in a ring, link it to the first node in the ring
                        # SPECIAL CASE for ring_deg == 1
                        if (idx == self.calc_hex_num(ring_deg) - 1):
                            node_df['edge_4'].loc[idx] = node_df['index'].loc[idx - ring_deg*6 + 1]
                        # If this isn't the first ring,
                        # connect the corners to the corners on the previous ring
                        if (ring_deg > 1):
                            node_df['edge_2'].loc[idx] = node_df['index'].loc[idx -
                                                                              ((ring_deg - 1)*6 +
                                                                               n)]
                        # Otherwise connect the corners to node 0
                        # SPECIAL CASE for ring_deg == 1
                        else:
                            node_df['edge_2'].loc[idx] = node_df['index'].loc[0]
                    # Middling edge nodes
                    else:
                        # Connect to the previous node
                        node_df['edge_1'].loc[idx] = node_df['index'].loc[idx - 1]
                        # Each middle node has two internal edges, edge_2 and edge_3 calculate this
                        node_df['edge_2'].loc[idx] = node_df['index'].loc[idx -
                                                                          ((ring_deg - 1)*6 + n)]
                        node_df['edge_3'].loc[idx] = node_df['index'].loc[idx -
                                                                          ((ring_deg - 1)*6 + n+1)]
                        # If it's the last middling node on a ring,
                        # then stitch it to the beginning of the ring

                        # For rings larger than degree 1,
                        # this includes the start of the previous ring
                        if (idx == self.calc_hex_num(ring_deg) - 1):
                            node_df['edge_4'].loc[idx] = node_df['index'].loc[idx - ring_deg*6 + 1]
                            node_df['edge_2'].loc[idx] = node_df['index'].loc[self.calc_hex_num(
                                ring_deg - 2)]
                    idx += 1

        # Generate a DataFrame for each connection
        df1 = node_df[['index', 'edge_1']]
        df2 = node_df[['index', 'edge_2']]
        df3 = node_df[['index', 'edge_3']]
        df4 = node_df[['index', 'edge_4']]
        # Align column names for combination
        df1.columns = ['index', 'edge']
        df2.columns = ['index', 'edge']
        df3.columns = ['index', 'edge']
        df4.columns = ['index', 'edge']
        # Combine
        node_map = pd.concat([df1, df2, df3, df4])
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

    """
    ENTITY METHODS
    """

    def calc_hex_num(self, degree):
        """
        Get the total number of Hex tiles on the map based on the degree or radius of the map.

        A bit longer description.

        Args:
            variable (type): description

        Returns:
            type: description

        Raises:
            Exception: description

        """
        if (degree == 0):
            return 1
        else:
            return (6*degree + self.calc_hex_num(degree - 1))

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
            self.draw_hex(screen, self.nodes[i]['hex'])

    """
    STATIC METHODS
    """

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
                             (math.cos(i / n * pi2) * radius + position[0],
                              math.sin(i / n * pi2) * radius + position[1]))
        return pygame.draw.lines(surface,
                                 color,
                                 True,
                                 [(math.cos(i / n * pi2) * radius + position[0],
                                   math.sin(i / n * pi2) * radius + position[1])
                                  for i in range(0, n)])

    # Actual Draw Function for game Tiles
    # **VERY USEFUL**

    @staticmethod
    def draw_hex(surface, hex):
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
        n, r = 6, hex.radius
        x, y = hex.center
        pygame.draw.polygon(surface, hex.color,
                            [(math.cos(i / n * pi2) * r + x, math.sin(i / n * pi2) * r + y)
                             for i in range(0, n)])

        pygame.draw.polygon(surface, (0, 0, 0),
                            [(math.cos(i / n * pi2) * r + x, math.sin(i / n * pi2) * r + y)
                             for i in range(0, n)], 3)

        # Code for displaying "hidden" hex attributes e.g. terrain, location, index, whatever
        GAME_FONT = pygame.font.SysFont('Comic Sans MS', 15)
        text_surface = GAME_FONT.render(str(hex.coord), False, (255, 0, 255))
        GAME_FONT = pygame.font.SysFont('Comic Sans MS', 15)
        text_surface_2 = GAME_FONT.render(str(hex.type), False, (255, 255, 255))
        surface.blit(text_surface, (hex.center[0]-20, hex.center[1] - 10))
        surface.blit(text_surface_2, (hex.center[0]-20, hex.center[1] - 30))

    @staticmethod
    def gen_terrain(degree, hex_radius):
        mult = (degree - 2)
        terrain = []
        for k in range(0, 4*mult):
            terrain.append(Swamp(k, hex_radius))
            terrain.append(Mountain(k, hex_radius))
            terrain.append(Lake(k, hex_radius))
        for k in range(0, 5*mult):
            terrain.append(Hill(k, hex_radius))
        for k in range(0, 9*mult):
            terrain.append(City(k, hex_radius))
            terrain.append(Forest(k, hex_radius))
        for k in range(0, 10*mult):
            terrain.append(Plains(k, hex_radius))
        random.shuffle(terrain)
        for i in range(0, 28*mult):
            terrain[i].index = i
        return (terrain)

    """
    PROPERTIES
    """

    def get_degree(self):
        return self._degree

    def set_degree(self, deg):
        self._degree = deg

    def del_degree(self):
        del self._degree

    degree = property(get_degree, set_degree, del_degree)

    def get_hex_num(self):
        return self._hex_num

    def set_hex_num(self, degree):
        self._hex_num = self.calc_hex_num(self._degree)

    def del_hex_num(self):
        del self._hex_num

    hex_num = property(get_hex_num, set_hex_num, del_hex_num)

    def get_center(self):
        return self._center

    def set_center(self, center):
        self._center = center

    def del_center(self):
        del self._center

    center = property(get_center, set_center, del_center)
