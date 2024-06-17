import schemdraw
import matplotlib
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    elm.Resistor()
    elm.Line().down().dot()
    elm.Capacitor().left()
    elm.Line().right
    elm.Line().down()
    elm.MeterV().down()
    
    d.draw()