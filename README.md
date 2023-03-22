# Testing NeRFS as INRs of Depth

This is the code-base for the research paper. TBD

Predicted scenes represented as point-clouds can be constructed with matplotlib as shown below:

![siren](https://user-images.githubusercontent.com/64833452/226962178-ceef5a4f-6317-40eb-9703-5dc7a7eaa622.gif)



<details>
<summary>Folders/Files</summary>
<br>

`modules` contains the network modules for our case study (Gauss, SIREN, WIRE and RELU activated NeRF architectures).

`runfile.py` can be configured to run training/evaluation, generate the scene and visualise the scene

`run_load_state.py` can be used to load the state of an experiment/network and display the scene/render images of the views. (Note that we have hard coded the image rendering step. If you change the number of rays in each view/the number of views, remeber to change `trainer.disp_heat()` in `trainer.py`)

`scene.py` defines the scene handler - setting up geometries and solving the GT targets. The `Scene` class also handles the interfacing with `Trainer`.

`trainer.py` defines the training / visualisation handler - it trains given networks and visualises the 3D scene with and without predicted results.

`utils_.py` defines the accuracy,loss and other necessary calculation functions
</details>

<details>
<summary>Installation (reproductability)</summary>
<br>
To note: We used a conda env with CUDA 13 with RTX 3090 and i10 processors on Windows. ~Hasn't been tested on other PCs yet~

Using Python 3.8, and installing the following packages  
```
pip install matplotlib==3.7.1, numpy==1.24.2, tensordict==0.0.2b0
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 -f https://download.pytorch.org/whl/torch_stable.html
```

IMPORTANT: `tensordict` needs to be `v0.0.2b0` not higher
</details>


<details>
<summary>Notes for Configuration and Running</summary>
<br>

The geometry (of cuboid volumes and rays) is hard coded into `scene.py`, however you can still modify the components (add more cubes or views) by adding to the `build_blocks` and `build_rays` function. If you do this and then wish to render images, remeber to change the `trainer.disp_heat()` function in `trainer.py` (this provides a heatmap of the depth-wise images relative to the three views we define).

For training, you can configure the params in `runfile.py` and this can be run for a number of models.

For visualisation you can use `scene.disp_scene` to plot the 3D view of scene with option to include ray-views, cubes and GT intersections. We can visualise predicted scene using `scene.disp_pred_scene`.

</details>
