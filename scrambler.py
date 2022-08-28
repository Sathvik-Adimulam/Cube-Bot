import numpy as np
import cv2



moves = np.array(["R", "R'", 'L', "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'", 'R2', 'L2', 'U2', 'D2', 'F2', 'B2'])

def perform(moves):
    r = np.array([["R", "R", "R"], 
                    ["R", "R", "R"], 
                    ["R", "R", "R"]])
    o = np.array([["O", "O", "O"], 
                    ["O", "O", "O"], 
                    ["O", "O", "O"]])
    b = np.array([["B", "B", "B"], 
                    ["B", "B", "B"], 
                    ["B", "B", "B"]])
    g = np.array([["G", "G", "G"], 
                    ["G", "G", "G"], 
                    ["G", "G", "G"]])
    w = np.array([["W", "W", "W"], 
                    ["W", "W", "W"], 
                    ["W", "W", "W"]])
    y = np.array([["Y", "Y", "Y"], 
                    ["Y", "Y", "Y"], 
                    ["Y", "Y", "Y"]])
    for move in moves:
        if move == "R":
                g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
                g[:, 2] = y_copy[:, 2]
                w[:, 2] = g_copy[:, 2]
                b[:, 2] = w_copy[:, 2]
                y[:, 2] = b_copy[:, 2]
                r = np.rot90(r, 1)
        elif move == "R'":
                g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
                g[:, 2] = w_copy[:, 2]
                w[:, 2] = b_copy[:, 2]
                b[:, 2] = y_copy[:, 2]
                y[:, 2] = g_copy[:, 2]
                r = np.rot90(r, -1)
        elif move == "R2":
                g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
                g[:, 2] = b_copy[:, 2]
                w[:, 2] = y_copy[:, 2]
                b[:, 2] = g_copy[:, 2]
                y[:, 2] = w_copy[:, 2]
                r = np.rot90(r, 2)
        elif move == "L":
            g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
            g[:, 0] = w_copy[:, 0]
            w[:, 0] = b_copy[:, 0]
            b[:, 0] = y_copy[:, 0]
            y[:, 0] = g_copy[:, 0]
            o = np.rot90(o, 1)
        elif move == "L'":
            g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
            g[:, 0] = y_copy[:, 0]
            w[:, 0] = g_copy[:, 0]
            b[:, 0] = w_copy[:, 0]
            y[:, 0] = b_copy[:, 0]
            o = np.rot90(o, -1)
        elif move == "L2":
            g_copy, w_copy, b_copy, y_copy = g.copy(), w.copy(), b.copy(), y.copy()
            g[:, 0] = b_copy[:, 0]
            w[:, 0] = y_copy[:, 0]
            b[:, 0] = g_copy[:, 0]
            y[:, 0] = w_copy[:, 0]
            o = np.rot90(o, 2)
        elif move == "U":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[0] = r_copy[0]
            r[0] = b_copy[0]
            b[0] = o_copy[0]
            o[0] = g_copy[0]
            w = np.rot90(w, -1)
        elif move == "U'":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[0] = o_copy[0]
            r[0] = g_copy[0]
            b[0] = r_copy[0]
            o[0] = b_copy[0]
            w = np.rot90(w)
        elif move == "U2":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[0] = b_copy[0]
            r[0] = o_copy[0]
            b[0] = g_copy[0]
            o[0] = r_copy[0]
            w = np.rot90(w, 2)  
        elif move == "D":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[2] = o_copy[2]
            r[2] = g_copy[2]
            b[2] = r_copy[2]
            o[2] = b_copy[2]
            y = np.rot90(y)
        elif move == "D'":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[2] = r_copy[2]
            r[2] = b_copy[2]
            b[2] = o_copy[2]
            o[2] = g_copy[2]
            y = np.rot90(y, -1)
        elif move == "D2":
            g_copy, r_copy, b_copy, o_copy = g.copy(), r.copy(), b.copy(), o.copy()
            g[2] = b_copy[2]
            r[2] = o_copy[2]
            b[2] = g_copy[2]
            o[2] = r_copy[2]
            y = np.rot90(y, 2)

        elif move == "F":
            w_copy, r_copy, y_copy, o_copy = w.copy(), r.copy(), y.copy(), o.copy()
            w[2] = o_copy[:, 2]
            r[:, 0] = w_copy[2]
            y[0] = r_copy[:, 2]
            o[:, 2] = y_copy[0]
            g = np.rot90(g)
        elif move == "F'":
            w_copy, r_copy, y_copy, o_copy = w.copy(), r.copy(), y.copy(), o.copy()
            w[2] = r_copy[:, 0]
            r[:, 0] = y_copy[0]
            y[0] = o_copy[:, 2]
            o[:, 2] = w_copy[2]
            g = np.rot90(g, -1)
    return w

# def generate_scramble():
#     scramble = []
#     move = "."
#     for i in range(20):
#         if i:
#             scramble.append(move)
#             move = np.random.choice(np.extract(np.logical_not(np.char.startswith(moves, move)), moves))
#         else: 
#             move = np.random.choice(moves)
#     return scramble 

print(perform(["F"]))