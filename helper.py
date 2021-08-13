import numpy as np
#    #source: https://en.wikipedia.org/wiki/Cubic_Hermite_spline

def CatmullRomSpline(P0, P1, P2, P3, nPoints=100):
        # alpha = something for Centripetal 
        def calculateT(ti, Pi, Pj, alpha=0):
            xi, yi, zi = Pi
            xj, yj, zj = Pj
            return ( ( (xj-xi)**2 + (yj-yi)**2 + (zj-zi)**2 )**0.5 )**alpha + ti

        t0 = 0
        t1 = calculateT(t0, P0, P1)
        t2 = calculateT(t1, P1, P2)
        t3 = calculateT(t2, P2, P3)
        t = np.linspace(t1,t2,nPoints)
        t = t.reshape(len(t), 1)
        A1 = (t1-t)/(t1-t0)*P0 + (t-t0)/(t1-t0)*P1
        A2 = (t2-t)/(t2-t1)*P1 + (t-t1)/(t2-t1)*P2
        A3 = (t3-t)/(t3-t2)*P2 + (t-t2)/(t3-t2)*P3
        B1 = (t2-t)/(t2-t0)*A1 + (t-t0)/(t2-t0)*A2
        B2 = (t3-t)/(t3-t1)*A2 + (t-t1)/(t3-t1)*A3
        C = (t2-t)/(t2-t1)*B1 + (t-t1)/(t2-t1)*B2
        return C 