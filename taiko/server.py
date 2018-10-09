import socket
import pickle
from threading import Thread
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import matplotlib.animation as animation


# Sent for figure
font = {'size': 9}
matplotlib.rc('font', **font)

# Setup figure and subplots
f0 = figure(num=0, figsize=(12, 8))  # , dpi = 100)
f0.suptitle("Sensor plot", fontsize=12)
l_ax = []
r_ax = []
label_name = ['ax','ay','az','gx','gy','gz']

# Data Placeholders
l_data={}
r_data={}
t1 = zeros(50).tolist()
t2 = zeros(50).tolist()

# set plots
plot_l = []
plot_r = []

for i in range(6):
    l_ax.append(subplot2grid((6,2), (i,0)))
    r_ax.append(subplot2grid((6,2), (i,1)))

for i in range(6):
    # set y-limits
    if i<3:
        l_ax[i].set_ylim(-20, 20)
        r_ax[i].set_ylim(-20, 20)
    else:
        l_ax[i].set_ylim(-50, 50)
        r_ax[i].set_ylim(-50, 50)
    # Turn on grids
    l_ax[i].grid(True)
    r_ax[i].grid(True)
    # set label names
    l_ax[i].set_ylabel(label_name[i])

    # set data init value
    l_data[label_name[i]] = zeros(50).tolist()
    r_data[label_name[i]] = zeros(50).tolist()

    # set plot
    plot_l.append(l_ax[i].plot(0, 0, 'b-', label=label_name[i])[0])
    plot_r.append((r_ax[i].plot(0, 0, 'k-', label=label_name[i])[0]))

# set label names
l_ax[5].set_xlabel("time")
r_ax[5].set_xlabel("time")

# set lagends
# ax01.legend([l1], [l1.get_label()])
# ax02.legend([r1], [r1.get_label()])

def updateData(self):

    for i in range(6):
        plot_l[i].set_data(t1[-50:], l_data[label_name[i]][-50:])
        plot_l[i].axes.set_xlim(t1[-50],t1[-1])

        plot_r[i].set_data(t2[-50:], r_data[label_name[i]][-50:])
        plot_r[i].axes.set_xlim(t2[-50],t2[-1])


def client_thread(connection, ip, port):
    is_activate =True
    print('%s connected!' %ip)
    while is_activate:
        buf = connection.recv(1024)
        try:
            data = pickle.loads(buf)
        except:
            continue

        if data[-1]=='Q':
            print("client reqest to quit")
            is_activate = False
            connection.close()
        else:
            time=data[-2]
            if data[-1]=='L':
                if time%20==0:
                    time /= 100.0
                    for i in range(6):
                        l_data[label_name[i]].append(data[i+1])
                    t1.append(time)
                    # print("left: %s "%data[-10:])

            elif data[-1]=='R':
                if time%20==0:
                    time /= 100.0
                    for i in range(6):
                        r_data[label_name[i]].append(data[i+1])
                    t2.append(time)
                    # print("right: %s "%data[-10:])

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind(('', 8001))
sock1.listen()
print('wait for connect1...\n')

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind(('', 8002))
sock2.listen()
print('wait for connect2...\n')

while True:
    connection, address = sock1.accept()
    print('connect by: ', address)
    ip1, port1 = str(address[0]), str(address[1])

    connection2, address2 = sock2.accept()
    print('connect by: ', address2)
    ip2, port2 = str(address2[0]), str(address2[1])

    try:
        new_thread = Thread(target=client_thread, args=(connection, ip1, port1)).start()
        new_thread = Thread(target=client_thread, args=(connection2, ip2, port2)).start()

    except:
        print("Thread did not start")

    ani = animation.FuncAnimation(f0, updateData, interval=200)
    plt.show()

sock.close()

