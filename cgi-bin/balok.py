def luas(p, L, t):
    l = 2*(p*L+p*t+L*t)
    return l

print "<!DOCTYPE html>"
print
print"""<html>
        <head>
            <title>Kegiatan 3</title>
        </head>
        <body>
            <table border='0'>
                <tr>
                    <td colspan='4'><p align='center'><b>Bangun Balok</b></p></td>
                </tr>
                <tr>
                    <td rowspan='8'><img src='../balok.jpg'></td>
                </tr>
                <tr>
                    <td>Nama bangun</td>
                    <td>:</td>
                    <td>Balok</td>
                </tr>
                <tr>
                    <td>Dimensi</td>
                    <td>:</td>
                    <td>3D</tdd>
                </tr>
                <tr>
                    <td>Rumus Luas</td>
                    <td>:</td>
                    <td> 2*(p x L + p x t + L x t)</td>
                </tr>
                <tr>
                    <td>Parameter 1</td>
                    <td>:</td>
                    <td>4 cm</td>
                </tr>
                <tr>
                    <td>Parameter 2</td>
                    <td>:</td>
                    <td>3 cm</td>
                </tr>
                 <tr>
                    <td>Parameter 3</td>
                    <td>:</td>
                    <td>5 cm</td>
                </tr>
                <tr>
                    <td>Luas</td>
                    <td>:</td>
                    <td> """
print luas(4, 3, 5)
print """cm</td>
                </tr>
            <table>
        </body>
    </html>"""
                    
                    
