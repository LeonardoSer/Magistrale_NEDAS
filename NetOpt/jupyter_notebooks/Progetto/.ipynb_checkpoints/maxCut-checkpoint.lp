\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  20 x[0,2] + 18 x[0,1] + 3 x[0,3] + 20 x[1,2] + 17 x[1,3] + 20 x[1,4]
   + 12 x[2,4] + x[2,3] + x[3,4]
Subject To
 cycleIneq0: x[0,1] - x[0,3] - x[1,3] <= 0
 cycleIneq1: - x[0,1] - x[0,3] + x[1,3] <= 0
 cycleIneq2: - x[0,1] + x[0,3] - x[1,3] <= 0
 cycleIneq3: x[0,1] + x[0,3] + x[1,3] <= 2
 cycleIneq4: x[0,2] - x[0,4] - x[2,4] <= 0
 cycleIneq5: - x[0,2] - x[0,4] + x[2,4] <= 0
 cycleIneq6: - x[0,2] + x[0,4] - x[2,4] <= 0
 cycleIneq7: x[0,2] + x[0,4] + x[2,4] <= 2
 cycleIneq8: - x[0,2] + x[0,1] - x[1,2] <= 0
 cycleIneq9: - x[0,2] - x[0,1] + x[1,2] <= 0
 cycleIneq10: x[0,2] - x[0,1] - x[1,2] <= 0
 cycleIneq11: x[0,2] + x[0,1] + x[1,2] <= 2
 cycleIneq12: x[1,2] - x[1,4] - x[2,4] <= 0
 cycleIneq13: - x[1,2] - x[1,4] + x[2,4] <= 0
 cycleIneq14: - x[1,2] + x[1,4] - x[2,4] <= 0
 cycleIneq15: x[1,2] + x[1,4] + x[2,4] <= 2
 cycleIneq16: x[0,2] - x[0,3] - x[2,3] <= 0
 cycleIneq17: - x[0,2] - x[0,3] + x[2,3] <= 0
 cycleIneq18: - x[0,2] + x[0,3] - x[2,3] <= 0
 cycleIneq19: x[0,2] + x[0,3] + x[2,3] <= 2
 cycleIneq20: x[0,1] - x[0,4] - x[1,4] <= 0
 cycleIneq21: - x[0,1] - x[0,4] + x[1,4] <= 0
 cycleIneq22: - x[0,1] + x[0,4] - x[1,4] <= 0
 cycleIneq23: x[0,1] + x[0,4] + x[1,4] <= 2
 cycleIneq24: x[0,3] - x[0,4] - x[3,4] <= 0
 cycleIneq25: - x[0,3] - x[0,4] + x[3,4] <= 0
 cycleIneq26: - x[0,3] + x[0,4] - x[3,4] <= 0
 cycleIneq27: x[0,3] + x[0,4] + x[3,4] <= 2
 cycleIneq28: x[1,2] - x[1,3] - x[2,3] <= 0
 cycleIneq29: - x[1,2] - x[1,3] + x[2,3] <= 0
 cycleIneq30: - x[1,2] + x[1,3] - x[2,3] <= 0
 cycleIneq31: x[1,2] + x[1,3] + x[2,3] <= 2
 cycleIneq32: x[1,3] - x[1,4] - x[3,4] <= 0
 cycleIneq33: - x[1,3] - x[1,4] + x[3,4] <= 0
 cycleIneq34: - x[1,3] + x[1,4] - x[3,4] <= 0
 cycleIneq35: x[1,3] + x[1,4] + x[3,4] <= 2
 cycleIneq36: - x[2,4] + x[2,3] - x[3,4] <= 0
 cycleIneq37: - x[2,4] - x[2,3] + x[3,4] <= 0
 cycleIneq38: x[2,4] - x[2,3] - x[3,4] <= 0
 cycleIneq39: x[2,4] + x[2,3] + x[3,4] <= 2
 triangleIneq0_0: x[0,2] + x[0,1] + x[1,2] <= 2
 triangleIneq1_0: x[0,2] + x[0,1] + x[1,2] <= 0
 triangleIneq2_0: x[0,2] + x[0,1] + x[1,2] <= 0
 triangleIneq3_0: x[0,2] + x[0,1] + x[1,2] <= 2
 triangleIneq0_1: x[0,1] + x[0,3] + x[1,3] <= 2
 triangleIneq1_1: x[0,1] + x[0,3] + x[1,3] <= 0
 triangleIneq2_1: x[0,1] + x[0,3] + x[1,3] <= 0
 triangleIneq3_1: x[0,1] + x[0,3] + x[1,3] <= 2
 triangleIneq0_2: x[0,1] + x[0,4] + x[1,4] <= 2
 triangleIneq1_2: x[0,1] + x[0,4] + x[1,4] <= 0
 triangleIneq2_2: x[0,1] + x[0,4] + x[1,4] <= 0
 triangleIneq3_2: x[0,1] + x[0,4] + x[1,4] <= 2
 triangleIneq0_3: x[0,2] + x[0,3] + x[2,3] <= 2
 triangleIneq1_3: x[0,2] + x[0,3] + x[2,3] <= 0
 triangleIneq2_3: x[0,2] + x[0,3] + x[2,3] <= 0
 triangleIneq3_3: x[0,2] + x[0,3] + x[2,3] <= 2
 triangleIneq0_4: x[0,2] + x[0,4] + x[2,4] <= 2
 triangleIneq1_4: x[0,2] + x[0,4] + x[2,4] <= 0
 triangleIneq2_4: x[0,2] + x[0,4] + x[2,4] <= 0
 triangleIneq3_4: x[0,2] + x[0,4] + x[2,4] <= 2
 triangleIneq0_5: x[0,3] + x[0,4] + x[3,4] <= 2
 triangleIneq1_5: x[0,3] + x[0,4] + x[3,4] <= 0
 triangleIneq2_5: x[0,3] + x[0,4] + x[3,4] <= 0
 triangleIneq3_5: x[0,3] + x[0,4] + x[3,4] <= 2
 triangleIneq0_6: x[1,2] + x[1,3] + x[2,3] <= 2
 triangleIneq1_6: x[1,2] + x[1,3] + x[2,3] <= 0
 triangleIneq2_6: x[1,2] + x[1,3] + x[2,3] <= 0
 triangleIneq3_6: x[1,2] + x[1,3] + x[2,3] <= 2
 triangleIneq0_7: x[1,2] + x[1,4] + x[2,4] <= 2
 triangleIneq1_7: x[1,2] + x[1,4] + x[2,4] <= 0
 triangleIneq2_7: x[1,2] + x[1,4] + x[2,4] <= 0
 triangleIneq3_7: x[1,2] + x[1,4] + x[2,4] <= 2
 triangleIneq0_8: x[1,3] + x[1,4] + x[3,4] <= 2
 triangleIneq1_8: x[1,3] + x[1,4] + x[3,4] <= 0
 triangleIneq2_8: x[1,3] + x[1,4] + x[3,4] <= 0
 triangleIneq3_8: x[1,3] + x[1,4] + x[3,4] <= 2
 triangleIneq0_9: x[2,4] + x[2,3] + x[3,4] <= 2
 triangleIneq1_9: x[2,4] + x[2,3] + x[3,4] <= 0
 triangleIneq2_9: x[2,4] + x[2,3] + x[3,4] <= 0
 triangleIneq3_9: x[2,4] + x[2,3] + x[3,4] <= 2
Bounds
Binaries
 x[0,2] x[0,1] x[0,3] x[0,4] x[1,2] x[1,3] x[1,4] x[2,4] x[2,3] x[3,4]
End
