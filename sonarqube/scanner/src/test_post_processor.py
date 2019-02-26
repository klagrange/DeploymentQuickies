#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:40:28 2018

@author: liujin
"""
import unittest
import post_processor as pp
import numpy as np

class Test_post_processor(unittest.TestCase):
    def test_getting_shortfall_surplus(self):
       priority = 1
       goals = [51020.40816326531, 102040.81632653062, 204081.63265306124]
       years = [6,11,16]
       ir_per_goal = [0.06,0.06,0.06]
       target_met=[0, 0, 0]
       frontend_fee = [0.02,0.02,0.02]
       max_frontend_fee = max(frontend_fee)
       
       ShortfallList = [29501.4638, 40109.8659, 54936.5533]
       SurplusList =  [0.00, 0.00, 0.00]
    
       goals_list = [np.array([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
       [9050.8368, 3920.0000, 5130.8368, 0.0000, 0.0000, 80.0000],
       [9050.8368, 3920.0000, 5130.8368, 0.0000, 0.0000, 80.0000],
       [9050.8368, 3920.0000, 5130.8368, 0.0000, 0.0000, 80.0000],
       [9050.8368, 3920.0000, 5130.8368, 0.0000, 0.0000, 80.0000],
       [9050.8368, 3920.0000, 5130.8368, 0.0000, 0.0000, 80.0000]]), np.array([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
       [7741.6284, 3920.0000, 3821.6284, 0.0000, 0.0000, 80.0000],
       [7741.6284, 3920.0000, 3821.6284, 0.0000, 0.0000, 80.0000],
       [7741.6284, 3920.0000, 3821.6284, 0.0000, 0.0000, 80.0000],
       [7741.6284, 3920.0000, 3821.6284, 0.0000, 0.0000, 80.0000],
       [7741.6284, 3920.0000, 3821.6284, 0.0000, 0.0000, 80.0000],
       [12855.8292, 5880.0000, 6975.8292, 0.0000, 0.0000, 120.0000],
       [12855.8292, 5880.0000, 6975.8292, 0.0000, 0.0000, 120.0000],
       [12855.8292, 5880.0000, 6975.8292, 0.0000, 0.0000, 120.0000],
       [12855.8292, 5880.0000, 6975.8292, 0.0000, 0.0000, 120.0000],
       [12855.8292, 5880.0000, 6975.8292, 0.0000, 0.0000, 120.0000]]), np.array([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
       [8767.9110, 3920.0000, 4847.9110, 0.0000, 0.0000, 80.0000],
       [8767.9110, 3920.0000, 4847.9110, 0.0000, 0.0000, 80.0000],
       [8767.9110, 3920.0000, 4847.9110, 0.0000, 0.0000, 80.0000],
       [8767.9110, 3920.0000, 4847.9110, 0.0000, 0.0000, 80.0000],
       [8767.9110, 3920.0000, 4847.9110, 0.0000, 0.0000, 80.0000],
       [12480.9276, 5880.0000, 6600.9276, 0.0000, 0.0000, 120.0000],
       [12480.9276, 5880.0000, 6600.9276, 0.0000, 0.0000, 120.0000],
       [12480.9276, 5880.0000, 6600.9276, 0.0000, 0.0000, 120.0000],
       [12480.9276, 5880.0000, 6600.9276, 0.0000, 0.0000, 120.0000],
       [12480.9276, 5880.0000, 6600.9276, 0.0000, 0.0000, 120.0000],
       [21314.4577, 11760.0000, 9554.4577, 0.0000, 0.0000, 240.0000],
       [21314.4577, 11760.0000, 9554.4577, 0.0000, 0.0000, 240.0000],
       [21314.4577, 11760.0000, 9554.4577, 0.0000, 0.0000, 240.0000],
       [21314.4577, 11760.0000, 9554.4577, 0.0000, 0.0000, 240.0000],
       [21314.4577, 11760.0000, 9554.4577, 0.0000, 0.0000, 240.0000]])]
        
       shortfall_list,surplus_list = pp.getting_shortfall_surplus(priority,goals,years,ir_per_goal,goals_list,target_met,max_frontend_fee)
       for i in range(len(shortfall_list)):           
           self.assertAlmostEqual(shortfall_list[i],ShortfallList[i],delta = 0.05)
           self.assertAlmostEqual(surplus_list[i],SurplusList[i],delta = 0.05)
             
if __name__ == '__main__':
    unittest.main()
        
        