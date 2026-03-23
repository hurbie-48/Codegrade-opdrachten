def calculateTotalWeight(widgetamount:int, widgetweight:int, gizmosamount:int, gizmosweight:int) -> int:
    return (widgetamount*widgetweight) + (gizmosamount*gizmosweight)
widgetweight = 75
gizmosweight = 112
widgetamount = int(input("Number of widgets: "))
gizmosamount = int(input("Number of gizmos: "))
print(calculateTotalWeight(widgetamount, widgetweight, gizmosamount, gizmosweight))