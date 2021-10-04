# -*- coding: utf-8 -*-
"""jacard-test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12fS1Qt8R7wyjICl9UbonROSUhij2xArs
"""

from google.colab import drive
drive.mount('/content/drive')
import networkx as nx
import numpy as np
import os, logging, time, operator, random, math, statistics
from prettytable import PrettyTable
from collections import defaultdict
from random import randrange
class SocialNetworkAnalistic:
  #constructor of class
  def __init__(self):
    self.dataset_path = '/content/drive/My Drive/Graph_Dataset/'
    self.datasets = ['family.txt'] 
    self.dataset_name =' '
    self.log_name = ' '
    self.list_nodes = [] #list of nodes
    self.list_edges = [] #list of edges
    self.nbrs = {} #finding all neighbors for each node
    self.weight_node = {}
    self.sorted_k = []
    self.k_top_node = []
    self.weight_edges = {} 
    self.threshold_each_node_dict = {}
    self.active_node = []
    self.G_active_node = []
    self.Time = []
    self.Ave_Active_Nodes = 0
    self.Ave_Execute_Time = 0
    self.Var = 0

  #open file 
  def Open_File(self):
    self.of = open(os.path.join(self.dataset_path,self.dataset_name), 'rb')

  #reading file and making a graph
  def Load_Graph(self):
    self.G =nx.read_adjlist(self.of, create_using = nx.DiGraph(), nodetype=int)
    self.list_nodes = self.G.nodes()
    self.list_edges = self.G.edges()

  #close file
  def Close_File(self):
    self.of.close()

  #finding all neighbors for each node
  def Find_Neighbors(self):
    self.t = time.time()
    in_nbrs = []
    out_nbrs = []
    for node in self.list_nodes:
      in_nbrs = list(self.G.predecessors(node))
      #print(self.G.predecessors(node))
      out_nbrs = list(self.G.neighbors(node))
      self.nbrs[node]={'in':in_nbrs, 'out':out_nbrs}

  #Jaccard Index
  def Jaccard_Index(self):
    for i,j in self.list_edges:
      nbrs_i = {*self.nbrs[i]['in']}|{*self.nbrs[i]['out']}
      nbrs_j = {*self.nbrs[j]['in']}|{*self.nbrs[j]['out']}
      intersection = nbrs_i & nbrs_j
      union = nbrs_i | nbrs_j
      j_index = (len(intersection)/len(union))
      self.G[i][j]['weight'] = round(j_index, 3)
      print(i,j,self.G[i][j]['weight'])

  def main(self):
    for i in range(1):
      self.dataset_name = self.datasets[i]
      self.log_name = '/content/drive/My Drive/Result/result.txt'
      self.Open_File()
      self.Load_Graph()
      self.Close_File()
      self.Find_Neighbors()
      self.Jaccard_Index()

if __name__== "__main__":
  main_obj = SocialNetworkAnalistic()
  main_obj.main()