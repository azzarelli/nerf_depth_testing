import copy

import matplotlib.pyplot as plt
import tensordict
import torch
import numpy as np

fig, (axA) = plt.subplots(1,1)
axA.title.set_text(' Accuracy')

col = ['#1E5631', '#0700C4', '#910000','#FE036A', 
        '#A4DE02', '#0000FF', '#6B0000', '#F5347F', 
        '#76BA1B','#0052FF', '#D32431', '#FC72A5',
        '#4C9A2A', '#007AFF', '#FF3F3D','#F99DBC', 
        '#ACDF87', '#00A3FF','#FF6B6B', '#FEC2D6'
]

experiment_title = 'Redo 1'
trackers = torch.load(f'results/history_{experiment_title}.pt').to_dict()
mean = {'S':[], 'G':[], 'R':[], 'W':[]}
psnrmean = {'S':[], 'G':[], 'R':[], 'W':[]}

for t in trackers:
    if 'SIREN' in t:
        mean['S'].append(trackers[t]['accuracy'][-1].item())
        psnrmean['S'].append(trackers[t]['psnr'][-1].item())
    elif 'Gauss' in t:
        mean['G'].append(trackers[t]['accuracy'][-1].item())
        psnrmean['G'].append(trackers[t]['psnr'][-1].item())
    elif 'WIRE' in t:
        mean['W'].append(trackers[t]['accuracy'][-1].item())
        psnrmean['W'].append(trackers[t]['psnr'][-1].item())
    elif 'RELU' in t:
        mean['R'].append(trackers[t]['accuracy'][-1].item())
        psnrmean['R'].append(trackers[t]['psnr'][-1].item())

for k in mean:
    m = np.array(mean[k])
    p = np.array(psnrmean[k])
    
    mm = np.mean(m)
    pm = np.mean(p)
    ms = np.std(m)
    ps = np.std(p)

    print(f'For {k} :')
    print(f'    WAPE: {mm} +- {ms}')
    print(f'    PSNR: {pm} +- {ps}')

# print(trackers)
exit()
t = None
for i, key in enumerate(trackers.keys()):
    if t == None: t = trackers[key]["accuracy"]
    else: t = t + trackers[key]["accuracy"]
    # axA.plot(trackers[key]["accuracy"], color=col[i], label=f'{key}', alpha=.5)
axA.plot(t/6., color=col[0], label=f'{experiment_title}', alpha=.5)

experiment_title = 'WIRE_Six'
trackers = torch.load(f'results/history_{experiment_title}.pt').to_dict()

t = None
for i, key in enumerate(trackers.keys()):
    if t == None: t = trackers[key]["accuracy"]
    else: t = t + trackers[key]["accuracy"]
    # axA.plot(trackers[key]["accuracy"], color=col[i], label=f'{key}', alpha=.5)
axA.plot(t/6., color=col[1], label=f'{experiment_title}', alpha=.5)


experiment_title = 'SIREN_Six'
trackers = torch.load(f'results/history_{experiment_title}.pt').to_dict()

t = None
for i, key in enumerate(trackers.keys()):
    if t == None: t = trackers[key]["accuracy"]
    else: t = t + trackers[key]["accuracy"]
    # axA.plot(trackers[key]["accuracy"], color=col[i], label=f'{key}', alpha=.5)
axA.plot(t/6., color=col[2], label=f'{experiment_title}', alpha=.5)

experiment_title = 'Gauss_Six'
trackers = torch.load(f'results/history_{experiment_title}.pt').to_dict()

t = None
for i, key in enumerate(trackers.keys()):
    if t == None: t = trackers[key]["accuracy"]
    else: t = t + trackers[key]["accuracy"]
    # axA.plot(trackers[key]["accuracy"], color=col[i], label=f'{key}', alpha=.5)
axA.plot(t/6., color=col[3], label=f'{experiment_title}', alpha=.5)


axA.set_xlabel("Epochs")
axA.set_ylabel("Avg. Pred Difference")
axA.legend()


plt.show()

